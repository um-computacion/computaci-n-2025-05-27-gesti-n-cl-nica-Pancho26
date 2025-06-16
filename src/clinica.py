from modelo import Paciente, Medico, Turno, Receta, HistoriaClinica
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

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        paciente = self.pacientes.get(dni)
        medico = self.medicos.get(matricula)

        if not paciente or not medico:
            return False

        for turno in self.turnos:
            if turno.medico == medico and turno.fecha_hora == fecha_hora:
                return False

        dia = fecha_hora.strftime('%A').lower()
        if medico.especialidad_en_dia(dia) != especialidad:
            return False

        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.turnos.append(turno)
        self.historias[dni].agregar_turno(turno)
        return True

    def emitir_receta(self, dni, matricula, medicamentos):
        paciente = self.pacientes.get(dni)
        medico = self.medicos.get(matricula)

        if not paciente or not medico or not medicamentos:
            return False

        receta = Receta(paciente, medico, medicamentos)
        self.historias[dni].agregar_receta(receta)
        return True

    def obtener_turnos(self):
        return list(self.turnos)

    def obtener_historia_clinica(self, dni):
        return self.historias.get(dni)
