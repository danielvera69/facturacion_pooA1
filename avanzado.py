# Crear una lista de 10 números
#          0  1  2 
import time

from product import Product
prod1 = Product()
prod2 = Product()
prod3 = Product()

# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# productos = [prod1, prod2, prod3]
# productos[0].preci=2000
# productos[-1].preci=1000
# numeros[0]=2
# numeros.append(20)
# numeros[-1]=30
# # Presentar solo los números pares utilizando un bucle for
# inicio=time.time()
# print(f"Inicio Recorrido: {inicio}")
# for numero in range(10000):
#     if numero % 2 == 0:
#         print(numero)
# print(f"Fin Recorrido: {time.time()-inicio}")
# print("Recorrido con bucle for con enumerate:")
# for indice,numero in enumerate(numeros):
#     if numero % 2 == 0:
#         print(indice,numero," Es par")
        
# # Ejemplo de recorrido de un diccionario mostrando clave y valor:

# diccionario = {"a": 1, "b": 2, "c": 3}
# for clave, valor in diccionario.items(): #values, keys()
#     print(f"Clave: {clave}, Valor: {valor}")

# Ejemplo:
# lista1=[5,10]
# lista2=[20,30]
# lista3 = lista1+lista2 # [5,10,20,30]

# lista = [1, 2, 3, 4,5,3,1,2,1,2, 5]  # Ejemplo de lista
# conjunto = {1, 2, 3, 4, 5}  # Ejemplo de conjunto
# conjunto2 = set(lista)
# conjunto2.add(100)
# print(conjunto2)
# La principal diferencia entre las listas/tuplas y los conjuntos 
# es que los conjuntos no permiten elementos duplicados, mientras 
# que las listas y las tuplas sí. Esto significa que los conjuntos
# son útiles cuando se necesita almacenar una colección de elementos
# únicos y no se necesita un orden específico, mientras que las 
# listas y las tuplas son más adecuadas cuando se necesita mantener
# un orden específico y se permiten elementos duplicados.
# print(lista)
# print(tupla)
# print(conjunto)


# Ejemplo 4: Verificar si un número es par utilizando una lista
# def es_par_lista(numero):
#     lista = [2, 4, 6, 8, 10]
#     # for num in lista:
#     #     if numero==num:
#     #         return True
#     # return False
#     if numero in lista:
#         return True
#     else:
#         return False

# # Ejemplo 5: Verificar si un número es par utilizando una tupla
# def es_par_tupla(numero):
#     tupla = (2, 4, 6, 8, 10)
#     if numero in tupla:
#         return True
#     else:
#         return False

# # Ejemplo 6: Verificar si un número es par utilizando un conjunto
# def es_par_conjunto(numero):
#     conjunto = {2, 4, 6, 8, 10}
#     if numero in conjunto:
#         return True
#     else:
#         return False

# numero = 6
# print(f"¿El número {numero} es par?")
# print(f"Usando una lista: {es_par_lista(numero)}")
# print(f"Usando una tupla: {es_par_tupla(5)}")
# print(f"Usando un conjunto: {es_par_conjunto(numero)}")

# Tipos de funciones en Python:
# 1. Funciones anónimas (lambda)
# 2. Funciones dentro de otras funciones
# 3. Funciones como parámetros

# Ejemplo de función anónima (lambda):
# def sumar(x,y): 
#     return x+y
# print(sumar(2,4))
# Lambda es una función anónima en Python que se define sin un nombre.
# Se utiliza cuando se necesita una función rápida y simple sin definir
# una función completa.
# Un ejemplo de uso de lambda en Python es para ordenar una lista 
# de acuerdo a un criterio específico.

# suma = lambda x, y: x + y
#print(suma(2,5))# 7
# print((lambda x, y: x + y)(2,5))
# es_par = lambda x: x % 2 == 0
# if es_par(5):
#     print("Par")
# else:    
#     print("Impar")
    

#Ejemplo de función dentro de otra función:
# def funcion_padre():
#     print("dentro de la funcion padre")
#     def funcion_hija():
#         print("Soy una función dentro de otra función")
#     funcion_hija()
#     print("fin funcion padre")
# funcion_padre()

# # Ejemplo de función como parámetro:
# def funcion_principal(expo,v1,v2,z):
#     print("Ejecutando función principal")
#     print(expo(v1,v2)+z)

# exponente = lambda x,y: x**y
# def sumar(x,y): 
#     return x+y

# funcion_principal(sumar,5,3,10)

