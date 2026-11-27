import unittest

from tareas import agregar, filtrar_por_prioridad, pendientes


class TestTareas(unittest.TestCase):
    def test_agregar(self):
        tareas = []
        self.assertEqual(agregar(tareas, "Leer")["id"], 1)

    def test_prioridad_por_defecto(self):
        self.assertEqual(agregar([], "Leer")["prioridad"], "media")

    def test_prioridad_alta(self):
        tarea = agregar([], "Resolver incidente", "alta")
        self.assertEqual(tarea["prioridad"], "alta")

    def test_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            agregar([], "Leer", "urgente")

    def test_filtrar_por_prioridad(self):
        tareas = []
        agregar(tareas, "Incidente", "alta")
        agregar(tareas, "Documentar", "baja")
        agregar(tareas, "Revisar", "alta")
        self.assertEqual(
            [tarea["titulo"] for tarea in filtrar_por_prioridad(tareas, "alta")],
            ["Incidente", "Revisar"],
        )

    def test_filtro_rechaza_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            filtrar_por_prioridad([], "crítica")

    def test_pendientes_devuelve_copia(self):
        tareas = [agregar([], "Preparar evidencia")]
        copia = pendientes(tareas)
        self.assertEqual(copia, tareas)
        self.assertIsNot(copia, tareas)

    def test_titulo_vacio(self):
        with self.assertRaises(ValueError):
            agregar([], " ")


if __name__ == "__main__":
    unittest.main()
