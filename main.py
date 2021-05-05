from colored import fg, bg, attr
from datetime import datetime
import time
import msvcrt
import os

def show_screen(menu, option):
    if      (menu == 0):  #Inicio/Voltar/Sair     ~
        if (option == -1):

            head()
            print("\n"+"[ MENU ]".center(os.get_terminal_size().columns))
            print("\n                 1 -> Iniciar Bot")
            print("                 2 -> Histórico de contas")
            print("                 3 -> Alterar configurações")
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

    elif    (menu == 1):  #Iniciar Bot            ~
        if (option == -1):

            clear()
            import account_creator_new
            return

    elif    (menu == 2):  #Historico              ~
        if (option == -1):

            head()
            print("\n"+"[ HISTORICO ]".center(os.get_terminal_size().columns))
            _option = Input()
            if (_option != 0):
                show_screen(_option, -1)
            else:
                show_screen(0, -1)
                return
            return

    elif    (menu == 3):  #Alterar config.txt     ~
        if (option == -1): #Tela principal (Alterar config.txt)

            head()
            config = open("config.txt", "r")
            lines = config.readlines()

            vpn_check = return_cfg("vpn")
            if(vpn_check):
                vpn_check = "X"
            else:
                vpn_check = " "

            clear_browser_check = return_cfg("clear_browser")
            if(clear_browser_check):
                clear_browser_check = "X"
            else:
                clear_browser_check = " "

            retry_captcha_check = return_cfg("retry_captcha")
            if(retry_captcha_check):
                retry_captcha_check = "X"
            else:
                retry_captcha_check = " "
            
            print("\n"+"[ CONFIGURAÇÕES ]".center(os.get_terminal_size().columns))
            print("\n               1 -> CHANGE CHROMEDRIVER PATH")
            print("               2 -> CHANGE API_KEY")
            print("               3 -> VPN                    ["+vpn_check+"]")
            print("               4 -> LIMPAR CACHE E COOKIES ["+clear_browser_check+"]")
            print("               5 -> RETRY CAPTCHA          ["+retry_captcha_check+"]")
            print("\n")
            print("              0 ->    Voltar")
            _option = Input()
            if   (_option == 1):
                show_screen(3,1)
                return
            elif (_option == 2):
                show_screen(3,2)
                return
            elif (_option == 3):
                if(vpn_check == "X"):
                    lines[2] = "vpn='False'\n"
                else:
                    lines[2] = "vpn='True'\n"
                config = open("config.txt", "w")
                config.writelines(lines)
                config.close()
                show_screen(3, -1)
                return
            elif (_option == 4):
                if(clear_browser_check == "X"):
                    lines[3] = "clear_browser='False'\n"
                else:
                    lines[3] = "clear_browser='True'\n"
                config = open("config.txt", "w")
                config.writelines(lines)
                config.close()
                show_screen(3, -1)
                return
            elif (_option == 5):
                if(retry_captcha_check == "X"):
                    lines[4] = "retry_captcha='False'"
                else:
                    lines[4] = "retry_captcha='True'"
                config = open("config.txt", "w")
                config.writelines(lines)
                config.close()
                show_screen(3, -1)
                return
            elif (_option == 0):
                show_screen(0, -1)
                return
            else:
                return ################################# ALTERAR ###################################
        
        elif (option == 1): #Alterar path

            head()
            config = open("config.txt", "r")
            lines = config.readlines()

            print("\n"+"[ CHROMEDRIVER PATH ]".center(os.get_terminal_size().columns))
            print("\n"+bg(15)+cBlack+return_cfg("path").center(os.get_terminal_size().columns)+cReset)
            print("1 -> Inserir         2 -> Default          0 -> Voltar".center(os.get_terminal_size().columns))
            _option = Input()
            if (_option == 1):
                print("INSERT: ")
                _path = input()
                config = open("config.txt", "w")
                lines[0] = "PATH='"+_path+"\chromedriver.exe'\n"
                config.writelines(lines)
                config.close()
                show_screen(3, 1)
            elif(_option == 2):
                config = open("config.txt", "w")
                lines[0] = "PATH='"+os.getcwd()+"\chromedriver.exe'\n"
                config.writelines(lines)
                config.close()
                show_screen(3, 1)                
            elif (_option == 0):
                show_screen(3, -1)
                return
            else:
                return ################################# ALTERAR ###################################
            
        elif (option == 2): #Alterar api key

            head()
            print("\n"+"[ API KEY ]".center(os.get_terminal_size().columns))
            print("\n"+bg(15)+cBlack+return_cfg("apikey").center(os.get_terminal_size().columns)+cReset)
            print("1 -> Alterar                   0 -> Voltar".center(os.get_terminal_size().columns))
            _option = Input()
            if (_option == 1):
                print("INSERT: ")
                _api_key = input()
                if (len(_api_key) == 32):
                    config = open("config.txt", "w")
                    lines[1] = "api_key='"+_api_key+"'\n"
                    config.writelines(lines)
                    config.close()
                    show_screen(3, 2)
                else:
                    print(cError+get_time()+"API KEY inválida."+cReset)
                    time.sleep(2)
                    show_screen(3, 2)
            elif (_option == 0):
                show_screen(3, -1)
            else:
                return ################################# ALTERAR ###################################

    elif    (menu == 4):  #Configurações          ~
        if (option == -1):
            return
    
    else:
        return ################################# ALTERAR ###################################

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
        elif    (_input == '5'):
            return 5
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

