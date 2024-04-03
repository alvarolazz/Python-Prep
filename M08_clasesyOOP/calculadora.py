class Calculadora:
    def __init__(self,lista):
        self.lista = lista
    def esprimo(self):
        for x in self.lista:
            if (self.__esprimo(x)):
                print('el elemento ',x, 'si es primo')
            else:
                print('el elemento', x, 'no es primo')
    def conversor_de_temperatura(self,u1,u2):
        for x in self.lista:
            print(x, 'grados', u1, 'equivalen a ', self.__conversor_de_temperatura(x,u1,u2), 'grados', u2 )
    def factorial(self):
        for x in self.lista:
            print('El factorial de ', x, 'es', self.__factorial(x))
    def __esprimo(self, numero):
        primo = True
        for x in range(2,numero):
            if numero % x == 0:
                primo = False
                break
        return primo
    def __conversor_de_temperatura(self,v,u1,u2):
        temperatura = 0
        if u1 == 'F' and u2 == 'C':
            temperatura = ((float(v) - 32) * 5 / 9)
        
        elif u1 == 'F' and u2 == 'K':
            temperatura = ((float(v) - 32) * 5 / 9) + 273.15

        elif u1 == 'F' and u2 == 'F':
            temperatura = v
            
        elif u1 == 'K' and u2 == 'C':
            temperatura = v - 273.15
            
        elif u1 == 'K' and u2 == 'F':
            temperatura = (((v - 273.15) * 9/5) + 32) 

        elif u1 == 'K' and u2 == 'K':
            temperatura = v
            
        elif u1 =='C' and u2 == 'F':
            temperatura = (v * 9/5) + 32
            
        elif u1 == 'C' and u2 == 'K':
            temperatura = v + 273.15

        elif u1 == 'C' and u2 == 'C':
            temperatura = v
        else:
            print('Parametros incorrectos')

        return temperatura
    def __factorial(self,num):
    
        if type(num) != int:
            return 'El numero debe ser entero'
        elif num < 0:
            return 'El numero debe ser positivo'
        elif num <= 1:
            return 1
        else:
            num = num * self.__factorial(num - 1)
        return num