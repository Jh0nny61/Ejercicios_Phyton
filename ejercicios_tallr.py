#Ejercicio 1 
print ("Hola mundo!")

#Ejercicio 2
nomb = input("Hola que tal!, Como te llamas? ")
print (f"Hola {nomb}, que tengas un buen día.")

#Ejercicio 3
a = int (input("Piensa en el primer num: "))
b = int (input("Piensa en el segundo num: "))

print (f"La suma de los numeros es: {a+b}")

#Ejercicio 4
a = int(input("Escribe la base del triangulo: "))
b = int(input("Escribe la altura del triangulo: "))
c = 0.5
print(f"el area del triangulo a calcular es: {c*a*b}")

#Ejercicio 5
cels = int(input("Escriba cuantos Grados C° deseas convertir: "))
fahr = (cels * 1.8) + 32
print(f"{cels}°C equivalen a {fahr}°F")

#Ejercicio 6
num = int(input("Escriba su numero: "))

if num % 2 == 0:
    print(f"Su numero {num} es PAR")
else:
    print(f"Su numero {num} es IMPAR")

#Ejercicio 7
num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba el segundo numero: "))
num3 = int(input("Escriba el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"El n# mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El n# mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El n# mayor es: {num3}")
else:
    print("Los tres numeros son iguales.")

#Ejercicio 8
num = int(input("Escriba el numero a elevar: "))
nuevo_num = num**2

print(f"El numero {num} elevado al cuadrado es: {nuevo_num}")

#Ejercicio 9
num = int(input("De cual numero quieres saber su tabla? "))
print (f"La tabla del {num} es:\n ")

for a in range(1, 16):
   print(f"{num} * {a} = {num * a}")

#Ejercicio 10
palabra = input("Escriba su palabra: ")

print(" Su palabra al reves es:", palabra[::-1])

#Ejercicio 11
edad = int(input("Cual es su edad? "))

if edad >= 18:
    print(f"Usted cuenta con {edad} años, eres MAYOR de edad")
else:
    print(f"Usted cuenta con {edad} años, eres MENOR de edad")

#Ejercicio 12

num = int(input("De que numero quieres su factorial? "))

fact = 1
for i in range(1, num + 1):
    fact *= i

print(f"El factorial de {num} es: {fact}")

#Ejercicio 13
n1 = float(input("Su primer numero: "))
n2 = float(input("Su segundo numero: "))
n3 = float(input("Su tercer numero: "))
n4 = float(input("Su cuarto numero: "))
n5 = float(input("Su quinto numero: "))

prom = (n1 + n2 + n3 + n4 + n5)/5

print (f"El promedio de sus 5 numeros es: {prom}")

#Ejercicio 14
num = int(input("Piense su numero: "))

print(f"Los numeros pares desde 1 hasta {num}:")

for i in range(1, num + 1):
    if i % 2 == 0:   
        print(i)

#Ejercicio 15
letra = input("Piensa en una letra: ").lower()  

if letra in "aeiou":
    print(f"La letra '{letra}' es una VOCAL")
else:
    print(f"La letra '{letra}' es una CONSONANTE")

#Ejercicio 16
a, b = 0, 1  
print("Estos son los 20 primeros numeros de la serie Fibonacci:")

for i in range(20):
    print(a)
    a, b = b, a + b   

#Ejercicio 17
num = int(input("piensa en un numero: "))
primo = True
if num <= 1:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
print(f"El numero:" , num , "si es primo" if primo else "no es primo")

#Ejercicio 18
lista = list(range(1, 101))
for a in lista:
    if a % 5 == 0:
        print(a)

#Ejercicio 19
p = input("Escribe cualquier palabra: ").lower()
vocal = "aeiou"
cont = 0
for letra in p:
    if letra in vocal:
        cont += 1
print("la cantidad de vocales en la palabra", p , "es de:", cont)

#Ejercicio 20
a = float(input("Dime el primer numero: "))
b = float(input("Dime el segundo numero: "))
op = input("Que operacion quieres realizar? +, -, *, / : ")
if op == "+":
    print("El resultado de la suma es:", a + b)
elif op == "-":
    print("El resultado de la resta es:", a - b)
elif op == "*":
    print("El resultado de la multiplicacion es:", a * b)
elif op == "/":
    if b != 0:
        print("El resultado al hacer la division es:", a / b)
    else:
        print("Disculpa, no es posible dividir entre 0")
else:
    print("la operación no es valida")

#Ejercicio 21
num = [1, 10, 8, 16, 12, 4, 7, 11, 6, 9]
may = num[0]
for n in num:
    if n > may:
        may = n
print("El numero mayor de la lista", num , "es:", may)

#Ejercicio 22
lista = [7, 4, 8, 3, 5, 11, 2, 10]
lista.sort()
print("el orden de la lista anterior:", lista)

#Ejercicio 23
lista = [2, 2, 8, 1, 3, 4, 4, 5, 7, 7, 9]
no_dupl = []
for n in lista:
    if n not in no_dupl:
        no_dupl.append(n)
print("la lista sin n# duplicados quedaría:", no_dupl)

#Ejercicio 24
nombres = ["Elizabeth", "Isaac", "Sebastian", "Luna", "Alberto", "Omar", "Uriel"]
nombres.sort()

print("La lista de nmbrs ordenados sería: ", nombres)

#Ejercicio 25
lista = [4, 5, 7, 11, 6]
suma = 0
for a in lista:
    suma += a
print("La suma en la lista es:", suma)

#Ejercicio 26
lista1 = [2 , 3 , 4 , 6 , 8]
lista2 = [16 , 32 , 40 , 48 , 54]

nueva_list = lista1 + lista2

print("Uniendo las dos listas anteriores:", nueva_list)

#Ejercicio 27
frase = input("Escriba cualquier frase: ")
palabras = frase.split()
print("la frase:", frase , "cuenta con", len(palabras) , "palabras:")

#Ejercicio 28
pal = input("Escriba cualquier palabra: ").lower()
if pal == pal[::-1]:
    print("La palabra", pal ,"SI es palíndromo")
else:
    print("La palabra", pal ,"NO es palíndromo")

#Ejercicio 29
cuad = []
for i in range(1, 11):
    cuad.append(i * i)
print("la lista de cuadrados es:", cuad)

#Ejercicio 30
lista = [20, 15, 8, 36, 14, 21]
lista.sort()
print("EL segundo num mas grande es:", lista[-2])