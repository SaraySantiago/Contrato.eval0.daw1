# from marvelous import rainbow

class monton():
 
   # __stuff = {} # bronce
    # __stuff = () # bronce
    stuff = [] # plata
    # __stuff = "" # PARA MASOCAS
    # __stuff = ... import maravilla # GLORIA
    
    def __init__(self, *args):
        """init regular y de copia"""
        self.stuff = []
        for item in args:
            self.amontona(item)

    def __str__(self)-> str:
        """doc..."""
        answ = "<<"
        for item in self.stuff:
            answ += f"{str(item)}, "
            answ += ">>"
            return answ 
                
    def amontona(self, algo):
        """si algo no es monton, al monton. Si algo es monton, todo lo que tiene, al monton"""
        if isinstance(algo, monton):
            self.stuff.extend(algo.stuff)
        else:
            self.stuff.append(algo)

    def contiene(self, algo) -> bool:
        return algo in self.stuff

    def copiar(self, algo) -> object:
        if algo in self.stuff:
            return algo
        return None  #TODO: Raise ValueError

    def tomar(self, algo) -> object:
        if algo in self.stuff:
            self.stuff.remove(algo)
            return algo
        return None #TODO: Raise ValueError

if __name__ == "__main__":
    
    m0 = monton()        # m0 es un nuevo monton vacio
    print("m0: ", m0)
    
    m2 = monton ("mas", "tomas")
    print ("m2: ", m2)
    
    m3 = monton (11, "doce", 13, m2)
    print ("m3: ", m3)

    m1 = monton("algo")  # m0 es un nuevo monton con "algo"
    m1.amontona("algo mas")
    # assert: en m1 hay "algo" y "algo mas" y NADA MAS.

    exit(0) # ==ir bajando...===========================

    m1.amontona("perla")
    # assert: en m1 hay "algo" y "algo mas" y "perla" y NADA MAS.

    m1.amontona("y mas mierdas")
    # assert: en m1 hay ...

    # puedo amontonar -todo lo que haya- en un monton en otro moton. Esto no vacia el monton argumentado (m1 aqui). Esto no vacia previamente el monton invocado (m0 aqui). no ~ m0 = m1
    m0.amontona(m1)

    predicado = m0.contiene("perla") # predicado == True
    copia = m0.copiar("perla") # copia == "perla"
    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"