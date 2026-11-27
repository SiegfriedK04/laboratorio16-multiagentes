"""Orquestación controlada de Planificador, Implementador y Revisor."""

from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

from mcp import Client
from mcp.types import TextContent
from ollama import chat

from mcp_requisitos import mcp


MODELO = "qwen2.5-coder:3b"
EVIDENCIAS = Path("evidencias")
EVIDENCIAS.mkdir(exist_ok=True)


async def leer_requisito() -> str:
    async with Client(mcp, mode="legacy") as cliente:
        resultado = await cliente.call_tool("requisito_prioridad", {})
        if resultado.is_error:
            raise RuntimeError("Falló la herramienta MCP")
        textos = [x.text for x in resultado.content if isinstance(x, TextContent)]
        if not textos:
            raise RuntimeError("MCP no devolvió bloques de texto")
        return "\n".join(textos)


def consultar(instruccion: str, datos: str) -> str:
    respuesta = chat(
        model=MODELO,
        messages=[
            {"role": "system", "content": instruccion},
            {"role": "user", "content": datos},
        ],
        options={"temperature": 0, "seed": 16},
    )
    return respuesta.message.content or ""


async def proponer() -> None:
    requisito = await leer_requisito()
    codigo = Path("tareas.py").read_text(encoding="utf-8")
    plan = consultar(
        "Eres Planificador. Define pasos, criterios de aceptación y pruebas. "
        "No escribas código, no inventes requisitos y señala cómo conservar la API.",
        f"REQUISITO MCP:\n{requisito}\n\nCÓDIGO BASE:\n{codigo}",
    )
    (EVIDENCIAS / "01_plan.md").write_text(plan, encoding="utf-8")
    propuesta = consultar(
        "Eres Implementador. Propón el contenido completo de tareas.py y tests/test_tareas.py. "
        "Conserva la API anterior, limita el cambio al requisito y no sugieras comandos de shell.",
        f"REQUISITO:\n{requisito}\n\nPLAN:\n{plan}\n\nCÓDIGO ACTUAL:\n{codigo}",
    )
    (EVIDENCIAS / "02_propuesta.md").write_text(propuesta, encoding="utf-8")
    print("Planificador -> evidencias/01_plan.md")
    print("Implementador -> evidencias/02_propuesta.md")
    print("Las propuestas requieren revisión y aplicación manual.")


async def revisar() -> None:
    requisito = await leer_requisito()
    pruebas = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    evidencia = (
        f"REQUISITO:\n{requisito}\n\n"
        f"CÓDIGO:\n{Path('tareas.py').read_text(encoding='utf-8')}\n\n"
        f"TESTS:\n{Path('tests/test_tareas.py').read_text(encoding='utf-8')}\n\n"
        f"RESULTADO (exit={pruebas.returncode}):\n{pruebas.stdout}{pruebas.stderr}"
    )
    informe = consultar(
        "Eres Revisor. Contrasta requisito, código y pruebas. Revisa regresión, seguridad y alcance. "
        "No declares aprobación si la evidencia no la demuestra.",
        evidencia,
    )
    (EVIDENCIAS / "03_revision.md").write_text(informe, encoding="utf-8")
    print("Exit code pruebas:", pruebas.returncode)
    print("Revisor -> evidencias/03_revision.md")


if __name__ == "__main__":
    modo = sys.argv[1].strip().lower() if len(sys.argv) > 1 else input("Modo (proponer/revisar): ").strip().lower()
    if modo not in {"proponer", "revisar"}:
        raise SystemExit("Use proponer o revisar")
    asyncio.run(revisar() if modo == "revisar" else proponer())
