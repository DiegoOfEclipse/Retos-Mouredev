import re
from string import Template

texto = "Tomate"

print(texto[0],texto[1], texto[2], texto[3])
print(texto[2], texto[3], texto[4], texto[5])

subcadena_unida = "Running Sky"

sub0 = subcadena_unida[0:7]
sub1 = subcadena_unida[8::]
sub2 = subcadena_unida[::2]
print(sub0, sub1, sub2)

nombre = "Don Felipe"

longitud = len(nombre)
print(longitud)

textos_anteriores = texto + " Haciendo " + subcadena_unida + " Junto a " + nombre
print(textos_anteriores)
f_textos_anteriores = f"{texto} Haciendo {subcadena_unida} Junto a {nombre}"
print(f_textos_anteriores)

dicho_popular = ["Nadie", "es", "profeta", "en", "su", "tierra"]
print(" ".join(dicho_popular))

si = ["y", "si"]
no = ["n", "no"]

def seleccionar_nombre():
    while True:
            nombre = input("Tu Nombre: ")
            caracteres = len(nombre)
            if caracteres == 0:
                print("Nombre no Introducido, Intentelo de Nuevo")
            else:
                confirmacion = input(f"Estas Seguro que Este es Tu Nombre? ")
                confirmacion_lowkey = confirmacion.lower()
                if confirmacion_lowkey not in (si + no):
                    print("Confirmacion No Valida!")
                elif confirmacion_lowkey in no:
                    print("Vale, Cual es tu Nombre?")
                elif confirmacion_lowkey in si: 
                    print("Nombre Seleccionado!")
                    print("Hola entonces {}, ".format(nombre) * 3)
                    break
seleccionar_nombre()

comida_fav = "Macarrones con queso"
for caracter in comida_fav:
     print(caracter)

for indice, letra in enumerate (comida_fav):
     print(f"Indice {indice}: {letra}")

comida_minuscula = comida_fav.lower()
comida_mayuscula = comida_fav.upper()
comida_titular = comida_fav.title()
comida_swap = comida_fav.swapcase()

print(f"{comida_mayuscula}, {comida_minuscula}, {comida_titular}, {comida_swap}")

nueva_comida_fav = comida_fav.replace("Macarrones", "Arroz").replace("queso", "garbanzos")
print(nueva_comida_fav)
pink = "She0is1a2mew3mew4girl5who6is7ready8to9play"
pink_espaciada = re.sub(r"\d", " ", pink)
print(pink_espaciada)
cancion_rancia = "Six Foot Seven the Tung Tung Man"
cancion_arreglada = cancion_rancia[:9] + "NO" + cancion_rancia[14:]
print(cancion_arreglada)

pink_x = re.sub(r"[0-9]", "X", pink)
pink_split = pink_x.split("X")
print(pink_split)

t = Template("En Todo el Mundo, Existen alrededor de $cantidad $animal, ya que Estan en Peligro de Extincion")
print(t.substitute(cantidad = 3200, animal = "Tigre"))

print(texto.isalpha())
print(pink.isalnum())

def comprobador(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    palabra1_i = palabra1[::-1]
    palabra_v = len(set(palabra1 + palabra2))
    palabra_u = len(palabra1 + palabra2)
    if palabra1_i == palabra2:
         print(f"Las Palabras {palabra1} y {palabra2} son Palindromos")
    elif sorted(palabra1) == sorted(palabra2):
         print(f"Las Palabras {palabra1} y {palabra2} son Anagramas")
    elif palabra_u == palabra_v:
         print(f"Las Palabras {palabra1} y {palabra2} son Isodramas")
    else:
         print("No se a Detectado Ninguna Coincidencia")
comprobador("Paris", "Prisa")
