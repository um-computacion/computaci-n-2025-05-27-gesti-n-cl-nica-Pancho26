import unittest
from datetime import datetime, timedelta
from src.clinica import Clinica
from src.modelos import Paciente, Medico, Especialidad
from src.excepciones import *

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "123", "01/01/1990")
        self.medico = Medico("Dr. House", "M001")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_registro_paciente(self):
        self.assertIn("123", [p.obtener_dni() for p in self.clinica.obtener_pacientes()])

    def test_registro_medico(self):
        self.assertIn("M001", [m.obtener_matricula() for m in self.clinica.obtener_medicos()])

    def test_turno_exitoso(self):
        fecha = datetime.now() + timedelta(days=(0 - datetime.now().weekday()) % 7)  # próximo lunes
        fecha = fecha.replace(hour=10, minute=0)
        self.clinica.agendar_turno("123", "M001", "Cardiología", fecha)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)

    def test_turno_duplicado(self):
        fecha = datetime.now() + timedelta(days=(0 - datetime.now().weekday()) % 7)
        fecha = fecha.replace(hour=10, minute=0)
        self.clinica.agendar_turno("123", "M001", "Cardiología", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("123", "M001", "Cardiología", fecha)

    def test_turno_medico_no_existe(self):
        fecha = datetime.now()
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("123", "NOEXISTE", "Cardiología", fecha)

    def test_turno_paciente_no_existe(self):
        fecha = datetime.now()
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("NOEXISTE", "M001", "Cardiología", fecha)

    def test_turno_especialidad_no_valida(self):
        fecha = datetime.now() + timedelta(days=(2 - datetime.now().weekday()) % 7)  # miércoles
        fecha = fecha.replace(hour=10, minute=0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("123", "M001", "Pediatría", fecha)

    def test_emitir_receta(self):
        self.clinica.emitir_receta("123", "M001", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("123")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("123", "M001", [])

if __name__ == "__main__":
    unittest.main()
