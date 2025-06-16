from datetime import datetime

class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni__

    def __str__(self) -> str:
        return f"{self.__nombre__} (DNI: {self.__dni__}, Nacimiento: {self.__fecha_nacimiento__})"

class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo__ = tipo
        self.__dias__ = [d.lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo__

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias__

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias__)
        return f"{self.__tipo__} (Días: {dias_str})"

class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__ = []

    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades__.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula__

    def obtener_especialidad_para_dia(self, dia: str):
        for esp in self.__especialidades__:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades = "; ".join(str(e) for e in self.__especialidades__)
        return f"{self.__nombre__} (Matrícula: {self.__matricula__}) - Especialidades: {especialidades}"

class Turno:
    def __init__(self, paciente, medico, fecha_hora: datetime, especialidad: str):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad

    def obtener_medico(self):
        return self.__medico__

    def obtener_fecha_hora(self):
        return self.__fecha_hora__

    def __str__(self):
        return (f"Turno: {self.__fecha_hora__} - Paciente: {self.__paciente__} - "
                f"Médico: {self.__medico__} - Especialidad: {self.__especialidad__}")

class Receta:
    def __init__(self, paciente, medico, medicamentos: list[str]):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = datetime.now()

    def __str__(self):
        meds = ", ".join(self.__medicamentos__)
        return (f"Receta ({self.__fecha__:%d/%m/%Y}): {self.__paciente__} - "
                f"Médico: {self.__medico__} - Medicamentos: {meds}")

class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente__ = paciente
        self.__turnos__ = []
        self.__recetas__ = []

    def agregar_turno(self, turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos__)

    def obtener_recetas(self):
        return list(self.__recetas__)

    def __str__(self):
        turnos = "\n".join(str(t) for t in self.__turnos__)
        recetas = "\n".join(str(r) for r in self.__recetas__)
        return (f"Historia clínica de {self.__paciente__}\n"
                f"Turnos:\n{turnos}\nRecetas:\n{recetas}")
