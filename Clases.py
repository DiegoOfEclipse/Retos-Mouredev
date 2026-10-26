import time
import random

tu_nombre = input("¿Cuál es el Nombre del Minero? ")
minerales_esenciales = {"Potasio": 100, "Zinc": 50, "Hierro": 25, "Calcio": 10, "Nada": 0}

class Minero:
    def __init__(self, nombre_minero):
        self.nombre = nombre_minero
        self.minerales = 0
        self.energia = 100
        self.descansos = 0
        self.contatienda = 0
        self.musgo = 0
        self.moneda = [0, 1]
        self.pico = 1
        self.carro_de_mina = 3
        self.casco_con_bombillita = 0.1
        self.Diamantes = 0
        self.salir = 0
        self.c1_s = None
        self.v1_s = None
        self.c2_s = None
        self.v2_s = None
        self.compra_y_vete_cacahuete = {
            "Pico_Picadura": False,
            "Carro_De_Mina": False,
            "Casco_Con_Bombillita": False,
            "Lamina_De_Hierro": False,
            "Fosforo": False
        }

    def Musgo(self):
        print("¡El Musgo fue Consumido con Gusto!")
        self.musgo = self.musgo + 1
        time.sleep(4)
        if self.musgo == 5:
            print("¡Eres un Gran Catador de Musgos! Consumiste 5 Musgos")
            time.sleep(4)

    def Pico_Picadura(self):
        print("¡Conseguiste el Pico Picadura!")
        self.pico = self.pico + 1
        self.compra_y_vete_cacahuete["Pico_Picadura"] = True

    def Fosforo(self):
        print("¡Fósforo se añadió a tus probabilidades!")
        minerales_esenciales.update({"Fósforo": 200})
        self.compra_y_vete_cacahuete["Fosforo"] = True

    def Moneda(self):
        print("¡Se tiró la moneda!")
        time.sleep(2)
        print("...")
        time.sleep(5)
        resultado = random.choice(self.moneda)
        if resultado == 0:
            self.minerales = self.minerales * 2
            print("¡La suerte está de tu lado! Conseguiste duplicar los minerales")
        else:
            self.minerales = 0
            print("La suerte te da la espalda... Te quedaste sin nada.")

    def Carro_De_Mina(self):
        print("¡Ahora tienes un carro de mina!")
        self.carro_de_mina = 1
        self.compra_y_vete_cacahuete["Carro_De_Mina"] = True

    def Cama(self):
        print("Descansaste un poco...")
        time.sleep(10)
        self.energia = self.energia + 500
        print("¡Ahora tienes 500 de energía!")

    def Pocion_Alocada(self):
        print("¡La poción se bebió con degustación!")
        time.sleep(2)
        minerales_esenciales["Potasio"] = random.randint(1, 200)
        print("Ahora el potasio dará la energía incorrecta")

    def Casco_Con_Bombillita(self):
        print("¡Has obtenido el casco con bombillita!")
        time.sleep(2)
        self.casco_con_bombillita = 0.05
        print("¡Ahora irás más rápido al picar!")
        self.compra_y_vete_cacahuete["Casco_Con_Bombillita"] = True

    def Lamina_De_Hierro(self):
        print("¡Untaste a tu pico la lámina de hierro!")
        time.sleep(2)
        print("Ahora es capaz de encontrar y picar DIAMANTES")
        minerales_esenciales.update({"Diamante": 1})
        self.compra_y_vete_cacahuete["Lamina_De_Hierro"] = True
        
    def tienda(self):
        self.contatienda = self.contatienda + 1
        print(("-" * 10) + "TIENDA" + ("-" * 10))
        self.objetos = {
            "Musgo: Sabe Musgoso": 1, 
            "Pico_Picadura: Su Picadura hace que Pique (Y Escueza) El Doble!": self.minerales * 3, 
            "Fosforo: Añade la Probabilidad de Encontrar Fosforo Entre los Minerales": self.minerales, 
            "Moneda: La Moneda de la Avaricia, Duplica o Pierde Todo": (self.minerales // 2), 
            "Carro_De_Mina: Se Necesitarán 3 Descansos en Lugar de 5 Para Llegar a La Tienda": self.minerales + (self.minerales // 2), 
            "Cama: Una Simple Cama Que te Da 500 Energia": (self.minerales * 2.5), 
            "Pocion_Alocada: Una Poción Que Cambia Al Azar La Cantidad de Energía (De 1 a 200) del Potasio": self.minerales // 1.5, 
            "Casco_Con_Bombillita: Este Casco Posee una Bombilla Para Iluminar el Camino, Haciendo que Picar sea Más Rápido": self.minerales // 3, 
            "Lamina_De_Hierro: Se le Añade una Lámina de Hierro alrededor de tu Pico, Con Ella, Puedes Encontrar y Picar Diamantes!": self.minerales * 2.5
        }
        
        for nombre, comprado in self.compra_y_vete_cacahuete.items():
            if comprado:
                for objeto in list(self.objetos.keys()):
                    objeto_iden = objeto.split(":")[0]
                    if objeto_iden == nombre:
                        del self.objetos[objeto]

        time.sleep(4)
        if self.contatienda > 1:
            print("¡Bienvenido de vuelta, muchachín!")
            time.sleep(1)
        else:
            (clave1, valor1), (clave2, valor2) = random.sample(list(self.objetos.items()), 2)
            print("¡Pero mira a quién tenemos por aquí! Saludos, viajero. Soy Seam, el vendedor de estas tierras! Desterrado a las minas por mis increíbles precios, en el buen y mal sentido. Ja, ja, ja")
            time.sleep(8)
        if self.salir == 1:
            self.salir = 0
            (clave1, valor1), (clave2, valor2) = (self.c1_s, self.v1_s), (self.c2_s, self.v2_s)
        print("")
        print(f"{clave1} y Cuesta {valor1} Minerales")
        print(f"{clave2} y Cuesta {valor2} Minerales")
        print("Salir: Pirarme de Esta Tienda (Porque Estoy en Números Rojos, o Porque solo Hay Chatarra)")
        print("")
        comprar1 = clave1.split(":")[0]
        comprar2 = clave2.split(":")[0]
        while True:
            respuesta = input("Dime, ¿te interesan algunas de mis baratijas? ")
            if respuesta == comprar1 and self.minerales >= valor1:
                time.sleep(1)
                print("¡Dicho y hecho!")
                self.minerales = self.minerales - valor1 
                getattr(mi_personaje, comprar1)()
                (clave1, valor1), (clave2, valor2) = random.sample(list(self.objetos.items()), 2)
                break
            elif respuesta == comprar2 and self.minerales >= valor2:
                time.sleep(1)
                print("¡Dicho y hecho!")
                self.minerales = self.minerales - valor2
                getattr(mi_personaje, comprar2)()
                (clave1, valor1), (clave2, valor2) = random.sample(list(self.objetos.items()), 2)
                break
            elif respuesta.lower() == "salir":
                time.sleep(1)
                print("Nos veremos otra vez... o no. Ja, ja, ja")
                time.sleep(2)
                (self.c1_s, self.v1_s), (self.c2_s, self.v2_s) = (clave1, valor1), (clave2, valor2)
                self.salir = self.salir + 1
                break
            else:
                time.sleep(1)
                print("Al parecer no tienes minerales... O has escrito mal el nombre. La segunda opción es mejor, para mi gusto ")
    
    def minar(self):
        while True:
            if self.descansos == self.carro_de_mina:
                self.descansos = 0
                mi_personaje.tienda()
            elif self.energia > 0:
                self.minerales = self.minerales + self.pico
                print(f"{self.nombre} encontró {self.minerales} Minerales!")
                time.sleep(self.casco_con_bombillita)
                self.energia = self.energia - 1
            else:
                print(f"{self.nombre} se quedó agotado!")
                time.sleep(1)
                print(f"{self.nombre} consiguió {self.minerales} Minerales!...")
                time.sleep(1)
                print("Un momento...")
                clave, valor = random.choice(list(minerales_esenciales.items()))
                if clave == "Diamante":
                    time.sleep(2)
                    print(f"{self.nombre} vio un diamante entre los minerales!")
                    time.sleep(1)
                    self.minerales = int((self.minerales // 2) * 2.5)
                    print(f"Vendes el diamante en la tienda por {self.minerales}")
                    time.sleep(5)
                    self.energia = self.energia + 100
                    print("¡Al ver la cantidad que has ganado, te da un subidón de energía!")
                elif valor == 0:
                    time.sleep(2)
                    print(f"Ah, no... nada. Por un momento {self.nombre} creyó ver algo raro en los minerales")
                    time.sleep(1)
                    print("Pero no le dio importancia.")
                    break
                else:
                    time.sleep(2)
                    print(f"{self.nombre} vio {clave} entre los minerales y se lo tragó de un bocado!")
                    time.sleep(2)
                    print(f"Ahora {self.nombre} tiene {valor} más de energía")
                    time.sleep(1)
                    self.energia = valor
                    print(f"{self.nombre} aumentó su energía a {valor}!")
                    self.descansos = self.descansos + 1 

mi_personaje = Minero(tu_nombre)
mi_personaje.minar()
