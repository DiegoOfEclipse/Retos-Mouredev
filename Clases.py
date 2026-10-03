import time
import random

minerales_esenciales = {"Potasio" : 100, "Zinc" : 50, "Hierro" : 25, "Calcio" : 10, "Nada" : 0}

class Minero:
    def __init__(self, nombre_minero):
        self.nombre = nombre_minero
        self.minerales = 0
        self.energia = 100

    def minero_accion(self):    
            while True:
                if self.energia > 0:
                    self.minerales = self.minerales + 1
                    print(f"{self.nombre} Encontro {self.minerales} Minerales!")
                    time.sleep(0.1)
                    self.energia = self.energia - 1
                else:
                    print(f"{self.nombre} Se Quedo Agotado!")
                    time.sleep(1)
                    print(f"{self.nombre} Consiguio {self.minerales} Minerales!...")
                    time.sleep(1)
                    print("Un Momento...")
                    clave, valor = random.choice(list(minerales_esenciales.items()))
                    if valor == 0:
                        time.sleep(2)
                        print(f"Ah, No Nada... Por un Momento {self.nombre} Creyo Ver Algo Raro En los Minerales")
                        time.sleep(1)
                        print("Pero No le dio Importancia.")
                        break
                    else:
                        time.sleep(2)
                        print(f"{self.nombre} Vio {clave} Entre los Minerales y Se lo Trago de un Bocado!")
                        time.sleep(2)
                        print(f"Ahora {self.nombre} Tiene {valor} mas de Energia")
                        time.sleep(1)
                        self.energia = valor
                        print(f"{self.nombre} Aumento su Energia a {valor}!")
mi_personaje = Minero("Lancer")
mi_personaje.minero_accion()