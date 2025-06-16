from datetime import datetime

class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni})"


class Especialidad:
    def __init__(self, tipo, dias):
        self.tipo = tipo
        self.dias = [dia.lower() for dia in dias]

    def verifica_dia(self, dia):
        return dia.lower() in self.dias

    def __str__(self):
        return f"{self.tipo} (Días: {', '.join(self.dias)})"


class Medico:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.especialidades = []

    def agregar_especialidad(self, especialidad):
        self.especialidades.append(especialidad)

    def especialidad_en_dia(self, dia):
        for e in self.especialidades:
            if e.verifica_dia(dia):
                return e.tipo
        return None

    def __str__(self):
        esp = "\n  - ".join(str(e) for e in self.especialidades)
        return f"{self.nombre} (Matrícula: {self.matricula})\n  - {esp}"


class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.especialidad = especialidad

    def __str__(self):
        fecha = self.fecha_hora.strftime('%d/%m/%Y %H:%M')
        return f"Turno: {self.paciente.nombre} con {self.medico.nombre} - {self.especialidad} - {fecha}"


class Receta:
    def __init__(self, paciente, medico, medicamentos):
        self.paciente = paciente
        self.medico = medico
        self.medicamentos = medicamentos
        self.fecha = datetime.now()

    def __str__(self):
        meds = ", ".join(self.medicamentos)
        return f"Receta para {self.paciente.nombre} - Médico: {self.medico.nombre} - Medicamentos: {meds} - Fecha: {self.fecha.strftime('%d/%m/%Y')}"


class HistoriaClinica:
    def __init__(self, paciente):
        self.paciente = paciente
        self.turnos = []
        self.recetas = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def __str__(self):
        texto = f"Historia Clínica de {self.paciente.nombre}\n\nTurnos:\n"
        for turno in self.turnos:
            texto += f"- {turno}\n"
        texto += "\nRecetas:\n"
        for receta in self.recetas:
            texto += f"- {receta}\n"
        return texto