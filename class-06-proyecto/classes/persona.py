class Persona:
    """Clase padre Persona

    Args:
        nombres: str
        apellidos: str
        dni: str
        nacionalidad: str
    """
    def __init__(
            self, 
            nombres: str, 
            apellidos: str, 
            dni: str, 
            nacionalidad: str
        ):
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Resumen de la Clase Persona:\n \
                Nombres: {self.nombres}\n \
                Apellidos: {self.apellidos}\n \
                DNI: {self.dni}\n \
                Nacionalidad: {self.nacionalidad}\n"

if (__name__ == "__main__"):
    print("Módulo persona")

    persona = Persona("Alex", "Marin Mendez", "18205786", "Peruana")
    print(persona)