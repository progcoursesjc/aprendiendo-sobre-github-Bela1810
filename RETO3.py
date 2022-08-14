class Partial:
    def __init__(self,id, name, group):

        self.id = id
        self.name = name
        self.group = group

List_Courses =[]
List_Courses.append("1. Pensamiento Algoritmico")
List_Courses.append("2. Programacion Orientada")
List_Courses.append("3. Calculo I")
List_Courses.append("4. Ingles")

#Objetos
Partial1= Partial(78494, "Pensamiento Algoritmico", 63)
Partial2= Partial(46382, "Programacion Orientada", 76)
Partial3= Partial(98645, "Calculo I", 65)
Partial4= Partial(42647, "Ingles", 87)

def menu():

        print("Lista de los cursos que dicta: ")
        print("1. Pensamiento Algoritmico")
        print("2. Programacion Orientada")
        print("3. Calculo I")
        print("4. Ingles ")
    
        Option = (input("Seleccione uno de sus cursos: "))

        if Option == "1" or Option == "Pensamiento Algoritmico":
            print(f"A SELECCIONADO EL CURSO: --------{Partial1.name},ID: {Partial1.id}, GRUPO:{Partial1.group}------------")

        elif Option == "2" or Option == "Programacion Orientada":
            print(f"A SELECCIONADO EL CURSO:  -------{Partial2.name}, ID: {Partial2.id}, GRUPO: {Partial2.group}-----------")

        elif Option == "3" or Option== "Calculo I":
            print(f"A SELECCIONADO EL CURSO: --------{Partial3.name}, ID:{Partial3.id}, GRUPO:{Partial3.group}------------") 

        elif Option == "4" or Option== "Ingles":
            print(f"A SELECCIONADO EL CURSO: --------{Partial4.name}, ID:{Partial4.id}, GRUPO:{Partial4.group}------------")
             
menu()


def Test_Final():
    List_Questions=[]
    porcent= int(input("ingrese el porcentaje que desea: "))
    N_Questions= int(input("ingrese el numero de preguntas que desee: "))

    for i in range(N_Questions):
        Question = input("ingrese las preguntas: ")
        List_Questions.append(Question)

    print("")
    print("")
    print("-------------------------SU PARCIAL HA SIDO CREADO------------------------------------")
    print("")
    print(f"Porcentaje Total del Parcial:{porcent}"'%')
    print("")
    print("Estas son sus preguntas:  ----------------------------------------------------------- ")
    print("")

    for i in List_Questions:
        print(i)

    print("")
    print("--------------------------------------------------------------------------------------")

Test_Final()

  