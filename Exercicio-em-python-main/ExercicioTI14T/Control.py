from Model import Model


class Control:
    def __init__(self):
        self.opcao = -1
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.modelo = Model()  # Conectando com a classe model

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def getNum3(self):
        return self.num3

    def getNum4(self):
        return self.num4

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2

    def setNum3(self, num3):
        self.num3 = num3

    def setNum4(self, num4):
        self.num4 = num4

    def coletar(self):
        print("Informe um número: ")
        self.setNum1(float(input()))

        print("Informe outro número: ")
        self.setNum2(float(input()))

    def menu(self):
        print("\nEscolha uma das opções abaixo: " +
              "\n0. Sair" +
              "\n1. Exercicio 1:" +
              "\n2. Exercicio 2:" +
              "\n3. Exercicio 3:" +
              "\n4. Exercicio 4:" +
              "\n5. Exercicio 5:" +
              "\n6. Exercicio 6:" +
              "\n7. Exercicio 7:" +
              "\n8. Exercicio 8:" +
              "\n9. Exercicio 9:" +
              "\n10. Exercicio 10:" +
              "\n11. Exercicio 11:" +
              "\n12. Exercicio 12:" +
              "\n13. Exercicio 13:" +
              "\n14. Exercicio 14:" +
              "\n15. Exercicio 15:" +
              "\n16. Exercicio 16:" +
              "\n17. Exercicio 17:" +
              "\n18. Exercicio 18:" +
              "\n19. Exercicio 19:" +
              "\n20. Exercicio 20:")
        self.setOpcao(int(input()))  # Coletando a escolha do usuário

    def operacao(self):
        while (self.getOpcao != 0):
            self.menu()  # Mostrar a lista de dados na tela
            if self.getOpcao() == 0:
                print("Obrigado!")
                break
            elif self.getOpcao() == 1:
                self.modelo.exercicio1()
            elif self.getOpcao() == 2:
                print("Digite um valor: ")
                print("O valor do Antecessor: {}".format(self.modelo.exercicio2(self.getNum1())))
            elif self.getOpcao() == 3:
                print("informe a base:")
                self.setNum1(float(input()))
                print("informe a altura:")
                self.setNum2(float(input()))
                print("A area do retangulo e: {}".format(self.modelo.exercicio3(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 4:
                print("informe quntos anos você tem:")
                self.setNum1(float(input()))
                print("informe quantos meses:")
                self.setNum2(float(input()))
                print("informe quantos dias:")
                self.setNum3(float(input()))
                print("Sua idade em dias é: {}".format(self.modelo.exercicio4(self.getNum1(), self.getNum2(), self.getNum3())))

            elif self.getOpcao() == 5:
                print("informe o número total de eletores: ")
                self.setNum1(float(input()))
                print("informe o número de votos em branco: ")
                self.setNum2(float(input()))
                print("informe o número de votos nulos: ")
                self.setNum3(float(input()))
                print("informe o número de votos validos:")
                self.setNum4(float(input()))
                self.modelo.exercicio5(self.getNum1(), self.getNum2(), self.getNum3(), self.getNum4())

            elif self.getOpcao() == 6:
                print("informe o seu salario atual: R$")
                self.setNum1(float(input()))
                print("informe o percentual salarial: %")
                self.setNum2(float(input()))
                print("O seu novo salario será de: R$ {:.2f}".format(self.modelo.exercicio6(self.getNum1(), self.getNum2())))

            elif self.getOpcao() == 7:
                print("Diga-me o valor do veiculo: R$")
                self.setNum1(float(input()))
                print("Informe o valor do distribuidor: R$")
                self.setNum2(float(input()))
                print("Diga-me o valor do imposto: R$")
                self.setNum3(float(input()))
                print("O valor do veiculo é: R$ {:.2f}".format(self.modelo.exercicio7(self.getNum1(), self.getNum2(), self.getNum3())))

            elif self.getOpcao() ==8:
                print("digite a primeira nota do aluno: ")
                self.setNum1(float(input()))
                print("digite a segunda nota do aluno: ")
                self.setNum2(float(input()))
                print("digite e a ultima nota do aluno: ")
                self.setNum3(float(input()))
                print("A nota final foi de: {}".format(self.modelo.exercicio8(self.getNum1(), self.getNum2(), self.getNum3())))

            elif self.getOpcao() == 9:
                print("Diga-me quantas maça você pegou? ")
                self.setNum1(float(input()))
                print("o valor da maça foi de: R$ {:.2f}".format(self.modelo.exercicio9(self.getNum1())))

            elif self.getOpcao() == 11:
                print("informe o seu Salario: R$")
                self.setNum1(float(input()))
                print("informe o valor das vendas: R$")
                self.setNum2(float(input()))
                print("O salario total é: R${:.2f}".format(self.modelo.exercicio11(self.setNum1(), self.setNum2())))

            elif self.getOpcao() == 12:
                print("informe o saldo: R$")
                self.setNum1(format(input()))
                print("informe o seu debito: R$")
                self.setNum2(format(input()))
                print("informe o seu credito: R$")
                self.setNum3(format(input()))
                self.modelo.exercicio5(self.getNum1(), self.getNum2(), self.getNum3(), self.getNum4())

            elif self.getOpcao() == 13:
                print("informe um valor de 1 a 10")
                print(self.modelo.exercicio13(int(input())))

            else:
                print("Opção invalida!")
