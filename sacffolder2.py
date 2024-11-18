
class monton():
    """
    en k's: la info en forma canonica
    en v's: la cantidad
    """
    __stuff = {} 
    
    def __init__(self, *args):
        """
        Inicializa un monton con los items dados en args.
        Si no se pasa nada, el monton se inicializa vacío.
        """
        for item in args:
            self.add(item)

    def __str__(self) -> str:
        """
        Devuelves una representación en cadena del monton,
        mostrando los items y sus cantidades.
        """
        return f"<<montonsito: {self.__stuff}>>"
    
    def add(self, algo):
        """
        Agregas un nuevo elemento al monton, o incrementas su cantidad
        si ya está presente.
        """
        if algo in self.__stuff:
            self.__stuff[algo] += 1
        else:
            self.__stuff[algo] = 1

    def __contains__(self, algo):
        """
        Verificas si el item está presente en el monton.
        """
        return algo in self.__stuff

    def __popPgetP__(self, algo) -> object:
        """
        Consultas y obtienes una copia del item sin modificar el contenedor.
        """
        if algo in self.__stuff:
            return algo
        else:
            return None

    def tomar(self, algo) -> object:
        """
        Consultas y obtienes una copia del item, reduciendo su cantidad en el contenedor.
        Si el item no está en el monton o su cantidad es 0, no hace nada.
        """
        if algo in self.__stuff and self.__stuff[algo] > 0:
            self.__stuff[algo] -= 1
            return algo
        else:
            return None

    def amontona(self, algo):
        """
        Agregas un item o todo el contenido de otro monton a este monton.
        Si el argumento es un monton, se agregan todos sus elementos sin vaciarlo.
        """
        if isinstance(algo, monton):
            for item, cantidad in algo.__stuff.items():
                for int in range(cantidad):
                    self.add(item)
        else:
            self.add(algo)
    
    def contiene(self, algo) -> bool:
        """
        Verificas si un item está presente en el monton.
        """
        return algo in self.__stuff
    
    def copiar(self, algo) -> object:
        """
        Devuelves una copia del item, si está presente.
        """
        return self.__popPgetP__(algo)
    

if __name__ == "__main__":
    m0 = monton()  # m0 es un nuevo monton vacío
    print(m0) 

    m1 = monton("algo")  # m1 es un monton con "algo"
    print(m1)  

    m1.amontona("algo mas")  # Añade "algo mas" a m1
    print(m1)  # Imprime el estado de m1 después de amontonar

    # Assert: en m1 debe haber "algo" y "algo mas" y nada más
    assert m1.contiene("algo")
    assert m1.contiene("algo mas")
    assert not m1.contiene("perla")

    m1.amontona("perla")  # Añade "perla" a m1
    print(m1)  # Verifica que "perla" ha sido añadido

    # Assert: en m1 debe haber "algo", "algo mas" y "perla"
    assert m1.contiene("perla")

    m1.amontona("y mas mierdas")  # Añade más items
    print(m1)

    # Ahora amontonamos todo de m1 a m0 sin vaciar m1
    m0.amontona(m1)
    print(m0) 

    # Consultamos y obtenemos una copia de un item en m0
    predicado = m0.contiene("perla")  # True
    print(predicado)
    
    copia = m0.copiar("perla")  # "perla"
    print(copia)
    
    tesoro = m0.tomar("perla")  # "perla", y en m0 desaparece
    print(tesoro)

    print(m0)  # Verificas que "perla" ya no está en m0 después de tomarlo
    print(m1)  # Verificas que m1 sigue igual después de la operación
