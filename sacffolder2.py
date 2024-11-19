class Monton():
    # Diccionario privado para almacenar los elementos y sus cantidades
    __stuff = {}

    def __init__(self, *args):
        """
        Inicializa un monton con los elementos dados en `args`.
        Si no se pasa nada, el monton se inicializa vacío.

        :para args: Elementos que se agregarán al monton (si se proporcionan).
        """
        for item in args:
            self.add(item)

    def __str__(self) -> str:
        """
        Representación en cadena del monton, mostrando los elementos y sus cantidades.

        :return: Cadena con el contenido del monton.
        """
        return f"<<montonsito: {self.__stuff}>>"

    def add(self, algo):
        """
        Agrega un nuevo elemento al monton o incrementa su cantidad si ya está presente.

        :para algo: El elemento que se desea agregar al monton.
        """
        if algo in self.__stuff:
            self.__stuff[algo] += 1  # Incrementa la cantidad si ya existe.
        else:
            self.__stuff[algo] = 1  # Añade el nuevo elemento con cantidad 1.

    def __contains__(self, algo):
        """
        Verifica si un elemento está presente en el monton.

        :para algo: Elemento a verificar en el monton.
        :return: `True` si el elemento está presente, `False` si no lo está.
        """
        return algo in self.__stuff

    def __popPgetP__(self, algo) -> object:
        """
        Obtiene una copia del elemento sin modificar el monton. 

        :para algo: Elemento a consultar.
        :return: El elemento si existe, `None` si no se encuentra.
        """
        if algo in self.__stuff:
            return algo
        else:
            return None

    def tomar(self, algo) -> object:
        """
        Obtiene una copia del elemento, reduciendo su cantidad en el monton. 
        Si el elemento no está en el monton o su cantidad es 0, no se hace nada.

        :para algo: Elemento a tomar.
        :return: El elemento si está disponible, `None` si no.
        """
        if algo in self.__stuff and self.__stuff[algo] > 0:
            self.__stuff[algo] -= 1  # Reduce la cantidad del elemento.
            return algo
        else:
            return None

    def amontona(self, algo):
        """
        Agrega un elemento o todo el contenido de otro monton al monton actual.
        Si el argumento es un monton, se agregan todos sus elementos sin vaciarlo.

        :para algo: El elemento o monton a amontonar.
        """
        if isinstance(algo, Monton):
            # Si el argumento es otro monton, agregamos sus elementos.
            for item, cantidad in algo.__stuff.items():
                for _ in range(cantidad):
                    self.add(item)
        else:
            # Si es un solo elemento, simplemente lo agregamos.
            self.add(algo)

    def contiene(self, algo) -> bool:
        """
        Verifica si un elemento está presente en el monton.

        :para algo: Elemento a verificar.
        :return: `True` si el elemento está presente, `False` si no lo está.
        """
        return algo in self.__stuff

    def copiar(self, algo) -> object:
        """
        Devuelve una copia del elemento si está presente en el monton.
        
        :para algo: Elemento a copiar.
        :return: El elemento copiado si existe, `None` si no existe.
        """
        return self.__popPgetP__(algo)

# Ejemplo de uso de la clase `Monton`
if __name__ == "__main__":
    m0 = Monton()  # Crea un monton vacío
    print(m0) 

    m1 = Monton("algo")  # Crea un monton con un único elemento "algo"
    print(m1)  

    m1.amontona("algo mas")  # Añade "algo mas" a m1
    print(m1)  # Imprime el estado de m1 después de amontonar

    # Verificación de la presencia de elementos en m1
    assert m1.contiene("algo")
    assert m1.contiene("algo mas")
    assert not m1.contiene("perla")

    m1.amontona("perla")  # Añade "perla" a m1
    print(m1)  # Verifica que "perla" ha sido añadido

    # Verificación después de añadir "perla"
    assert m1.contiene("perla")

    m1.amontona("y mas mierdas")  # Añade más elementos a m1
    print(m1)

    # Ahora amontonamos todo de m1 a m0 sin vaciar m1
    m0.amontona(m1)
    print(m0) 

    # Consultamos y obtenemos una copia de "perla" de m0
    predicado = m0.contiene("perla")  # True
    print(predicado)
    
    copia = m0.copiar("perla")  # "perla"
    print(copia)
    
    tesoro = m0.tomar("perla")  # "perla" se toma y se elimina de m0
    print(tesoro)

    # Verificamos que "perla" ya no está en m0 después de tomarlo
    print(m0)  
    # Verificamos que m1 sigue igual después de la operación
    print(m1)
