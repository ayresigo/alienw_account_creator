from colored import fg, bg, attr
from datetime import datetime
import time
import msvcrt
import os

def show_screen(menu, option):
    if      (menu == 0 and option == -1):  #Inicio/Voltar/Sair     ~
        head()

        print("\n"+"[ MENU ]".center(os.get_terminal_size().columns))
        print("\n                 1 -> Iniciar Bot")
        print("                 2 -> Histórico de contas")
        print("                 3 -> Alterar config.txt")
        print("                 4 -> Configurações")
        print("\n")
        print("                 0 ->    Sair")

        _option = Input()
        if (_option != 0):
            show_screen(_option, -1)
        else:
            return
        #Iniciar Bot        -> Qtd contas a criar
        #                   -> Revisar configurações

        #Configurações      -> Toggle VPN
        #                   -> Toggle Limpar Cache/Cookies
        #                   -> Retry captcha

    elif    (menu == 1 and option == -1):  #Iniciar Bot            ~
        clear()
        import account_creator
        return

    elif    (menu == 2 and option == -1):  #Historico              ~
        head()

        print("\n"+"[ HISTORICO ]".center(os.get_terminal_size().columns))
        _option = Input()
        if (_option != 0):
            show_screen(_option, -1)
        else:
            show_screen(0, -1)
            return

        return

    elif    (menu == 3 and option == -1):  #Alterar config.txt     ~
        return

    elif    (menu == 4 and option == -1):  #Configurações          ~
        return

def Input():
    _input = 1
    while (_input != 0):
        _input = msvcrt.getch().decode("utf-8").lower()
        if      (_input == '1'):
            return 1
        elif    (_input == '2'):
            return 2
        elif    (_input == '3'):
            return 3
        elif    (_input == '4'):
            return 4
        elif    (_input == '0'):
            return 0
        else:
            return 0

def head():
    clear()
    check_cfg()
    print (bg(6)+fg(255)+attr('bold')+"".center(os.get_terminal_size().columns))
    print ("[ Alien Worlds Account Creator V0.1 ]".center(os.get_terminal_size().columns))
    print ("".center(os.get_terminal_size().columns)+attr('reset'))

def get_time(): #Pega o timestamp pelo horário atual.
    now = datetime.now()
    return "[ " + now.strftime("%H:%M:%S") + " ] "

def check_cfg():
    try:
        config = open("config.txt", "r")
        _path = config.readline()
        _apikey = config.readline()

        if (_path[:6] != "PATH='"       #Primeira linha não é PATH='
        or _path[:7] == "PATH=''"       #PATH está vazio
        or _apikey[:9] != "api_key='"   #Segunda linha não é api_key='
        or _apikey[:10] == "api_key=''" #api_key está vazio
        or len(_apikey[9:-1]) != 32):   #api_key é invalido (32 digitos)

            print(cError+get_time()+"Arquivo config.txt configurado incorretamente."+cReset)
            raise OSError

    except OSError:
        time.sleep(2)
        print(cMessage+get_time()+"Gerando novo arquivo config.txt..."+cReset)
        print(cMessage+get_time()+"PATH='"+os.getcwd()+"\chromedriver.exe'"+cReset)
        print(cMessage+get_time()+"api_key="+cReset)

        try:
            api__key = input()
            if(len(api__key) != 32):
                raise
        except:
            print(cError+get_time()+"API Key inválido. Se o problema persistir, altere manualmente no .txt"+cReset)
            return 0
        else:
            config = open("config.txt", "w+")
            config.write("PATH='"+os.getcwd()+"\chromedriver.exe'\napi_key='"+api__key+"'")
            return 1

    except:
        print(cError+get_time()+"Erro inesperado. Encerrando..."+cReset)
        return 0
    else:
        config.close()
        return 1

#Cores do console
cBlack = fg(0) #Preto
cError = fg(1) #Vermelho
cMessage = fg(84) #Verde
cWarning = fg(3) #Amarelho
cGreenBg = bg(84) #Fundo verde
cReset = attr('reset') #Reset

cmd = 'mode 60,35'
clear = lambda: os.system('cls')
os.system(cmd)
if (check_cfg() == 1):
    time.sleep(1)
    show_screen(0, -1)
else:
    print(cError+get_time()+"Encerrando..."+cReset)
    time.sleep(3)








"""
def main_menu():
    
    
    #print(char)

def iniciar_bot():
    head()
    operator2 = 1
    print("Pagina incial")
    operator2 = msvcrt.getch().decode("utf-8").lower()
    while(operator2 != 5):
        if (operator2 == 0):
            print("Returning...")
            main_menu()
    
def historico():
    return

def alterar_config():
    return

def configuracoes():
    return

"""


