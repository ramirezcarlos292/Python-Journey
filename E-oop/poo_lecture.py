class Personaje:
    nombre = "Default"
    fuerza = 0 
    inteligencia = 0
    defensa = 0
    vida = 0
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
        
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
    
    def get_fuerza(self):
        return self.fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.fuerza = fuerza
    
    
## Herencia
class Guerrero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) # no self needed, si la super clase cambia su nombre, no es necesario que aqui tambien cambie
        self.espada = espada
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de arma incorrecto")
            
    def atributos(self): # cambia el danio para la subclase hija
        super().atributos()
        print("Espada:", self.espada)
        
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self):
        super().atributos()
        print("Libro", self.libro)
        
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

# Poliformismo    
personaje_1 = Guerrero("Guts", 20, 4, 20, 100, 4)
personaje_2 = Mago("Vanesa", 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Accion de ", jugador_1.nombre, ":", sep = "")
        jugador_1.atacar(jugador_2)
        print(">>> Accion de ", jugador_2.nombre, ":", sep = "")
        jugador_2.atacar(jugador_1)
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")
    
combate(personaje_1, personaje_2)

# goku = Personaje("Goku", 20, 15, 10, 100)        
# guts = Guerrero("Guts", 20, 10, 10, 100, 5)
# vanesa = Mago("Vanessa", 20, 15, 10, 100, 5)
# goku.atributos()
# print(" ")
# guts.atributos()
# print(" ")
# vanesa.atributos()
# print(" ")
# goku.atacar(guts)
# guts.atacar(vanesa)
# vanesa.atacar(goku)
# goku.atributos()
# print(" ")
# guts.atributos()
# print(" ")
# vanesa.atributos()
# print(" ")
