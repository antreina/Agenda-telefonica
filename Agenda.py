import sys
class Agenda:

    def __init__(self):
        self.nombre=[]
        self.telefono=[]
        self.email=[]

    def menu(self):
        opcion=0
        while opcion!=5:
            print("+-----------------------------------+")
            print("|************** AGENDA *************|")
            print("|- - - - - - - - - - - - - - - - - -|")
            print("| 1. Ingresar datos                 |")
            print("| 2. Listar datos                   |")
            print("| 3. Consultar datos                |")
            print("| 4. Modificar el numero telefonico |")
            print("| 5. Salir                          |")
            print("+-----------------------------------+")
            
            opcion=int(input("ingrese su opcion: "))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.consultar()
            elif opcion==4:
                self.modificar()
            elif opcion==5:
                self.salir()
                    
        
    def cargar(self):
            for x in range(2):
                nom=input("Ingrese nombre del contacto: ")
                self.nombre.append(nom)
                tel=int(input("Ingrese el numero telefonico: "))
                self.telefono.append(tel)
                em=input("Ingrese el correo electronico: \n")
                self.email.append(em)

    def listar(self):
        print("*******Lista de contactos*******")
        for x in range(2):
            print(self.nombre[x],self.telefono[x],self.email[x])
        print("___________________________________________")

    def consultar(self):
        buscar=input("Nombre del contacto a buscar: ")
        
        indice = self.nombre.index(buscar)
        print("Contacto encontrado \n",self.nombre[indice],self.telefono[indice],self.email[indice])
        print("___________________________________________")


    def modificar(self):
        buscar=input("Nombre del contacto a modificar : ") 
        indice = self.nombre.index(buscar)
        print("Numero a modificar \n",self.nombre[indice],self.telefono[indice],self.email[indice])
        
        if buscar in self.nombre[indice]:
            num=int(input("Ingrese nuevo numero:"))
            self.telefono[indice]=num
            email=input("Ingrese nuevo email:")
            self.telefono[indice]=email
                
        print("*****Modificado con exito *****\n",self.nombre[indice],self.telefono[indice],self.email[indice])
        print("___________________________________________")

    def salir(self):
        print("****Saliendo****")
        sys.exit("***ADIOS***")


agenda=Agenda()
agenda.menu()
