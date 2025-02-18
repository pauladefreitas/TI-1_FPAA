# Algoritmo de Karatsuba em Python

O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números inteiros grandes, introduzida por Anatoly Karatsuba em 1960. Ele melhora a complexidade da multiplicação em comparação ao método tradicional de multiplicação direta, reduzindo o número de multiplicações necessárias e, consequentemente, o tempo de execução para números com muitos dígitos.

## Implementação do Algoritmo

A implementação inicia-se com a declaração da função recursiva principal do algoritmo de Karatsuba.

```python
   def karatsuba(x, y):
```

A partir disso, inicia-se a implantação da função com a validação do valor. Caso o valor de _x_ ou de _y_ for menor que 10, o valor retornado é a multiplicação entre os dois valores.

```python
    if x<10 or y<10:
        return x*y
```

Logo após, há a obtenção do tamanho do maior número em dígitos e a definição da metade do tamanho para divisão, onde inicia-se o processo de divisão e conquista.

```python
    n = max(tam(x), tam(y)) #a variável n precisa ser o número de dígitos do maior número
    m = n//2 #metade do tamanho para divisão
```

A divisão dos valores de _x_ e _y_ é feita para separar as partes alta e baixa de cada número, facilitando a aplicação recursiva do algoritmo de Karatsuba. Essa separação ocorre da seguinte forma:

```python
    a = x//(10**m)
    b = x%(10**m)
    c = y//(10**m)
    d = y%(10**m)
```

Onde _a_ e _c_ representam os dígitos mais significativos (parte alta) de x e y, respectivamente. São obtidos por uma divisão inteira. E _b_ e _d_ correspondem aos dígitos menos significativos (parte baixa), sendo extraídos com o operador módulo (%).

Posteriormente, há uma recursão para calcular os produtos menores.

```python
    z0 = karatsuba(b,d) #partes mais baixas
    z1 = karatsuba((a+b),(c+d)) #soma das partes
    z2 = karatsuba(a,c) #partes mais altas
```

O último passo dessa função é o cálculo do resultado final combinando os produtos parciais.

```python
    result = z2*(10**(2*m))+(z1-z2-z0)*(10**m)+z0
```

No código, ainda há uma função auxiliar que conta o número de dígitos do maior número.

```python
def tam(x):
    if x<10:
        return 1

    contador = 0
    while x>0:
        x = x//10
        contador += 1

    return contador
```

## Como rodar em ambiente local?

### Passo 1: Clonar o repositório

1. Clone o repositório git em uma pasta no seu ambiente local com o seguinte comando:

   ```bash
   git clone https://github.com/seu-usuario/karatsuba.git
   cd karatsuba
   ```

### Passo 2: Executar o script

1. Execute o script principal:

   ```bash
   python main.py
   ```

2. O programa solicitará que você insira dois números, como:

   ```bash
   Digite o valor de x:
   Digite o valor de y:
   ```

3. O resultado será exibido logo depois.
