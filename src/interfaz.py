
from clinica import Clinica
from .modelos import Pacientes, Medico, Especialidad
from datetime import datetime

def mostrar_menu():
    print("\n--- Menú Clínica ---")
    print("1) Agregar paciente")
    print("2) Agregar médico")
    print("3) Agregar especialidad a médico")
    print("4) Agendar turno")
    print("5) Emitir receta")
    print("6) Ver historia clínica")
    print("7) Ver todos los pacientes")
    print("8) Ver todos los médicos")
    print("9) Ver todos los turnos")
    print("0) Salir")

def main():
    clinica = Clinica()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            dni = input("DNI: ")
            fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
            paciente = Pacientes(nombre, dni, fecha)
            clinica.agregar_paciente(paciente)
            print("Paciente agregado.")
            continue

        if opcion == "2":
            nombre = input("Nombre del médico: ")
            matricula = input("Matrícula: ")
            medico = Medico(nombre, matricula)
            clinica.agregar_medico(medico)
            print("Médico agregado.")
            continue

        if opcion == "3":
            matricula = input("Matrícula del médico: ")
            medico = clinica.obtener_medico_por_matricula(matricula)
            if not medico:
                print("Médico no encontrado.")
                continue
            tipo = input("Especialidad: ")
            dias = input("Días de atención (separados por coma): ").split(",")
            especialidad = Especialidad(tipo, dias)
            medico.agregar_especialidad(especialidad)
            print("Especialidad agregada.")
            continue

        if opcion == "4":
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            especialidad = input("Especialidad: ")
            fecha_str = input("Fecha y hora del turno (dd/mm/aaaa hh:mm): ")
            try:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
                ok = clinica.agendar_turno(dni, matricula, especialidad, fecha)
                if ok:
                    print("Turno agendado.")
                else:
                    print("No se pudo agendar el turno.")
            except:
                print("Fecha inválida.")
            continue

        if opcion == "5":
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma): ").split(",")
            ok = clinica.emitir_receta(dni, matricula, medicamentos)
            if ok:
                print("Receta emitida.")
            else:
                print("No se pudo emitir la receta.")
            continue

        if opcion == "6":
            dni = input("DNI del paciente: ")
            historia = clinica.obtener_historia_clinica(dni)
            if historia:
                print(historia)
            else:
                print("Paciente no encontrado.")
            continue

        if opcion == "7":
            for p in clinica.obtener_pacientes():
                print("-", p)
            continue

        if opcion == "8":
            for m in clinica.obtener_medicos():
                print("-", m)
            continue

        if opcion == "9":
            for t in clinica.obtener_turnos():
                print("-", t)
            continue

        if opcion == "0":
            print("Saliendo del sistema...")
            break

        print("Opción inválida.")

if __name__ == "__main__":
    main()