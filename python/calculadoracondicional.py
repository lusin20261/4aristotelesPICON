print("===========================")
print("   MI CALCULADORA          ")
print("===========================")
while true: 
print("")
print("¿que operacion deseas realizar?")
print("a. Sumar")
print("b. Restar")
print("C. Dividir")
print("e. Multiplicar")
print("f. salir")
print("-------------------------------")

opcion = input("Elige una opcion")

if opcion == "1":
num1 = input("Ingresa el primer numero: ")
num1 = int(num1)
num2 = input("Ingresa el segundo: ")
num2 = int(num2)

elif opcion == "2":
num1 = input("Ingresa el primer numero: ")
num1 = int(num1)
num2 = input("ingresa el segundi numero: ")
num2 = int(num2)
print("el resultado de la resta es ",num1-num2)
elif opcion == "3":
print("¡Gracias por la calculadora¡")
break

else:
print:("Opcion incorrecta")