from mock.datos_mock import profesores_mock
from utils.data_utils import profesores
from classes.profesor import Profesor

def agregar():
    """Registra un profesor en la base de datos
    """
    print("\nRegistro de profesor nuevo...")
    nombres = input("Nombres (solo nombres): ")
    apellidos = input("Apellidos: ")
    dni = input("DNI: ")
    nacionalidad = input("Nacionalidad: ")
    cotizacion = float(input("Cotización /hora (USD): "))
    nuevo_profesor = Profesor(nombres, apellidos, dni, nacionalidad, cotizacion)
    profesores[dni] = nuevo_profesor
    print("Profesor registrado!\n")
    input("Press <ENTER> to continue...")

def eliminar():
    """Dar de baja un profesor. Cambia el atributo 'activo' a False para indicar que ya no se le asignará cursos
    """
    print("\nDar de baja un profesor...")
    dni = input("Ingrese DNI del profesor que desea DAR DE BAJA: ")
    profesor = Profesor(profesores[dni].nombres, profesores[dni].apellidos, profesores[dni].dni, profesores[dni].nacionalidad, profesores[dni].cotizacion, profesores[dni].cant_horas, False)
    profesores[dni] = profesor
    print("BAJA registrada!\n")
    input("Press <ENTER> to continue...")

def editar():
    """Modifica 2 de los atributos del profesor. Solo es posible modificar la Cotización /hora y la Cantidad de horas de clases realizadas
    """
    print("\nModificando los datos de profesor...")
    dni = input("Ingrese DNI del profesor que desea modificar: ")
    print("Los datos del profesor seleccionado son:")
    print(profesores[dni])
    print("\nInformación que puede actualizar:")
    print("(1): Cotización /hora")
    print("(2): Cantidad de horas\n")
    clave_para_actualizar = int(input(("Qué información desea actualizar (1 o 2): ")))
    if (clave_para_actualizar == 1):
        dato_para_actualizar = float(input(f"Cuál es el nuevo valor para [Cotizacion /hora] (USD): "))
        profesor = Profesor(profesores[dni].nombres, profesores[dni].apellidos, profesores[dni].dni, profesores[dni].nacionalidad, dato_para_actualizar, profesores[dni].cant_horas, profesores[dni].activo)
    else:
        dato_para_actualizar = int(input(f"Cuál es el nuevo valor para [Cantidad de horas]: "))
        profesor = Profesor(profesores[dni].nombres, profesores[dni].apellidos, profesores[dni].dni, profesores[dni].nacionalidad, profesores[dni].cotizacion, dato_para_actualizar, profesores[dni].activo)
    profesores[dni] = profesor
    print("Dato actualizado!\n")
    input("Press <ENTER> to continue...")

def mostrar():
    """Imprime la lista de profesores registrados
    """
    print("\nLista de profesores...")
    print(profesores)
    print("Fin de la lista de profesores.\n")
    input("Press <ENTER> to continue...")

def buscar():
    """Imprime los datos de un profesor. Se busca por el DNI
    """
    print("\nBuscando profesor...")
    dni = input("Ingrese DNI del profesor que desea buscar: ")
    print("Profesor encontrado. Sus datos son:")
    print(profesores[dni])
    print("Fin de la lista de datos de este profesor.\n")
    input("Press <ENTER> to continue...")

def cargar_mock():
    """Añade datos de prueba a la base de datos
    """
    #pretendo que los datos de prueba se agreguen al diccionario (base de datos)
    #pero no funciona. Parece que 'profesores' lo tomara como variable local solo de esta funcion
    profesores = profesores_mock
    print(profesores)  #aquí me imprime los datos de prueba, pero no los datos agregados durante la ejecución del programa

    #una posible solución: intento recorrer el diccionario de datos de ejemplo y asignarlo uno a uno al diccionario de profesores
    #pero ya no sé mas como hacerlo
    # for x in profesores_mock.items():
    #     print(x)

    input("Press <ENTER> to continue...")