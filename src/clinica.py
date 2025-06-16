from modelo import Paciente, Medico, Turno, Receta, HistoriaClinica
from exepciones import (
    PacienteNoEncontrado,
    MedicoNoEncontrado,
    TurnoOcupado,
    EspecialidadNoDisponible,
    RecetaInvalida
)
from datetime import datetime

class Clinica:
    def __init__(self):
        self.pacientes = {}
        self.medicos = {}
        self.turnos = []
        self.historias = {}

    def agregar_paciente(self, paciente):
        if paciente.dni not in self.pacientes:
            self.pacientes[paciente.dni] = paciente
            self.historias[paciente.dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        if medico.matricula not in self.medicos:
            self.medicos[medico.matricula] = medico

    def obtener_pacientes(self):
        return list(self.pacientes.values())

    def obtener_medicos(self):
        return list(self.medicos.values())

    def obtener_medico_por_matricula(self, matricula):
        return self.medicos.get(matricula)

    def obtener_paciente_por_dni(self, dni):
        return self.pacientes.get(dni)

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        paciente = self.obtener_paciente_por_dni(dni)
        if not paciente:
            raise PacienteNoEncontrado("El paciente no está registrado.")

        medico = self.obtener_medico_por_matricula(matricula)
        if not medico:
            raise MedicoNoEncontrado("El médico no está registrado.")

        for turno in self.turnos:
            if turno.medico == medico and turno.fecha_hora == fecha_hora:
                raise TurnoOcupado("Ese turno ya está ocupado.")

        dia = fecha_hora.strftime('%A').lower()
        if medico.especialidad_en_dia(dia) != especialidad:
            raise EspecialidadNoDisponible("El médico no atiende esa especialidad ese día.")

        nuevo_turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.turnos.append(nuevo_turno)
        self.historias[dni].agregar_turno(nuevo_turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        paciente = self.obtener_paciente_por_dni(dni)
        if not paciente:
            raise PacienteNoEncontrado("El paciente no está registrado.")

        medico = self.obtener_medico_por_matricula(matricula)
        if not medico:
            raise MedicoNoEncontrado("El médico no está registrado.")

        if not medicamentos:
            raise RecetaInvalida("La receta no contiene medicamentos.")

        receta = Receta(paciente, medico, medicamentos)
        self.historias[dni].agregar_receta(receta)

    def obtener_turnos(self):
        return list(self.turnos)

    def obtener_historia_clinica(self, dni):
        return self.historias.get(dni)
