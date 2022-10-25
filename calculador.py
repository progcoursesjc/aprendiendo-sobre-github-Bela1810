class Calculator:
    def __init__(self):
        self.result = 0
    
    def numbers(self):
        try:
            valor= input("Ingrese numeros y operacion a realizar: ")
            number1 = all(element.isdigit() for element in valor.split()[0])   ##Split se utiliza para dividir o separar un string en partes
            simbolo = all(element.isdigit() for element in valor.split()[1])
            number2 = all(element.isdigit() for element in valor.split()[2])
         
            print("Escriba TERMINAR para salir")
            valor=valor.lower()
            Calculator.operar(valor,self)

        except:
            if len(valor.split()) != 3:
                print("Recuerda separar los digitos")
                c.numbers()
    
    def operacion(valor,self):
            if valor != "TERMINAR":
                try:
                    if valor.split()[1] == "+":
                        self.resultado = int(valor.split()[0]) + int(valor.split()[2])
                        print(f"El resultado es:  {self.resultado:.2f}")
                        self.numbers()
                    elif valor.split()[1] == "-":
                        self.resultado = int(valor.split()[0]) - int(valor.split()[2])
                        print(f"El resultado es: {self.resultado:.2f}")
                        self.numbers()
                    elif valor.split()[1] == "*":
                        self.resultado = int(valor.split()[0]) * int(valor.split()[2])
                        print(f"El resultado es:  {self.resultado:.2f}")
                        self.numbers()
                    elif valor.split()[1] == "/":
                        self.resultado = int(valor.split()[0]) / int(valor.split()[2])
                        print(f"El resultado es:  {self.resultado:.2f}")
                        self.numbers()
                except incorrect:
                    print("Solo se ingresan numeros")
                    self.numbers()
                except DivisionporCero:
                    print("No es posible dividir por cero, ingresa otra operacion")
                    self.numbers()
          
class DivisionporCero(ZeroDivisionError):
    pass
class incorrect(ValueError):
    pass

                
c = Calculator()
c.numbers()
