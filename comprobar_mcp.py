"""Comprueba la llamada real a la herramienta MCP."""

import asyncio

from mcp import Client
from mcp.types import TextContent

from mcp_requisitos import mcp


async def main() -> None:
    async with Client(mcp, mode="legacy") as cliente:
        resultado = await cliente.call_tool("requisito_prioridad", {})
        if resultado.is_error:
            raise RuntimeError("La herramienta MCP devolvió un error")
        textos = [bloque.text for bloque in resultado.content if isinstance(bloque, TextContent)]
        print("Herramienta: requisito_prioridad")
        print("Estado: correcto")
        print("Respuesta:", "\n".join(textos))


if __name__ == "__main__":
    asyncio.run(main())
