

class figuraGeometrica:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcAreaTriangulo(self):
        area_triangulo = (self.altura * self.base) / 2
        print(f"El área del triángulo teniendo una altura de {self.altura} y una base de {self.base} es de {area_triangulo}")


calculo1 = figuraGeometrica(5,3)
calculo1.calcAreaTriangulo()