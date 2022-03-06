# linhas de estilização
linha = "-"*50

def converterParaDecimal(num, baseOrigem):
    if (baseOrigem == 'b'):
        num = int(num)
        decimal, i = 0, 0
        while(num != 0):
            aux = num % 10
            decimal = decimal + aux * pow(2, i)
            num = num//10
            i += 1
        return decimal
    elif(baseOrigem == 'h'):
        num = num.upper()
        base, decimal = 1, 0  # base de conversão para servir como o resultado da exponencial de 16
        # For decrescente, irá parar em -1(Quando toda a string tiver sido lida), com passo -1 para ler da direita pra esquerda
        for i in range(len(num) - 1, -1, -1):
            if num[i] >= '0' and num[i] <= '9':
                decimal += (ord(num[i]) - 48) * base
                base = base * 16
            elif num[i] >= 'A' and num[i] <= 'F':
                decimal += (ord(num[i]) - 55) * base
                base = base * 16
        return decimal
    elif(baseOrigem == 'o'):
        num = int(num)
        # base de conversão para servir como o resultado da exponencial de 8
        decimal, base, aux = 0, 1, num
        while (aux != 0):
            digitoAtual = aux % 10
            aux = aux//10
            decimal += digitoAtual * base
            base = base * 8
        return decimal
    else:
        return None


def converterParaBase(decimal, baseDestino):
    if(baseDestino == 'b'):
        binario, i = 0, 0
        while (decimal):
            rem = decimal % 2
            c = pow(10, i)
            binario += rem * c
            decimal //= 2
            i += 1
        return binario  # O retorno do binário é feito como inteiro, para facilitar, não é necessário armazenar em array
    elif(baseDestino == 'h'):
        hexArray, i = [], 0
        while(decimal != 0):
            aux = 0
            aux = decimal % 16
            if(aux < 10):
                hexArray.append(chr(aux + 48))
                i += 1
            else:
                hexArray.append(chr(aux + 55))
                i += 1
            decimal = int(decimal / 16)
        # Fazendo reverse do array, pois a lista precisa ser exibida em ordem contrária
        hexArray.reverse()
        # Este comando converte uma lista de inteiros em uma string
        hexadecimal = ''.join(str(n) for n in hexArray)
        return hexadecimal
    elif(baseDestino == 'o'):
        aux, i = [], 0
        while (decimal != 0):
            aux.append(decimal % 8)
            decimal = decimal//8
            i += 1
        aux.reverse()  # Fazendo reverse do array, pois a lista precisa ser exibida em ordem contrária
        # Este comando converte uma lista de inteiros em uma string
        octal = ''.join(str(n) for n in aux)
        return octal
    else:
        return None


while(1):
    #  interface bonita do codigo
    num = input(
        "Digite o numero a ser convertido:\n>>>> ")
    print(linha)
    baseOrigem = input(
        "Qual base você está?\nh) Hexadecima/ 16\nd) Decimal/ 10\no) Octadecimal/ 8 \nb) Binária/ 2\n>>>>  ")
    print(linha)
    baseOrigem = baseOrigem.lower()
    baseDestino = input(
        "Pra qual base você quer ir?\nh) Hexadecima/ 16\nd) Decimal/ 10\no) Octadecimal/ 8 \nb) Binária/ 2\n>>>>  ")
    print(linha)
    baseDestino = baseDestino.lower()
    decimal = None
    if(baseOrigem == baseDestino):
        print("A base de origem não pode ser a mesma da base de Destino, insira os dados novamente\n")
    # Apenas as bases h,o e b precisam de conversão para decimal, converter dec -> dec é desnecessário
    # A conversão da base de Origem para uma intermediária(Decimal) é feito para facilitar as operações finais, dessa forma, não é necessário fazer funções que envolvam um produto cartesiano das bases(Função para converter cada base de origem para cada base de destino), ex: Func de bin -> hex, func de bin->oct, func de bin->dec, etc
    # Dessa forma, fazemos apenas: Func de baseOrigem -> decimal e Func de baseDecimal->BaseDestino
    elif(baseOrigem == 'h' or baseOrigem == 'o' or baseOrigem == 'b'):
        decimal = converterParaDecimal(num, baseOrigem)
        # Exibição dos resultados
        if(not decimal):  # Base informada é inválida
            print("Dados inválidos, insira novamente\n")
        elif(baseDestino == 'd'):
            print(decimal)
            break
    else:
        decimal = int(num)

    if(not decimal):  # Base informada é inválida
        print("Dados inválidos, insira novamente\n")
    else:
        convertido = converterParaBase(decimal, baseDestino)
        if(convertido):
            print(convertido)
            break
        else:  # Base informada é inválida
            print("Dados inválidos, insira novamente\n")