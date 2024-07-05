from funcion import *
print("HOLA, bienvenido")
while True:
    print('seleccione el proceso que desea realizar')
    print('1: Ingrese puntos de evaluación y comentarios')
    print('2: Comprueba los resultados hasta el momento')
    print('3: Finalizar')
    num=int(input())
    if num==3:
        print("Se finalizó el programa")
        break
    elif num==1:
        calificacion_comentario()
    elif num==2:
        registro()