def calificacion_comentario():
    num = 0
    comentario = "sin comentario, puntos perfectos"
    while num < 1 or num > 5:
        num = int(input("Ingresa una calificación del 1 al 5: "))
    if num < 3:
        comentario = input("Ingrese una sugerencia para mejorar: ")
        if comentario == '':
            comentario = "sin comentario"
    else:
        comentario = input("Ingrese un comentario (opcional): ")
        if comentario == '':
            comentario = "sin comentario"
    file = open("data.txt", 'a')
    post = f'puntos: {num} \ncomentario: {comentario}'
    file.write(f'{post}\n')
    file.close()
    print("Se guardó el comentario satisfactoriamente")
def registro():
    print("Resgistros hasta el momento")
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()