class Calculator:

    def __init__(self):
        self.value = 0

    def add(self, a, b):
        self.value = a + b

    def rest(self, a, b):
        self.value = a - b

    def prod(self, a, b):
        self.value = a * b

    def div(self, a, b):
        self.value = a/b

    def fact(self, a):
        if a<0:
            self.value="No se puede hacer el factorial de un número negativo"
        else:
            fact=1
            for i in range(1, a+1):
                fact= fact*i
            self.value=fact


