class Node:
    def __init__(self, cedula, nombre, numhab):
        self.cedula = cedula
        self.nombre = nombre
        self.numhab = numhab
        self.siguiente = None
       
class Hotel:
    def __init__(self):
        self.cabecera = None
        self.habdisponible = set(range(1, 10))
        self.listEntrada = []
        self.listSalida = []

    def check_in(self, cedula, nombre, numhab):
   
        if numhab not in self.habdisponible:
            print(f"Habitacion {numhab} ocupada")
           
            return

        nuevo_nodo = Node(cedula, nombre, numhab)

        if self.cabecera is None:
            self.cabecera = nuevo_nodo
        
        else:
            nodo_actual = self.cabecera
            while(nodo_actual.siguiente):
                nodo_actual = nodo_actual.siguiente
                
            nodo_actual.siguiente = nuevo_nodo

        self.habdisponible.remove(numhab)
        self.listEntrada.append(nuevo_nodo)
        print(f"El usuario {nombre} ha sido registrado en la habitacion {numhab}.")
       
    def check_out(self,cedula):
   
        actual= self.cabecera
        anterior= None
        while actual:
            if actual.cedula == cedula:
                if actual.numhab not in self.habdisponible:
                    self.habdisponible.add(actual.numhab)
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabecera = actual.siguiente
                print(f"El usuario {actual.nombre} se ha retirado del hotel")
                self.listSalida.append(actual)
                return
            anterior = actual
            actual = actual.siguiente

        print(f"El usuario con la cedula {cedula} no se encuentra registrado")
   
    def consulta_huesped(self, cedula):
   
        actual= self.cabecera
        while actual:
            if actual.cedula == cedula:
               
                print(f"Nombre del usuario: {actual.nombre}")
                print(f"Cedula del usario: {actual.cedula}")
                print(f"Numero de Habitacion: {actual.numhab}")
               
                return
            actual = actual.siguiente

        print(f"El usuario con la cedula {cedula} no se encuentra disponible")
     
    def hab_disponible(self):
       print("Habitaciones que se encuentran disponibles:")
       organSet = sorted(list(self.habdisponible))
       for habitacion in organSet:
           print(habitacion)

    def hab_ocupada(self):
        print("Habitaciones que se encuentran ocupadas:")
        actual = self.cabecera
        while actual:
            print(f"Numero de habitacion {actual.numhab}  Usuario {actual.nombre}")
            actual = actual.siguiente  
           
    def huespedes (self, consultacedula=False):
   
        if consultacedula:
       
         print("Lista de huespedes por cedula:")
        disp = {}
        actual = self.cabecera
        while actual:
                disp[actual.cedula] = actual.nombre
                actual = actual.siguiente
        for cedula, nombre in disp.items():
                print(f"Cedula: {cedula} Usuario: {nombre}")
        else:
            print("Lista de huespedes por orden de llegada:")
            actual = self.cabecera
            while actual:
                print(f"Usuario: {actual.nombre} Habitacion: {actual.numhab}")
                actual = actual.siguiente

    def regisHuespedes(self):
        print("Los registros de quienes se han registraron es: ")
        i = 1
        j = 1
        for huesEntraron in self.listEntrada:
            print(i)
            print(f"Nombre del huesped: {huesEntraron.nombre}")
            print(f"Cedula: {huesEntraron.cedula}")
            print(f"Habitacion: {huesEntraron.numhab}")
            i = i+1
        print()
        print("Los registros de quienes ya salieron es: ")
        for huesSalieron in self.listSalida:
            print(j)
            print(f"Nombre del huesped: {huesSalieron.nombre}")
            print(f"Cedula: {huesSalieron.cedula}")
            print(f"Se hospedo en la habitacion: {huesSalieron.numhab}")
            j = j+1

hotel = Hotel()
hotel.check_in(254669, "Pablo", 8)
hotel.check_in(648523, "Valentina", 5)
hotel.check_in(325489, "David", 4)
hotel.hab_ocupada()
hotel.check_out(648523)
hotel.check_out(548654)
hotel.consulta_huesped(648523)
hotel.consulta_huesped(254669)
hotel.hab_disponible()
hotel.huespedes(consultacedula=True)
print()
hotel.regisHuespedes()