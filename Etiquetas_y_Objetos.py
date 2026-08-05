def inmutable_ejemplo():
    a = 10
    b = a
    a = 20
    print(b)
inmutable_ejemplo()

def mutable_ejemplo():
    lista = [1, 2, 3]
    lista2 = lista
    lista.append(4)
    print(lista2)
mutable_ejemplo

h_eclipse_i = "17:34"
h_eclipse_f = "21:58"

def inmutable(h_eclipse_i, h_eclipse_f):
    h_eclipse_i, h_eclipse_f = h_eclipse_f, h_eclipse_i
    return h_eclipse_i, h_eclipse_f

eclipse_i_2, eclipse_f_2 = inmutable(h_eclipse_i, h_eclipse_f)

print(h_eclipse_i, h_eclipse_f, eclipse_i_2, eclipse_f_2)

comida = ["abichuelas", "macarrones", "arroz"]
zoologico = ["zorro", "girafa", "elefante"]

def mutable(comida, zoologico):
    comida, zoologico = zoologico, comida
    return comida, zoologico

comida2, zoologico2 = mutable(comida, zoologico)

print(comida, zoologico, comida2, zoologico2)