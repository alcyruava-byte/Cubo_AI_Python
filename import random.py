import random

numero_secreto = random.randint(1, 99)
intento = 0

print("===================================")
print("     JUEGO: ADIVINA EL NÚMERO")
print("===================================")
print("Estoy pensando en un número entre 1 y 99.")
print("¡Intenta adivinarlo!")

while intento != numero_secreto:
    intento = int(input("\nEscribe tu número: "))

    if intento < numero_secreto:
        print("El número secreto es MAYOR.")
    elif intento > numero_secreto:
        print("El número secreto es MENOR.")
    else:
        print("\n🎉 ¡FELICIDADES! ¡ADIVINASTE EL NÚMERO!")
        print("El número secreto era:", numero_secreto)