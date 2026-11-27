### Requisitos MCP:

1. **Agregar prioridad alta, media o baja; por defecto media. Rechazar otra prioridad con `ValueError`.**
2. **Crear `filtrar_por_prioridad(tareas, prioridad)`.**
3. **Conservar `agregar(tareas, titulo)` y `pendientes(tareas)`.**
4. **Agregar pruebas válidas, inválidas y de regresión.**

### Código Base:

```python
def agregar(tareas, titulo):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("Título obligatorio")
    tarea = {"id": len(tareas) + 1, "titulo": titulo, "prioridad": "media"}
    tareas.append(tarea)
    return tarea


def pendientes(tareas):
    return list(tareas)
```

### Definición de Pasos:

1. **Agregar prioridad alta, media o baja; por defecto media. Rechazar otra prioridad con `ValueError`.**
   - Crear una función `agregar_prioridad(tareas, titulo, prioridad)` que acepte un tercer argumento `prioridad`.
   - Validar que la `prioridad` sea uno de los valores válidos: "alta", "media" o "baja".
   - Si la `prioridad` no es válida, lanzar un `ValueError`.

2. **Crear `filtrar_por_prioridad(tareas, prioridad)`.**
   - Crear una función `filtrar_por_prioridad(tareas, prioridad)` que filtre las tareas por la `prioridad` especificada.

3. **Conservar `agregar(tareas, titulo)` y `pendientes(tareas)`.**
   - Mantener las funciones `agregar(tareas, titulo)` y `pendientes(tareas)` sin cambios.

4. **Agregar pruebas válidas, inválidas y de regresión.**
   - Crear una clase de pruebas que incluya pruebas válidas, inválidas y de regresión.

### Código Actualizado:

```python
def agregar(tareas, titulo, prioridad="media"):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("Título obligatorio")
    if prioridad not in ["alta", "media", "baja"]:
        raise ValueError("Prioridad inválida. Debe ser 'alta', 'media' o 'baja'.")
    tarea = {"id": len(tareas) + 1, "titulo": titulo, "prioridad": prioridad}
    tareas.append(tarea)
    return tarea


def pendientes(tareas):
    return list(tareas)


def filtrar_por_prioridad(tareas, prioridad):
    return [tarea for tarea in tareas if tarea["prioridad"] == prioridad]
```

### Pruebas:

```python
import unittest

class TestTareas(unittest.TestCase):
    def setUp(self):
        self.tareas = []

    def test_agregar_valida(self):
        tarea = agregar(self.tareas, "Tarea 1")
        self.assertEqual(tarea, {"id": 1, "titulo": "Tarea 1", "prioridad": "media"})
        self.assertEqual(len(self.tareas), 1)

    def test_agregar_invalida_titulo(self):
        with self.assertRaises(ValueError):
            agregar(self.tareas, "")

    def test_agregar_invalida_prioridad(self):
        with self.assertRaises(ValueError):
            agregar(self.tareas, "Tarea 2", "alta")

    def test_pendientes(self):
        tarea1 = agregar(self.tareas, "Tarea 1")
        tarea2 = agregar(self.tareas, "Tarea 2")
        self.assertEqual(pendientes(self.tareas), [tarea1, tarea2])

    def test_filtrar_por_prioridad(self):
        tarea1 = agregar(self.tareas, "Tarea 1", "alta")
        tarea2 = agregar(self.tareas, "Tarea 2", "media")
        tarea3 = agregar(self.tareas, "Tarea 3", "baja")
        self.assertEqual(filtrar_por_prioridad(self.tareas, "alta"), [tarea1])
        self.assertEqual(filtrar_por_prioridad(self.tareas, "media"), [tarea2])
        self.assertEqual(filtrar_por_prioridad(self.tareas, "baja"), [tarea3])
        self.assertEqual(filtrar_por_prioridad(self.tareas, "alta"), [tarea1])
        self.assertEqual(filtrar_por_prioridad(self.tareas, "media"), [tarea2])
        self.assertEqual(filtrar_por_prioridad(self.tareas, "baja"), [tarea3])

if __name__ == "__main__":
    unittest.main()
```

### Conservación de la API:

- **Conservar `agregar(tareas, titulo)` y `pendientes(tareas)`:** No se han realizado cambios en estas funciones.
- **Conservar `filtrar_por_prioridad(tareas, prioridad)`:** Se ha creado una nueva función para filtrar las tareas por prioridad.

### Pruebas:

- **Pruebas válidas:** Verificar que las tareas se agregan correctamente con diferentes prioridades y que el método `pendientes` funciona correctamente.
- **Pruebas inválidas:** Verificar que se lanza un `ValueError` cuando se intenta agregar un título vacío o una prioridad inválida.
- **Pruebas de regresión:** Verificar que las pruebas anteriores siguen funcionando después de realizar cambios en el código.