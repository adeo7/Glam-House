import datetime

class especialidad:
    def __init__(self,nombre):
        self.nombre=nombre

class persona:
     def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.apellido = correo
        self.telefono = telefono

class empleado(persona):
    def __init__(self, nombre, correo, telefono, especialidad):
        super().__init__(nombre, correo, telefono)
        self.especialidad = especialidad

class cliente(persona):
    def __init__(self, nombre, correo, telefono, sexo):
        super().__init__(nombre, correo, telefono)
        self.sexo = sexo

class servicio(especialidad):
    def __init__(self, nombre, precio):
        super().__init__(nombre)
        self.precio = precio

class cita:
    def __init__(self, cliente, servicio, fecha, hora, atendida = False):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.hora = hora
        self.atendida = atendida
    def Atender(self):
        self.atendida=True

class ServiciosPrestados:
    def __init__(self, cliente, servicio, empleado):
        self.cliente = cliente
        self.servicio = servicio
        self.empleado = empleado

espe1=especialidad("Corte de Cabello")
espe2=especialidad("Maquillaje y peinado")
espe3=especialidad("Uñas")
espe4=especialidad("Diseño y depilado de cejas")
espe5=especialidad("Tratamientos Capilares")

ListaEmpleados=[]
listaClientes=[]
listaEspecialidad=[espe1,espe2,espe3,espe4,espe5]
listaServicios=[]
listaCitas=[]
listaServiciosPrestado=[]

def agregarEspecialidad():
    nombre=input("Por favor ingresa el nombre de la especialidad: ")
    miEspecialidad=especialidad(nombre)
    listaEspecialidad.append(miEspecialidad)
    print("especialidad agregada correctamente")

def registrarEmpleado():
    nombre=input("Por favor ingresa el nombre del empleado: ")
    correo=input("Por favor ingresa el correo del empleado: ")
    telefono=input("Por favor ingresa el telefono del empleado: ")
    for i, espe in  enumerate(listaEspecialidad):
        print(f"{i}. {espe.nombre}")
    index=int(input("escoge una de las opciones anteriores"))
    especialidad=listaEspecialidad[index]
    UnEmpleado=empleado(nombre, correo, telefono, especialidad)
    ListaEmpleados.append(UnEmpleado)

def agregarCliente():
     nombre=input("Por favor ingresa el nombre del Cliente: ")
     correo=input("Por favor ingresa el correo del cliente: ")
     telefono=input("Por favor ingresa el telefono del cliente: ")
     sexo=input("Por favor ingresa el sexo del cliente: ")
     miCliente=cliente(nombre, correo, telefono, sexo)
     listaClientes.append(miCliente)

def agregarServicios():
    nombre=input("Por favor ingresa el nombre del servicio: ")
    precio=int(input("Por favor ingresa el precio del servicio: "))
    miServicio=servicio(nombre, precio)
    listaServicios.append(miServicio)

def agregarCita():
    for indice, cliente in enumerate(listaClientes):
        print(f"{indice}. {cliente.nombre}")
    indexC=int(input("Por favor ingresa el numero del cliente: "))
    clienteCita=listaClientes[indexC]
    for indice, servi in enumerate(listaServicios):
        print(f"{indice}. {servi.nombre}")
    indexS=int(input("Por favor ingresa el numero del servicio: "))
    servicioCita=listaServicios[indexS]
    anio=int(input("por favor ingresa el año de la cita"))
    mes=int(input("por favor ingresa el mes de la cita"))
    dia=int(input("por favor ingresa el dia de la cita"))
    fecha=datetime.date(anio, mes, dia)
    hora=int(input("por favor ingresa en formato militar solo la hora de la cita"))
    min=int(input(f"la cita sera a las {hora} con cuantos minutos? "))
    horaCita=datetime.time(hora,min, 0)
    miCita=cita(clienteCita, servicioCita, fecha, horaCita, False)
    print(f"su cita con {clienteCita.nombre}, para el servicio de {servicioCita.nombre } es para el dia {fecha} a la hora{horaCita} ")
    listaCitas.append(miCita)

def atenderCita():
    for i, cita in enumerate(listaCitas):
        print(f"{i}. cita de {cita.cliente.nombre} del dia {cita.fecha} a las {cita.hora}")
    index=int(input("que cita desa atender? "))
    micita=listaCitas[index]
    micita.Atender()
    listaCitas[index]=micita
    for i, emple in enumerate(ListaEmpleados):
        print(f"{i}. {emple.nombre}")
    indexEmple=int(input("escoge que empleado atendio la cita"))
    miempleado=ListaEmpleados[indexEmple]
    ResumenSer=ServiciosPrestados(micita.cliente,micita.servicio, miempleado)
    listaServiciosPrestado.append(ResumenSer)

while True:
    print("1.Registrar los servicios: ")
    print("2.Registrar citas: ")
    print("3.Consultar citas pendientes: ")
    print("4.Consultar citas atendidas : ")
    print("5.Agregar clientes : ")
    print("6.listar clientes : ")
    print("7.atender cita: ")
    print("8.administrar personal: ")
    print("9.Salir : ")
    accion=int(input("por favor ingresa que deseas hacer hoy: "))
    if accion==9:
        break
    elif accion==1:
        agregarServicios()
        print("servicio agregado")
    elif accion==2:
        agregarCita()
        print("cita agregada")
    elif accion==3:
        if len(listaCitas)==0:
            print("no hay citas ")
        else:
            for cita in listaCitas:
                if cita.atendida:
                    break
                else:
                    print(f"cliente: {cita.cliente.nombre} servicio: {cita.servicio.nombre} fecha: {cita.fecha}, hora: {cita.hora}")
    elif accion==4:
          if len(listaCitas)==0:
            print("no hay citas atendidas")
          else:  
            for cita in listaCitas:
                if cita.atendida:
                    print(f"cliente: {cita.cliente.nombre} servicio: {cita.servicio.nombre} fecha: {cita.fecha}, hora: {cita.hora}")
                else:
                    break
    elif accion==5:
        agregarCliente()
        print("Cliente agregado con exito")
    elif accion==6:
        for cliente in listaClientes:
            print(f"nombre:{cliente.nombre}, correo: , telefono: {cliente.telefono}, sexo: {cliente.sexo}")
    elif accion==7:
        atenderCita()
        print("cita atendida con exito")
    elif accion==8:
        print("Bienvenido que desdeas hacer")
        print("1.Agregar Especialidad")
        print("2.Agregar empleado")
        print("3.Ver atenciones")
        print("4.volver")
        accioAmin=int(input("Seleciona una opcion"))
        if accioAmin==1:
            agregarEspecialidad()
            print("Especialidad agregada")
        elif accioAmin==2:
            registrarEmpleado()
            print("empleado resgitrado")
        elif accioAmin==3:
            if len(listaServiciosPrestado) ==0 :
                print("no hay registros aun")
            else:
                for serP in listaServiciosPrestado:
                    print(f"{serP.cliente.nombre}, {serP.servicio.nombre}, {serP.empleado.nombre}")
        elif accioAmin==4:
            print("saliste")