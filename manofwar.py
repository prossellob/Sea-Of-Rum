import random,sys,time,os
global main
class barco:
    def __init__(self,nivel,nombre,capitan,armas,tripulacion,dinero):
        self.nivel = nivel
        self.nombre = nombre
        self.capitan = capitan
        self.armas = armas
        self.tripulacion = tripulacion
        self.punteria = 50
        self.dinero = dinero
        self.tripulantes = {'oficiales':0,'artilleros':0,'carpinteros':0}
        self.revision_nivel()

    def revision_nivel(self):
        if self.nivel == 5:
            self.vida += 150
            self.maxtripulacion += 400
            self.maxarmas += 50
        elif self.nivel == 4:
            self.vida += 75
            self.maxtripulacion += 250
            self.maxarmas += 32
        elif self.nivel == 3:
            self.vida += 40
            self.maxtripulacion += 100
            self.maxarmas += 12
        elif self.nivel == 2:
            self.vida += 20
            self.maxtripulacion += 30
            self.maxarmas += 4
        elif self.nivel == 1:
            self.vida = 15
            self.maxtripulacion = 20
            self.maxarmas = 2


    def revision_compra_tripulantes(self,objeto,cantidad):
        if objeto == 'oficiales':
            self.maxtripulacion += cantidad * 5
        elif objeto == 'artilleros':
            self.punteria += cantidad * 5
        elif objeto == 'carpinteros':
            self.vida += cantidad * 10


    def info(self):
        print(self.armas)
        print(self.tripulacion)
        print(self.maxtripulacion)
        print(self.vida)
        print(self.dinero)
        print(self.punteria)

    def ataque(self,other):
        print(self.nombre + ' ataca a ' + other.nombre + ' con ' + str(self.armas) + ' cañones')
        i,impactos = 0,0
        while i <= self.armas:
            rnd = random.randint(0,100)
            if rnd <= self.punteria:
                impactos += 1
                i += 1
            else:
                i += 1
        print(self.nombre + ' ha acertado ' + str(impactos) + ' disparos de cañon.')
        other.vida -= impactos
        print(other.vida)

    def comprar_armas(self,cantidad,precio):
        if (self.armas + cantidad) <= self.maxarmas:
            self.armas += cantidad
            self.dinero -= precio
            tienda()
        else:
            delay_print('No puedes comprar más cañones.')
            tienda()
    def comprar_marineros(self,cantidad,precio):
        if (self.tripulacion + cantidad) <= self.maxtripulacion:
            self.tripulacion += cantidad
            self.dinero -= precio
            tienda()
        else:
            delay_print('No puedes tener más tripulantes.')
            tienda()
    def comprar_especiales(self,objeto,cantidad,precio):
        if (self.tripulacion + cantidad) <= self.maxtripulacion:
            if (self.tripulantes[objeto] + cantidad) <= self.nivel:
                self.tripulacion += cantidad
                self.tripulantes[objeto] += cantidad
                self.dinero -= precio
                self.revision_tripulantes(objeto,cantidad)
                tienda()
            else:
                delay_print('No puedes tener más tripulantes.')
                tienda()
        else:
            delay_print('No puedes tener más tripulantes.')
            tienda()

def delay_print(s): #Función para imprimir palabra por palabra.
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.04)

def crearbarco(): #Función de creación del barco.
    global main
    i,x = 150,0
    delay_print('Ingresa el nombre del barco: \n')
    nombre = input('>')
    delay_print('Ingrese el nombre del capitán: \n')
    capitan = input('>')
    delay_print('Lanzando el dado del dinero.\n')
    while x <= 9: #Bucle a modo de dado.
        while i <= 300:
            print(i,end = '\r') #Para sobrescribir la línea.
            time.sleep(0.002)
            i += 1
        x,i = x+1,150
    dinero = random.randint(150,300)
    delay_print('Has ganado: '+ str(dinero) + ' piezas de oro.\n')
    time.sleep(0.5)
    delay_print('Tu barco se esta construyendo en el astillero...\n')
    main = barco(1,nombre,capitan,0,0,dinero)

def tienda():
    precios = {'1':5,'2':25,'3':25,'4':75,'5':75}
    global main
    os.system('clear')
    print('--------TIENDA--------')
    delay_print('Tienes ' + str(main.dinero) + ' piezas de oro.\n')
    print('LISTADO DE PRECIOS:')
    print('1)Marineros --> 5 PO.')
    print('2)Cañon --> 25 PO.')
    print('3)Oficiales --> 25 PO.')
    print('4)Artilleros --> 75 PO.')
    print('5)Carpinteros --> 75 PO.')
    print('Introduce 0 para salir.')
    print('Ingrese el número del producto que quieres comprar: ')
    compra = str(int(input('>')))
    if compra in ['1','2','3','4','5']:
        delay_print('Ingresa la cantidad:\n')
        cantidad = int(input('>'))
        precio = precios[compra] * cantidad
        if precio > main.dinero:
            delay_print('No tienes dinero, no te intentes pasar de listo...')
            tienda()
        else:
            if compra == '1':
                main.comprar_marineros(cantidad,precio)
            elif compra == '2':
                main.comprar_armas(cantidad,precio)
            elif compra == '3':
                main.comprar_especiales('oficiales',cantidad,precio)
            elif compra == '4':
                main.comprar_especiales('artilleros',cantidad,precio)
            elif compra == '5':
                main.comprar_especiales('carpinteros',cantidad,precio)
    elif compra == '0':
        return
    else:
        tienda()



# crearbarco()
main = barco(1,'North','Drake',0,0,50000)
print(main.tripulantes)
tienda()
main.info()
print(main.tripulacion)
print(main.tripulantes)
# main.info()
