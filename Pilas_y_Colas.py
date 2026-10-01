from collections import deque

cola_supermercado = deque()


poner_s = "Personas"
no_poner_s = "Persona"
poner_hyn = "han"
no_poner_hyn = "ha"
confirmacion1 = ["y", "Y"]
confirmacion2 = ["x", "X"]

def detectar_s():
    if len(cola_supermercado) == 1:
        return no_poner_s
    else:
        return poner_s

def detectar_hyn():
    if len(cola_supermercado) <= 1:
        return no_poner_hyn
    else:
        return poner_hyn
    
def detectar_general():
    detectar_s()
    detectar_hyn()

def salida_persona():
    while True:
        if len(cola_supermercado) > 0:
            salida_cola = cola_supermercado.popleft()
            print(f"{salida_cola} ha Salido de la Cola")
            detectar_general()
            decision_final_s = detectar_s()
            print(f"Queda en el Supermercado {len(cola_supermercado)} {decision_final_s}")
            salida_persona()
        else:
            break

def añadir_persona():
    while True:
        respuesta = input("Presiona Y Para Añadir a Alguien | Presiona X para Procesarlo ")
        if respuesta in confirmacion1:
            persona = input(("A quien Quieres Añadir? "))
            cola_supermercado.append(persona)
            detectar_general()
            decision_final_s = detectar_s()
            decision_final_hyn = detectar_hyn()
            print(f"Se {decision_final_hyn} puesto {len(cola_supermercado)} {decision_final_s} en la Cola")
        elif respuesta in confirmacion2 and len(cola_supermercado) > 0:
            salida_persona()
        elif respuesta in confirmacion2:
            print("No has Añadido a Nadie Aun!")
        else:
            print("bash: x: command not found")
            break

pila = []

def procesar_objeto():
    while True:
        if len(pila) > 0:
            procesado = pila.pop()
            print(f"Se a Procesado {procesado}")
            procesar_objeto()
        else:
            break

def añadir_objeto():
    while True:
        respuesta = input("Presiona Y Para Añadir un Objeto | Presiona X para Procesarlo ")
        if respuesta in confirmacion1:
            objeto = input("Que Objeto Quieres Añadir? ")
            pila.append(objeto)
            print(f"Se ha puesto {objeto} en la Lista")
        elif respuesta in confirmacion2:
            procesar_objeto()
        elif respuesta in confirmacion2:
            print("No has Añadido a Nadie Aun!")
        else:
            print("bash: x: command not found")
            break

def eleccion_pilas_colas():
    while True:
        respuesta = input("Que Deseas Utilizar? Pilas o Colas? ")
        if respuesta == "Colas":
            añadir_persona()
        elif respuesta == "Pilas":
            añadir_objeto()
eleccion_pilas_colas()