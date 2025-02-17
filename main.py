def karatsuba(x, y):
    if x<10 or y<10:
        return x*y

    n = max(tam(x), tam(y)) #a variável n precisa ser o número de dígitos do maior número
    m = n//2

    a = x//(10**m)
    b = x%(10**m)
    c = y//(10**m)
    d = y%(10**m)

    z0 = karatsuba(b,d) #partes mais baixas
    z1 = karatsuba((a+b),(c+d)) #soma das partes
    z2 = karatsuba(a,c) #partes mais altas

    result = z2*(10**(2*m))+(z1-z2-z0)*(10**m)+z0
    return result

def tam(x):
    if x<10:
        return 1

    contador = 0
    while x>0:
        x = x//10
        contador += 1

    return contador

def main():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    print(karatsuba(x,y))

main()