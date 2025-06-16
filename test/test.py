
import unittest
from datetime import datetime
import sys
import os


sys.path.append(os.path.abspath("src"))

from modelo import Paciente, Medico, Especialidad
from clinica import Clinica

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. Gómez", "M001")
        self.especialidad = Especialidad("Clínica", ["lunes", "miércoles"])

        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)

    def test_agregar_paciente(self):
        self.assertIn("12345678", self.clinica.pacientes)

    def test_agregar_medico(self):
        self.assertIn("M001", self.clinica.medicos)

    def test_agendar_turno_exitoso(self):
        fecha_mal = datetime.strptime("17/06/2025 09:00", "%d/%m/%Y %H:%M")  # martes
        with self.assertRaises(Exception):
            self.clinica.agendar_turno("12345678", "M001", "Clínica", fecha_mal)

        fecha_ok = datetime.strptime("16/06/2025 09:00", "%d/%m/%Y %H:%M")  # lunes
        self.clinica.agendar_turno("12345678", "M001", "Clínica", fecha_ok)
        self.assertEqual(len(self.clinica.turnos), 1)

    def test_turno_duplicado(self):
        fecha = datetime.strptime("16/06/2025 10:00", "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno("12345678", "M001", "Clínica", fecha)
        with self.assertRaises(Exception):
            self.clinica.agendar_turno("12345678", "M001", "Clínica", fecha)

    def test_emitir_receta_valida(self):
        self.clinica.emitir_receta("12345678", "M001", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.recetas), 1)

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(Exception):
            self.clinica.emitir_receta("12345678", "M001", [])

    def test_historia_clinica(self):
        self.clinica.emitir_receta("12345678", "M001", ["Vitamina C"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIsNotNone(historia)
        self.assertEqual(len(historia.recetas), 1)

if __name__ == '__main__':
    unittest.main()
