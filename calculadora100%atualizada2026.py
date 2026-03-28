from calculos import * #o * chama todas as funções do import
menu1 = 1 
hist = []  
op = ()
while menu1 == 1:
    while True:
        try:
            menu2 = int(input("Selecione a ação que deseja realizar: 1-Calcular, 2-Historico, 3-Limpar, 4-Finalizar, 5-Calcular binário "))
            break
        except ValueError:
            print("Inválido")
    match menu2:


        case 1:
            while True:
                try:
                    n1 = float(input("Insira o primeiro numero "))
                    result = None
                    break
                except ValueError:
                    print("Inválido")

            while True:
                op = None
                if result != None:
                    n1 = result
                sinais = ["+", "-", "*", "/", "r", "%", "**"]
                while op not in sinais:
                    op = input(f" Insira +, -, /, * ou r para Raiz, % para porcentagem, ** para elevar ao quadrado {n1} ")
                
                para_op = False
                
                match op:
                    case "%":
                        porcentagem = float(input(f"{n1} Insira o número que você deseja tirar {n1}% : "))
                        result = porcentagemc(n1, porcentagem)
                    case "r":         
                        result = raiz(n1)
                    case "**":          
                        result = elevar(n1)
                    case _:
                        while True:
                            try:
                                n2 = float(input(f"{n1} {op} "))
                                break 
                            except ValueError:
                                print("Inválido")
                        para_op = True
                        
                        match op:
                            case "+":
                                result = somar(n1, n2)
                                
                            case "-":
                                result = subtrair(n1, n2)
                                
                            case "/":
                                result =  dividir(n1, n2)
                                
                            case "*":
                                result =  multiplicar(n1, n2)
                                
                if op == "%":
                    print(f"{n1} {op} de {porcentagem} = {result}")
                    hist.append(f"[{n1} {op} de {porcentagem} = {result}]")
                elif para_op == True: 
                    print(f"{n1} {op} {n2} = {result}")
                    hist.append(f"[{n1} {op} {n2} = {result}]")
                elif para_op == False:
                    print(f"{n1} {op} = {result}")
                    hist.append(f"[{n1} {op} = {result}]")
               

                    
                escolha = input("Deseja continuar a operação?: (s/n) ").lower()
                if escolha == "n":
                    break
            
            
        case 2:
            for operacao in hist:
                print(operacao)
        case 3:
            hist.clear() 
            
        case 4:
            menu1 = 0

        case 5:
            while True:
                print("O que você deseja fazer?")
                print("1 - Decimal -> Binário")
                print("2 - Binário -> Decimal")
                print("3 - Decimal -> Octal")
                print("4 - Octal -> Decimal")
                print("5 - Decimal -> Hexadecimal")
                print("6 - Hexadecimal -> Decimal")
                print("7 - Hexadecimal -> Binário")
                print("8 - Binário -> Hexadecimal")
                print("9 - Hexadecimal -> Octal")
                print("10 - Octal -> Hexadecimal")
                print("Digite 11 para sair ")
                while True:
                    try:
                        op = int(input("Escolha uma opção: "))
                        break
                    except ValueError:
                        print("Inválido")

                #Decimal para Binário
                if op == 1:
                    while True:
                        try:
                            num = int(input("Digite um número decimal: "))
                            print("Binário:", bin(num)[2:])
                            break
                        except ValueError:
                            print("Inválido")

                #Binário para Decimal
                elif op == 2:
                    while True:
                        try:
                            num = input("Digite um número binário: ")
                            print("Decimal:", int(num, 2))
                            break
                        except ValueError:
                            print("Inválido")
   
                #Decimal para Octal
                elif op == 3:
                    while True:
                        try:
                            num = int(input("Digite um número decimal: "))
                            print("Octal:", oct(num)[2:])
                            break
                        except ValueError:
                            print("Inválido")

                #Octal para Decimal
                elif op == 4:
                    while True:
                        try:
                            num = input("Digite um número octal: ")
                            print("Decimal:", int(num, 8))
                            break
                        except ValueError:
                            print("Inválido")

                #Decimal para Hexadecimal
                elif op == 5:
                    while True:
                        try:
                            num = int(input("Digite um número decimal: "))
                            print("Hexadecimal:", hex(num)[2:].upper())
                            break
                        except ValueError:
                            print("Inválido")

                #Hexadecimal para Decimal
                elif op == 6:
                    while True:
                        try:
                            num = input("Digite um número hexadecimal: ")
                            print("Decimal:", int(num, 16))
                            break
                        except ValueError:
                            print("Inválido")

                #Hexadecimal para Binário
                elif op == 7:
                    while True:
                        try:
                            num = input("Digite um número hexadecimal: ")
                            decimal = int(num, 16)
                            print("Binário:", bin(decimal)[2:])
                            break
                        except ValueError:
                            print("Inválido")

                #Binário para Hexadecimal
                elif op == 8:
                    while True:
                        try:
                            num = input("Digite um número binário: ")
                            decimal = int(num, 2)
                            print("Hexadecimal:", hex(decimal)[2:].upper())
                            break
                        except ValueError:
                            print("Inválido")

                #Hexadecimal para Octal
                elif op == 9:
                    while True:
                        try:
                            num = input("Digite um número hexadecimal: ")
                            decimal = int(num, 16)
                            print("Octal:", oct(decimal)[2:])
                            break
                        except ValueError:
                            print("Inválido")

                #Octal para Hexadecimal
                elif op == 10:
                    while True:
                        try:
                            num = input("Digite um número octal: ")
                            decimal = int(num, 8)
                            print("Hexadecimal:", hex(decimal)[2:].upper())
                            break
                        except ValueError:
                            print("Inválido")
                
                elif op == 11:
                    print("Saindo dos cálculos de binário... ")
                    break