# Ejemplo de uso de listas

Misnovios = ["Jose","David","Roberto"]
MisNumeros = [34,44,355]
# Mostrando mis novios
print(Misnovios)
# Mostrando mis numeros
print(MisNumeros)
print("---accediendo a los elementos de la lista---")
print(Misnovios[-2])
if "Dan" in Misnovios:
    print("Si, 'Dan' esta en la lista de mis novias")
else:
    print("Chale no eres mi novio. :(")
print("Numero de novios")
Nnovios = len(Misnovios)
print(f"Numero de novios =  {Nnovios}")
print("Ciclo for en listas")
posicion=0
for medianaranja in Misnovios:
    print(posicion," ",medianaranja)
    posicion=posicion+1 