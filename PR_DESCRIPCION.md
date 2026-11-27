# Prioridades con revisión multiagente y CI

## Objetivo

Agregar prioridad al gestor de tareas sin romper la interfaz existente.

## Requisito MCP

La herramienta `requisito_prioridad` define tres valores permitidos, prioridad media por defecto, rechazo de valores inválidos y filtro por prioridad.

## Evidencias

- `evidencias/01_plan.md`
- `evidencias/02_propuesta.md`
- `evidencias/03_revision.md`
- `evidencias/04_prueba_mcp.txt`
- `evidencias/05_pruebas_finales.txt`
- `evidencias/07_fallo_corregido.txt`

## Pruebas

`python -m unittest discover -s tests -v`

## Riesgos

- Una salida del modelo puede contener código incorrecto y siempre requiere revisión humana.
- CI confirma pruebas automatizadas, pero no demuestra por sí sola que la decisión funcional sea correcta.

## Checklist

- [x] Requisito obtenido por MCP de solo lectura
- [x] API anterior conservada
- [x] Prioridades y filtro probados
- [x] Sin secretos ni datos personales
- [x] Revisión humana previa al merge
