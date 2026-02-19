README.txt
PROYECTO: Sistema de Gestión de Turnos Médicos
Versión: 1.0

Desarrollado en: Java (Swing para GUI)

Arquitectura: Orientación a Objetos (POO) con separación de lógica y presentación.

1. Descripción del Proyecto
Este sistema permite gestionar la reserva de turnos en un centro médico. El programa simula una base de datos de doctores y pacientes, permitiendo buscar turnos por especialidad, registrar nuevos pacientes con validaciones de seguridad y confirmar citas médicas.

Características principales:
  Búsqueda Multihilo: La búsqueda de turnos simula una carga de red/proceso mediante hilos (Threads), manteniendo la interfaz fluida.
  Validaciones Robustas: Control de DNI duplicados, formatos numéricos en edad y validación de caracteres en nombres/apellidos.
  Sistema de Beneficios: Cálculo automático de beneficios según la cobertura del paciente (Jubilado, Con Obra Social, Sin Obra Social).

2. Estructura de Clases
Main: Punto de entrada que inicializa la base de datos y la interfaz.

Persona (Clase Padre): Contiene los atributos básicos (Nombre, DNI, Edad) y lógica compartida de validación.
  Doctor: Extiende de Persona. Incluye una especialidad y una matriz aleatoria de disponibilidad semanal.
  Paciente: Extiende de Persona. Gestiona el tipo de obra social y los mensajes de beneficios.

BasedeDatos: Almacena de forma estática las listas iniciales de profesionales y pacientes.

Buscador: Lógica para filtrar doctores por especialidad y gestionar objetos TurnoDisponible.

GestorTurnos: El "Controlador" que une la lógica de búsqueda, registro y validación de reglas de negocio.

InterfaceGrafica: Vista construida en Swing que gestiona los eventos de usuario y cuadros de diálogo.

3. Requisitos del Sistema
Java SDK: Versión 17 o superior (por el uso de sintaxis moderna como _ en ActionListeners y switch mejorados).
IDE Recomendado: Eclipse, IntelliJ IDEA o NetBeans.
Resolución de pantalla: Mínimo 800x600.

4. Guía de ejecución:
Opción 1: Ejecución desde un IDE (Recomendado)
  Descargar el código: Asegúrate de tener todos los archivos .java en una carpeta llamada TP_Sistema_gestion_turnos.
  Importar el proyecto: * Abre tu IDE y selecciona "Open Project" o "Import Project".
  Selecciona la carpeta raíz que contiene el paquete.
  Configurar el Package: Verifica que la primera línea de cada archivo sea package TP_Sistema_gestion_turnos; para evitar errores de compilación.
  Ejecutar: Busca el archivo Main.java, haz clic derecho y selecciona "Run As > Java Application".

Opción 2: Ejecución desde la Terminal (Consola)
  Sigue estos comandos desde la carpeta donde se encuentra la carpeta TP_Sistema_gestion_turnos:
    1. javac TP_Sistema_gestion_turnos/*.java    (compila el proyecto)
    2. java TP_Sistema_gestion_turnos.Main       (ejecuta la aplicación)

Notas de Uso dentro de la Aplicación
  Flujo de Trabajo: Inicia ingresando Nombre, Apellido y DNI del paciente. Luego selecciona la especialidad deseada en el menú desplegable.
  Simulación de Espera: Al hacer clic en "Buscar Turno", el sistema mostrará un mensaje de "Buscando turno..." durante 5 segundos. Esto es una simulación de proceso mediante hilos para no congelar la interfaz.
  Registro de Pacientes: Si el DNI no existe en la base de datos pre-cargada, el sistema te guiará automáticamente para registrar los datos faltantes (Edad y Obra Social).
  Validaciones: El sistema no permitirá ingresar nombres con números ni edades fuera del rango de 0 a 110 años.

5. Notas de Implementación
Agendas Dinámicas: Las agendas de los doctores se inicializan de forma aleatoria cada vez que se inicia el programa.

