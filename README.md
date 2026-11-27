# Gestor de tareas con revisión multiagente

Proyecto del Laboratorio 16. La especificación se consulta mediante una herramienta MCP de solo lectura. Los agentes Planificador, Implementador y Revisor escriben únicamente archivos de evidencia; la persona aplica y aprueba los cambios.

## Requisitos

- Python 3.12
- Ollama con `qwen2.5-coder:3b`
- Paquetes de `requirements.txt`

## Ejecución

```powershell
python comprobar_mcp.py
python multiagentes.py proponer
python -m unittest discover -s tests -v
python multiagentes.py revisar
```

La automatización de GitHub prueba el cambio en cada PR. Después de integrar a `main`, el job `delivery` genera `paquete-lab`; no despliega software en producción.
