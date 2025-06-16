class paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni})"
