# Explicación general del sistema de gestión de clínica

El sistema está organizado en dos carpetas principales:  
- `src/` contiene todo el código fuente del sistema (modelos, lógica, CLI, excepciones, main).
- `test/` contiene las pruebas unitarias.

## Estructura y responsabilidades

### Modelos (`src/modelos.py`)
Define las clases principales del dominio:
- **Paciente**: almacena datos personales.
- **Medico**: almacena datos y especialidades.
- **Especialidad**: nombre y días de atención.
- **Turno**: representa una cita entre paciente y médico.
- **Receta**: medicamentos recetados por un médico a un paciente.
- **HistoriaClinica**: historial de turnos y recetas de un paciente.

Cada clase tiene atributos privados y métodos para acceder a la información y representarla en texto.

### Excepciones (`src/excepciones.py`)
Define excepciones personalizadas para manejar errores de dominio, como paciente no encontrado, médico no disponible, turno ocupado, etc.  
Esto permite separar la lógica de validación del manejo de errores en la interfaz.

### Lógica principal (`src/clinica.py`)
La clase **Clinica** es el núcleo del sistema.  
Se encarga de:
- Registrar pacientes y médicos.
- Agendar turnos validando disponibilidad y especialidad.
- Emitir recetas.
- Gestionar historias clínicas.
- Validar todas las operaciones y lanzar excepciones si hay errores.

### Interfaz de consola (`src/cli.py`)
La clase **CLI** es la interfaz de usuario por consola.  
Muestra un menú interactivo, solicita datos al usuario y llama a los métodos de la clase **Clinica**.  
No contiene lógica de negocio, solo interacción y manejo de errores para mostrar mensajes claros.

### Main (`src/main.py`)
Punto de entrada del sistema.  
Simplemente crea una instancia de la CLI y ejecuta el menú.

### Pruebas (`test/test_clinica.py`)
Incluye pruebas unitarias usando `unittest` para verificar los casos principales y errores del modelo y la lógica de la clínica.

## Ejecución

- Para usar el sistema:  
  `python -m src.main`
- Para correr los tests:  
  `python -m unittest discover test`

## Diseño

El diseño sigue principios de orientación a objetos y separación de responsabilidades:
- El modelo encapsula los datos y reglas del dominio.
- La lógica de negocio y validaciones están en la clase principal `Clinica`.
- La interfaz de consola es simple y desacoplada de la lógica.
- Las excepciones personalizadas permiten un manejo de errores claro y específico.
