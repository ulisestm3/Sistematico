class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcArea(self):
        areaRectangulo = self.base*self.altura
        print(f"El area del triangulo teniendo una base de {self.base} y una altura de {self.altura} es de {areaRectangulo}")
    
calculo1 = Rectangulo(4,8)
calculo1.calcArea()