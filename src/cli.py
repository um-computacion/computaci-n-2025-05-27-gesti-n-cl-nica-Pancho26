from src.clinica import Clinica
from src.modelos import Paciente, Medico, Especialidad
from src.excepciones import *
from datetime import datetime

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            op = input("Opción: ")
            try:
                if op == "1":
                    self.agregar_paciente()
                elif op == "2":
                    self.agregar_medico()
                elif op == "3":
                    self.agendar_turno()
                elif op == "4":
                    self.agregar_especialidad()
                elif op == "5":
                    self.emitir_receta()
                elif op == "6":
                    self.ver_historia_clinica()
                elif op == "7":
                    self.ver_turnos()
                elif op == "8":
                    self.ver_pacientes()
                elif op == "9":
                    self.ver_medicos()
                elif op == "0":
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida")
            except Exception as e:
                print(f"Error: {e}")

    def agregar_paciente(self):
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        fecha = input("Fecha nacimiento (dd/mm/aaaa): ")
        paciente = Paciente(nombre, dni, fecha)
        self.clinica.agregar_paciente(paciente)
        print("Paciente agregado.")

    def agregar_medico(self):
        nombre = input("Nombre: ")
        matricula = input("Matrícula: ")
        medico = Medico(nombre, matricula)
        self.clinica.agregar_medico(medico)
        print("Médico agregado.")

    def agendar_turno(self):
        dni = input("DNI paciente: ")
        matricula = input("Matrícula médico: ")
        especialidad = input("Especialidad: ")
        fecha_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
        fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
        self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
        print("Turno agendado.")

    def agregar_especialidad(self):
        matricula = input("Matrícula médico: ")
        tipo = input("Especialidad: ")
        dias = input("Días de atención (separados por coma): ").split(",")
        dias = [d.strip().lower() for d in dias]
        especialidad = Especialidad(tipo, dias)
        medico = self.clinica.obtener_medico_por_matricula(matricula)
        medico.agregar_especialidad(especialidad)
        print("Especialidad agregada.")

    def emitir_receta(self):
        dni = input("DNI paciente: ")
        matricula = input("Matrícula médico: ")
        medicamentos = input("Medicamentos (separados por coma): ").split(",")
        medicamentos = [m.strip() for m in medicamentos if m.strip()]
        self.clinica.emitir_receta(dni, matricula, medicamentos)
        print("Receta emitida.")

    def ver_historia_clinica(self):
        dni = input("DNI paciente: ")
        historia = self.clinica.obtener_historia_clinica(dni)
        print(historia)

    def ver_turnos(self):
        for t in self.clinica.obtener_turnos():
            print(t)

    def ver_pacientes(self):
        for p in self.clinica.obtener_pacientes():
            print(p)

    def ver_medicos(self):
        for m in self.clinica.obtener_medicos():
            print(m)