# # funciones de orden superior
# # Ejemplo 1: Elevar al cuadrado todos los elementos de una lista
# exponente = lambda x: x**x
# numeros = [1, 2, 3, 4, 5]
# # def multi(valor):
# #    return valor*2
# # cuadrados = list(map(multi, numeros))#[1,4,9,16,25]
# # cuadrados = list(map(lambda x: x ** 2, numeros))#[1,4,9,16,25]
# cuadrados = list(map(exponente, numeros))#[1,4,9,16,25]
# print(cuadrados)
# from functools import reduce

# # Generar una lista con la serie Fibonacci de n términos
# fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])
# print(fibonacci(7))  # Salida: [0, 1, 1, 2, 3, 5, 8]
# def expo(x):
#      return x**2

# def mapNuestro(funcion,numeros):
#     datosmap=[]
#     for x in numeros:
#         res = funcion(x)
#         datosmap.append(res)
#     return datosmap
# print(mapNuestro(expo,[1,2,3]))
# print(list(map(lambda x: x ** 2,numeros)))
          
# # print(cuadrados,datosmap)  # Output: [1, 4, 9, 16, 25]

# # Ejemplo 2: Convertir cadenas a mayúsculas
# palabras = ['hola', 'mundo', 'python']
# mayusculas = map(str.upper, palabras)

# print(list(mayusculas))  # Output: ['HOLA', 'MUNDO', 'PYTHON']

# # Ejemplo 1: Filtrar números impares de una lista
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# impares = filter(lambda x: x % 2 != 0, numeros)
# print(list(impares))  # Output: [1, 3, 5, 7, 9]

# Ejemplo 2: Filtrar palabras que comienzan con 'a'
# palabras = ['apple', 'banana', 'avocado', 'orange']
# comienza_con_a = filter(lambda palabra: palabra.startswith('a'), palabras)
# print(list(comienza_con_a))  # Output: ['apple', 'avocado']
# from functools import reduce

# # # Ejemplo 1: Sumar todos los elementos de una lista
# numeros = [1, 2, 3, 4, 5]
# suma = reduce(lambda x, y: x * y, numeros,1)#15
# print(suma)  # Output: 15

# # Ejemplo 2: Calcular el producto de todos los elementos de una lista
# numeros = [2, 3, 4]
# producto = reduce(lambda x, y: x * y, numeros,5)
# print(producto)  # Output: 24

from functools import reduce

# # Generar una lista con la serie Fibonacci de n términos
#                            #      [0,1]  [0,1] + [1+0=1]=[0,1,1]
#                            #     [0,1,1] [0,1,1] + [2] = [0,1,1,2]
#                            #    [0,1,1,2][0,1,1,2] 
# fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])
# print(fibonacci(7)) 
# funcion_principal(exponente,5,3)
class OrdenSuperior:
    def calculo(self, limite):
        serie = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])
        print(serie(limite)) 
red = OrdenSuperior()
red.calculo(5)

# Ejecutar ejemplos:

# funcion_padre()
#funcion_principal(lambda: print("Soy una función como parámetro"))
# funcion_principal(suma)

# Comprehension en Python es una forma concisa de crear listas, 
# conjuntos y diccionarios utilizando una sintaxis compacta.
# Se recomienda su uso cuando se necesita crear una nueva estructura de datos a partir de una existente, aplicando una transformación o filtrando elementos.
# Aquí hay tres ejemplos de comprehension en Python:

# Ejemplo 1: Crear una lista de los cuadrados de los números del 1 al 10
# cuadrados = [x**2 for x in range(1,11) if x % 2 ==0 ] # [4,16,36,64,100]
# print(cuadrados)
# cua=[]
# for x in range(1,11):
#    if x % 2 ==0:
#      cua.append(x**2)
# print(cua)    
# # Ejemplo 2: Crear un conjunto de los números pares del 1 al 10
# impares = tuple(x for x in range(1, 11) if x % 2 != 0)

# # # Ejemplo 3: Crear un conjunto de los números pares del 1 al 10
# pares = {x for x in range(1, 11) if x % 2 == 0}
# print(impares)
# print(pares)
# # # Ejemplo 3: Crear un diccionario con los números del 1 al 5 como claves y sus cuadrados como valores
# diccionario = {x: x**2 for x in range(1, 600)}
# print(diccionario)
# dic = {}
# for c,v in enumerate([1,2,3,4,5]):
#     dic[str(c)]=v**2
# exponente = lambda x: x**2
# inicio=time.time()
# print(f"Inicio Recorrido: {inicio}")
# cuadrados = [(lambda x: x**2)(x) for x in range(100) if x % 2 ==0 ]
# print(cuadrados)
# print(f"Fin Recorrido: {time.time()-inicio}") 
# Recomendaría el uso de comprehension cuando se necesite crear una nueva estructura de datos de manera concisa y legible.

