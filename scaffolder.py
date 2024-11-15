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

    def __contains__ (self, algo):
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
    pass 