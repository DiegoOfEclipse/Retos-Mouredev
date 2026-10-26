print(10 + 20, 20 - 10, 5 * 10, 40 / 10, 40 // 10, 10 % 5, 5 ** 10)

x = 10
print(x)
x += 10
print(x)
x -= 10
print(x)
x *= 10
print(x)
x /= 10
print(x)
x // 10
print(x)
x % 10
print(x)
x ** 10
print(x)

print(10 == 10, 10 != 20, 20 > 10, 10 < 20, 20 >= 10, 10 <= 20)

print(20 > 10 and 30 > 20, 30 > 20 or 50 < 40, not(20 > 30 and 50 > 40))

hamburguesa = "Pan"
pizza = "Peperoni"
print("Peperoni" in pizza)
print("Peperoni" not in hamburguesa)

cubo_1 = 10
cubo_2 = 20

if cubo_1 >= cubo_2:
    print("Parece Que el Cubo 1 Es Mas Grande!")
elif cubo_1 == cubo_2:
    print("Son Igual de Grandes!")
else:
    print("Parece Que el Cubo 2 Es Mas Grande!")

animales = ["Gato", "Conejo", "Tortuga", "Perro"]

for especies in animales:
    if especies == "Gato":
        print("Mira Un " + especies + " !")
    elif especies == "Conejo":
        print("Mira Un " + especies + " !")
    elif especies == "Tortuga":
        print("Mira Una " + especies + " !")
    elif especies == "Perro":
        print("Mira Un " + especies + " !")

for numero in range(10, 56):
    if numero == 16:
        continue
    elif numero % 2 == 0:
        print("El Numero " + str(numero) + " Es Par!")
    elif numero % 3 == 0:
        continue

import time 

caminar = True
hambre = 0


while True:
    if caminar:
        print("Estoy Caminando")
        hambre += 1
        if hambre >= 30:
            caminar = False
            print("¡Tengo mucha Hambre! Me detengo a comer.")
    
    else:
        print("Estoy Comiendo")
        hambre -= 1
        if hambre == 0:
            caminar = True
            print("¡Ya estoy lleno! A caminar de nuevo.")
    
    time.sleep(0.1)