#print(cuadrados,impares,pares,diccionario)
# funciones de orden superior
# El concepto de map en Python es una función incorporada que se utiliza para aplicar una función a cada elemento de una lista (u otro iterable) y devolver un nuevo iterable con los resultados.
# Se utiliza para realizar operaciones en paralelo en todos los elementos de una lista sin necesidad de utilizar bucles explícitos.
# Un ejemplo de uso de map en Python es para aplicar una función lambda a cada elemento de una lista.


# lista = [1, 2, 3, 4, 5]
# suma = lambda x: x + 2
# resultado = list(map(suma, lista))
# print(resultado)

# El concepto de filter en Python es una función incorporada que se utiliza para filtrar elementos de una lista (u otro iterable) según una condición.
# Se utiliza para seleccionar los elementos que cumplen con la condición especificada y devolver un nuevo iterable con esos elementos.
# Un ejemplo de uso de filter en Python es para filtrar los números pares de una lista.

# lista = [4, 5, 3, 7, 10,7,0,20]
# resultado = list(filter(lambda x: x % 2 == 0, lista))
# print(resultado)

#argumentos           (1,2,3,8)  {"num1":4,"num2:5"}
# def suma_con_args_kwargs(*args, **kwargs):
#     suma = 0
#     prom=0
#     print(args)
#     for arg in args:
#         suma += arg
#     print(kwargs)
#     for key, value in kwargs.items():
#         prom += value
    
#     return suma,prom/2

# resultado = suma_con_args_kwargs(1,2,3,8,20,nota1=50,nota2=40)
# print(resultado)

# def decorador_division_cero(func):
#     # Esta es la función wrapper que envuelve la función original
#     def nueva_funcionalidad(*args, **kwargs):
#         try:
           
#             return f"Dividir{args}= {func(*args, **kwargs)}"
#         except ZeroDivisionError:
#             # Si hay una división por cero, devolvemos un mensaje de error
#             return "Error: División por cero"
#     # Devolvemos la función wrapper
#     return nueva_funcionalidad


# @decorador_division_cero
# def dividir(a, b):
#     return a / b
# print(dividir(2,2))

# # decorador de clase
# def agregar_atributo(cls):
#     cls.nuevo_atributo = "Hola, soy un nuevo atributo!"
#     return cls

# @agregar_atributo
# class MiClase:
#     def __init__(self, valor):
#         self.valor = valor
#     def __str__(self):
#         return f"valor={self.valor} nuevo atributo={self.nuevo_atributo}"

# objeto = MiClase(10)
# print(objeto)

# # Los mixins son clases que contienen métodos que puedes utilizar en otras clases para agregar funcionalidad adicional. Son útiles cuando deseas compartir funcionalidad común entre varias clases sin usar herencia múltiple, ya que Python no admite herencia múltiple directa.
# class ConducirMixin:
#     def conducir(self):
#         return "Vehículo en movimiento"

# # # Clase base
# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca

# # Clase Coche con capacidad de conducir
# class Coche(Vehiculo, ConducirMixin):
#     def __init__(self, marca, modelo):
#         super().__init__(marca)
#         self.modelo = modelo
#     def __str__(self):
#         return f"Coche:{self.marca} - {self.modelo} - {self.conducir()}"
# # Crear instancias de Coche
# coche = Coche("Toyota", "Corolla")
# # Usar métodos de los mixins
# print(coche)
# print(coche.conducir()) 
# clases dentro de otra clase
# class OperacionMatematica():
#     def __init__(self, x):
#         self.x = x

#     class Suma:

#         def __init__(self, exterior, y):
#             self.resultado = exterior.x + y

# # Crear una instancia de la clase OperacionMatematica
# operacion = OperacionMatematica(10)
# print(operacion.x)
# Crear una instancia de la clase Suma dentro de OperacionMatematica
# suma = operacion.Suma(operacion,5)

# # # # 
# print(suma.resultado)  # Output: 15 (10 + 5)

# def imprimir_numeros(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         imprimir_numeros(n - 1)

# Llamamos a la función con el número inicial
# imprimir_numeros(10)

# La recursividad es un concepto en programación donde una función se llama a sí misma para resolver un problema más grande. 
# def imprimir_numeros(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         imprimir_numeros(n - 1)

# # Llamamos a la función con el número inicial
# imprimir_numeros(5)
# fac,n=1,5
# while n > 0:
#     fac = fac* n
#     n = n -1
# print("fac: ",fac)
    
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Ejemplo de uso
# print("fac recursivo:",factorial(5))  # Output: 120

