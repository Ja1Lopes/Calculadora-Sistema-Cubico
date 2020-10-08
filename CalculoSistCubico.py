import math

print("Olá, usuário")

while True:

    pi = float(math.pi)
    resultado = 0

    operation = input("Selecione a operação desejada: \n"
                      " CS(1) \n"
                      " CCC(2) \n"
                      " CFC(3) \n"
                      " Sair(n) \n")



    if operation == 'n':
        print("Saindo")
        exit()



    if operation == '1':

        escolha = input("Deseja salvar os resultados? (s) or (n)")
        if escolha == 's':
            try:
                file1 = open(
                    'C:\\Users\\João Lopes\\Documents\\Programação\Phyton\\TXT\\ResultadosCS.txt', 'r+')
            except FileNotFoundError:
                print("Arquivo não encontrado, criando....")
                file1 = open(
                    'C:\\Users\\João Lopes\\Documents\\Programação\\Phyton\\TXT\ResultadosCS.txt', 'w+')
        elif escolha == 'n':
            pass

        teste = input("a or r?  ")

        if teste == 'a':
            a = float(input("Parametro de rede:  "))
            r = float(a/2)
            vc = float(a ** 3)
            va = float(4/3 * pi * r ** 3)
            n = 1
            fe = float((n * va) / vc)
            resultado = 1
            if resultado == 1:
                print("\t Parâmetro de rede = ", a)
                print("\t Raio atômico = ", r)
                print("\t Número de átomos que ocupam a célula = ", n)
                print("\t Volume unitário = ", vc)
                print("\t Volume atômico = ", va)
                print("\t Fator de empacotamento = ", fe)

        if teste == 'r':
            r = float(input("Raio Atomico:  "))
            a = float(2*r)
            vc = float(8 * r ** 3)
            va = float(4/3 * pi * r ** 3)
            n = 1
            fe = float((n * va) / vc)
            resultado = 1
            if resultado == 1:
                print("\t Parâmetro de rede = ", a)
                print("\t Raio atômico = ", r)
                print("\t Número de átomos que ocupam a célula = ", n)
                print("\t Volume unitário = ", vc)
                print("\t Volume atômico = ", va)
                print("\t Fator de empacotamento = ", fe)

        resultados = list()
        resultados.append("Resultados \n")
        resultados.append("\t Parâmetro de rede = ")
        resultados.append(str(a))
        resultados.append('\n')
        resultados.append("\t Raio atômico = ")
        resultados.append(str(r))
        resultados.append('\n')
        resultados.append("\t Número de átomos que ocupam a célula = ")
        resultados.append(str(n))
        resultados.append('\n')
        resultados.append("\t Volume unitário = ")
        resultados.append(str(vc))
        resultados.append('\n')
        resultados.append("\t Volume atômico = ")
        resultados.append(str(va))
        resultados.append('\n')
        resultados.append("\t Fator de empacotamento = ")
        resultados.append(str(fe))
        resultados.append('\n')
        file1.writelines(resultados)
        file1.close()



    if operation == '2':

        escolha = input("Deseja salvar os resultados? (s) or (n)")
        if escolha == 's':
            try:
                file2 = open(
                    'C:\\Users\\João Lopes\\Documents\\Programação\Phyton\\TXT\\ResultadosCCC.txt', 'r+')
            except FileNotFoundError:
                print("Arquivo não encontrado, criando....")
                file2 = open(
                    'C:\\Users\\João Lopes\\Documents\\Programação\\Phyton\\TXT\ResultadosCCC.txt', 'w+')
        elif escolha == 'n':
            pass

        teste = input("a or r?  ")

        if teste == 'a':
            a = float(input("Parametro de rede:  "))
            r = float((a * 3 ** 0.5) / 4)
            vc = float(a ** 3)
            va = float(4/3 * pi * r ** 3)
            n = 2
            fe = float((n * va) / vc)
            resultado = 1
            if resultado == 1:
                print("\t Parâmetro de rede = ", a)
                print("\t Raio atômico = ", r)
                print("\t Número de átomos que ocupam a célula = ", n)
                print("\t Volume unitário = ", vc)
                print("\t Volume atômico = ", va)
                print("\t Fator de empacotamento = ", fe)

        if teste == 'r':
            r = float(input("Raio Atomico:  "))
            a = float((4 * r) / 3 ** 0.5)
            vc = float(a ** 3)
            va = float(4/3 * pi * r ** 3)
            n = 2
            fe = float((n * va) / vc)
            resultado = 1
            if resultado == 1:
                print("\t Parâmetro de rede = ", a)
                print("\t Raio atômico = ", r)
                print("\t Número de átomos que ocupam a célula = ", n)
                print("\t Volume unitário = ", vc)
                print("\t Volume atômico = ", va)
                print("\t Fator de empacotamento = ", fe)

        resultados = list()
        resultados.append("Resultados \n")
        resultados.append("\t Parâmetro de rede = ")
        resultados.append(str(a))
        resultados.append('\n')
        resultados.append("\t Raio atômico = ")
        resultados.append(str(r))
        resultados.append('\n')
        resultados.append("\t Número de átomos que ocupam a célula = ")
        resultados.append(str(n))
        resultados.append('\n')
        resultados.append("\t Volume unitário = ")
        resultados.append(str(vc))
        resultados.append('\n')
        resultados.append("\t Volume atômico = ")
        resultados.append(str(va))
        resultados.append('\n')
        resultados.append("\t Fator de empacotamento = ")
        resultados.append(str(fe))
        resultados.append('\n')
        file2.writelines(resultados)
        file2.close()



    if operation == '3':

        escolha = input("Deseja salvar os resultados? (s) or (n)")
        if escolha == 's':
            try:
                file3 = open(
                    'C:\\Users\\João Lopes\\Documents\\Programação\Phyton\\TXT\\ResultadosCFC.txt', 'r+')
            except FileNotFoundError:
                print("Arquivo não encontrado, criando....")
                file3 = open(
                    'C:\\Users\\João Lopes\\Documents\\Programação\\Phyton\\TXT\ResultadosCFC.txt', 'w+')
        elif escolha == 'n':
            pass

        teste = input("a or r?  ")

        if teste == 'a':
            a = float(input("Parametro de rede:  "))
            r = float((2*a) ** 0.5 / 4)
            vc = float(16 * r ** 3 * (2 ** 0.5))
            va = float(4/3 * pi * r ** 3)
            n = 4
            fe = float((n * va) / vc)
            resultado = 1
            if resultado == 1:
                print("\t Parâmetro de rede = ", a)
                print("\t Raio atômico = ", r)
                print("\t Número de átomos que ocupam a célula = ", n)
                print("\t Volume unitário = ", vc)
                print("\t Volume atômico = ", va)
                print("\t Fator de empacotamento = ", fe)

        if teste == 'r':
            r = float(input("Raio Atomico:  "))
            a = float(2 * r * (2 ** 0.5))
            vc = float(16 * r ** 3 * (2 ** 0.5))
            va = float(4/3 * pi * r ** 3)
            n = 4
            fe = float((n * va) / vc)
            resultado = 1
            if resultado == 1:
                print("\t Parâmetro de rede = ", a)
                print("\t Raio atômico = ", r)
                print("\t Número de átomos que ocupam a célula = ", n)
                print("\t Volume unitário = ", vc)
                print("\t Volume atômico = ", va)
                print("\t Fator de empacotamento = ", fe)

        resultados = list()
        resultados.append("Resultados \n")
        resultados.append("\t Parâmetro de rede = ")
        resultados.append(str(a))
        resultados.append('\n')
        resultados.append("\t Raio atômico = ")
        resultados.append(str(r))
        resultados.append('\n')
        resultados.append("\t Número de átomos que ocupam a célula = ")
        resultados.append(str(n))
        resultados.append('\n')
        resultados.append("\t Volume unitário = ")
        resultados.append(str(vc))
        resultados.append('\n')
        resultados.append("\t Volume atômico = ")
        resultados.append(str(va))
        resultados.append('\n')
        resultados.append("\t Fator de empacotamento = ")
        resultados.append(str(fe))
        resultados.append('\n')
        file3.writelines(resultados)
        file3.close()