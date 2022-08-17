import math


class Model:

    def __init__(self):
        self.a = 0
        self.b = 0

    def exercicio1(self):
        a = 10
        b = 20
        self.a = b
        self.b = a
        return print("Número A:",self.a,"Número B:", self.b)

    def exercicio2(self, num1):
        return num1 - 1

    def exercicio3(self, base, altura):
        return base * altura

    def exercicio4(self, ano, mes, dias):
        return ano * 360 + mes * 12 + dias

    def exercicio5(self, eleitor, branco, nulos, validos):
        totalnulo = (nulos / eleitor) * 100
        totalvalido = (validos / eleitor) * 100
        totalbranco = (branco / eleitor) * 100
        return print("O total de votos foi: ", eleitor, "%\nO total de votos nulos foi de: ", totalnulo, "%\nO total de votos brancos foi de: ", totalbranco, "%\nO total de votos válidos é de: ", totalvalido, "%")

    def exercicio6(self, salario, reajuste):
        return salario + (salario * reajuste / 100)

    def exercicio7(self, custo, distri, impos):
        distri = custo * (28 / 100)
        impos = custo * (45 / 100)

        return distri + impos + custo

    def exercicio8(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3) / 3

    def exercicio9(self, maca):
        if maca >= 12:
            return maca * 1
        else:
            return maca * 1.3

    def exercicio10(self):
        return

    def exercicio11(self, bonus, venda, salario, comissao2, comissao):
        comissao2 = bonus * 5 / 100
        comissao = venda * 3 / 100
        return salario

    def exercicio12(self, saldo, credito, debito, numConta):
        final = saldo - debito + credito
        if final >= 0:
            return print(f' Número da conta {numConta}' f' Seu saldo é: {final}' f' saldo positivo')
        else:
            return print(f' Número da conta {numConta}' f' Seu saldo é: {final}' f' saldo negativo')

    def exercicio13(self, num):
        if num < 10 and num > 1:
            msg = ""
            for i in range(11):
                msg = msg + "\n{} * {} = {}".format(num, i, num * i)
            return msg
        else:
            print("Somente numero de 1 a 10")

    def exercicio14(self):
        return