def config_captcha(api_key):
    config_ac_api_key = open(os.getcwd()+"\essentials\Anticaptcha-plugin_v0.53\js\config_ac_api_key.js","r")
    content = config_ac_api_key.readlines()
    content[2] =    "var antiCapthaPredefinedApiKey = '"+api_key+"';\n"
    content[8] =    "    auto_submit_form: true,\n"
    content[30] =   "    use_recaptcha_precaching: true,\n"

    config_ac_api_key = open(os.getcwd()+"\essentials\Anticaptcha-plugin_v0.53\js\config_ac_api_key.js","w")
    config_ac_api_key.writelines(content)
    config_ac_api_key.close()
    return

def return_cfg(cfg):
    if (check_cfg() != 0):
        config = open("config.txt", "r")
        _path = config.readline()
        _apikey = config.readline()
        _vpn = config.readline()
        _clear_browser = config.readline()
        _retry_captcha = config.readline()
        config.close()
        
        if      (cfg == "path"):
            return _path[6:-2]
        elif    (cfg == "apikey"):
            return _apikey[9:-2]
        elif    (cfg == "vpn"):
            if (_vpn[5:-2] == "True"):
                return True
            elif (_vpn[5:-2] == "False"):
                return False
            else:
                return Exception
        elif    (cfg == "clear_browser"):
            if (_clear_browser[15:-2] == "True"):
                return True
            elif (_clear_browser[15:-2] == "False"):
                return False
            else:
                return Exception
        elif    (cfg == "retry_captcha"):
            if (_retry_captcha[15:-1] == "True"):
                return True
            elif (_retry_captcha[15:-1] == "False"):
                return False
            else:
                return Exception
        else:
            return Exception

def check_cfg():
    try:
        config = open("config.txt", "r")
        _path = config.readline()
        _apikey = config.readline()
        _vpn = config.readline()
        _clear_browser = config.readline()
        _retry_captcha = config.readline()
        

        if (_path[:6] != "PATH='"                           #Primeira linha não é PATH='
        or _path[:7] == "PATH=''"                           #PATH está vazio
        or _apikey[:9] != "api_key='"                       #Segunda linha não é api_key='
        or _apikey[:10] == "api_key=''"                     #api_key está vazio
        or len(_apikey[9:-2]) != 32                         #api_key é invalido (32 digitos)
        or _vpn[:5] != "vpn='"                              #Terceira linha não é vpn='
        or _vpn[:6] == "vpn=''"                             #vpn está vazio
        or _clear_browser[:15] != "clear_browser='"         #Quarta linha não é clear_browser='
        or _clear_browser[:16] == "clear_browser=''"        #clear_browser está vazio
        or _retry_captcha[:15] != "retry_captcha='"         #Quinta linha não é retry_captcha='
        or _retry_captcha[:16] == "retry_captcha=''"):      #retry_captcha está vazio

            print(cError+get_time()+"Arquivo config.txt configurado incorretamente."+cReset)
            raise OSError

    except OSError:
        time.sleep(2)
        print(cMessage+get_time()+"Gerando novo arquivo config.txt..."+cReset)
        print(cMessage+get_time()+"PATH='"+cWarning+os.getcwd()+"\essentials\chromedriver.exe'"+cReset)
        print(cMessage+get_time()+"api_key="+cReset)
        time.sleep(1)

        try:
            api__key = input()
            if(len(api__key) != 32):
                raise
        except:
            print(cError+get_time()+"API Key inválido. Se o problema persistir, altere manualmente no .txt"+cReset)
            return 0
        else:
            print(cMessage+get_time()+"vpn="+cWarning+"'True'"+cMessage+"\n"+get_time()+"clear_browser="+cWarning+"'True'"+cMessage+"\n"+get_time()+"retry_captcha="+cWarning+"'True'"+cReset)
            config = open("config.txt", "w+")
            time.sleep(1)
            config.write("PATH='"+os.getcwd()+"\essentials\chromedriver.exe'\napi_key='"+api__key+"'\nvpn='True'\nclear_browser='True'\nretry_captcha='True'")
            config.close()
            config_captcha(api__key)
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