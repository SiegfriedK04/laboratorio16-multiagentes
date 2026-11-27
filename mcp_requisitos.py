"""Servidor MCP de solo lectura con el requisito aprobado del laboratorio."""

from mcp.server import MCPServer


mcp = MCPServer("RequisitosLab16Gabriel")


@mcp.tool()
def requisito_prioridad() -> str:
    """Devuelve el requisito autorizado para el gestor de tareas."""
    return (
        "Agregar prioridad alta, media o baja; por defecto media. "
        "Rechazar otra prioridad con ValueError. "
        "Crear filtrar_por_prioridad(tareas, prioridad). "
        "Conservar agregar(tareas, titulo) y pendientes(tareas). "
        "Agregar pruebas válidas, inválidas y de regresión."
    )
