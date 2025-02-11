def distinguir_positivos(num):
    """
distinguir_positivos: Number -> String
    dato entrada: Number
    mensaje: String
    
    Clasifica los numeros dados dando un
    mensaje para cada categoria, >0, ==0, <0.
    
Ejemplos:
    distinguir_positivos(5) == 'Numero positivo.'
    distinguir_positivos(0) == 'Es cero.'
    distinguir_positivos(-5) == 'Numero negativo.'
    """
    if(num > 0):
        respuesta = "Numero positivo."
    elif(num==0):
        respuesta = "Es cero."
    else:
        respuesta = "Numero negativo."
    return respuesta

def test_distinguir_positivos():
    assert distinguir_positivos(5) == "Numero positivo."
    assert distinguir_positivos(0) == "Es cero."
    assert distinguir_positivos(-5) == "Numero negativo."

def main():
    num = int(input("Ingrese un numero: "))
    resp = distinguir_positivos(num)
    print(resp)
    ejecutar = input("Ingrese S para seguir o otra letra para finalizar: ")
    if ejecutar == "S":
        main()
    else:
        exit()

if __name__ == '__main__':
    main()
