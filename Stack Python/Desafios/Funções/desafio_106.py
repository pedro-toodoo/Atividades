def ajuda():
    while True:
        qnt_menu = len("SISTEMA DE AJUDA EM PYTHON")

        print("\033[30;44m-\033[m"*qnt_menu)
        print("\033[1;30;44mSISTEMA DE AJUDA EM PYTHON\033[m")
        print("\033[30;44m-\033[m"*qnt_menu)

        comando = input("Função ou biblioteca que deseja receber informações: ")
        qnt = len(comando) + len("Manual ''")

        print(f"\033[4;30;41mManual '{comando}'\033[m")
        help(comando)

        if comando in "fimFIM":
            break

ajuda()