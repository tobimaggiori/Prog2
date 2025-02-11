def contar(l, x, result=0):
    if x == "":
        return result
    else:
        if x[0] == l:
            return (contar(l, x[1:], result+1))
        else:
            return (contar(l, x[1:], result))

print(contar("l", "hola"))
