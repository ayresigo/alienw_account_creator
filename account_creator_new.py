from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium.webdriver.common.action_chains import ActionChains
from colored import fg, bg, attr
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import unidecode
import unicodedata
import time
import string
import random

#TODO
#CONFIRMAR VERIFICAÇÃO YOPMAIL
#OPÇÃO DE LOGIN
#   SELECIONAR CONTAS DO BOT

def generate_email(): #Gera email aleatório com o <head> do wikipedia.
    print(output(Warn, "Gerando e-mail..."))
    if(return_cfg("random_mail") == ""):
        driver.execute_script("window.open();") #Abre nova aba
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://en.wikipedia.org/wiki/Special:Random')
        temp = driver.find_element_by_class_name("firstHeading").text
        for char in string.punctuation:
            temp = temp.replace(char, '') #Tira pontuação
        for char in string.digits:
            temp = temp.replace(char, '') #Tira símbolos
        email = ''.join(temp.split()).join(random.choice(string.ascii_lowercase) for i in range(4)) #Junta 4 letras aleatórias
        unidecode.unidecode(email)
        email = email[:random.randint(7,9)] #Corta a stringa aleatoriamente para ficar entre 7 e 9 caracteres
        for i in range(4): #Acrescenta 4 numeros aleatórios no final
            email += random.choice(string.digits)
        print(output(Message, "Email "+bg(84)+fg(0)+email+attr('reset')+fg(84)+" criado com sucesso."))
        driver.execute_script("window.close();") #Fecha aba aberta
        driver.switch_to.window(driver.window_handles[0])
        return email
    else:
        email = return_cfg("random_mail")
        for i in range(4):
            email+= random.choice(string.digits)
        print(output(Message, "Email "+bg(84)+fg(0)+email+attr('reset')+fg(84)+" criado com sucesso."))
        return email

def generate_pw(): #Gera senha aleatória
    print(output(Warn, "Gerando senha..."))
    if(return_cfg("random_pw") == ""):
        random_source = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)

        for i in range(6):
            password += random.choice(random_source)

        password_list = list(password)
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        print(output(Message, "Senha "+bg(84)+fg(0)+password+attr('reset')+fg(84)+" criada com sucesso."))
        return password
    else:
        print(output(Warn, "Pulando geração de senha. Usando senha padrão ..."))
        return password

def return_cfg(cfg): #Retorna algum dado do config.txt ("path", "apikey", "vpn", "clear_browser", "retry_captcha", "random_mail", "random_pw")
    config = open("config.txt", "r")
    _path = config.readline()
    _apikey = config.readline()
    _vpn = config.readline()
    _clear_browser = config.readline()
    _retry_captcha = config.readline()
    _random_mail = config.readline()
    _random_pw = config.readline()
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
        if (_retry_captcha[15:-2] == "True"):
            return True
        elif (_retry_captcha[15:-2] == "False"):
            return False
        else:
            return Exception
    elif    (cfg == "random_mail"):
            return _random_mail[13:-2]
    elif    (cfg == "random_pw"):
            return _random_pw[11:-2]            
    else:
        return Exception

def get_time(): #Pega o timestamp pelo horário atual.
    now = datetime.now()
    return "[ " + now.strftime("%H:%M:%S") + " ] "

def output(Type, String, Timestamp = True, Center = False): #Controla cores do console

    #Cores do console
    cBlack = fg(0) #Preto
    cError = fg(1) #Vermelho
    cMessage = fg(84) #Verde
    cWarning = fg(11) #Amarelho
    cGreenBg = bg(84) #Fundo verde
    cReset = attr('reset') #Reset

    timestamp = ""

    if (Center):
        String = String.center(os.get_terminal_size().columns)
    
    if (Timestamp):
        timestamp = get_time()

    if      (Type == "error"):
        return cError+timestamp+String+cReset
    elif    (Type == "message"):
        return cMessage+timestamp+String+cReset
    elif    (Type == "warn"):
        return cWarning+timestamp+String+cReset
    elif    (Type == "black"):
        return cBlack+timestamp+String+cReset
    else:
        return Type+timestamp+String+cReset
    return

def clear_browser(): #Limpa a cache do navegador ao abri-lo.
    try:
        if(return_cfg("clear_browser")):
            print(output(Warn, "Limpando Cookies..."))
            driver.delete_all_cookies()
            print(output(Warn, "Limpando Cache..."))
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
            time.sleep(2)
            actions = ActionChains(driver) 
            actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
            actions.perform()
            actions = ActionChains(driver) 
            actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
            actions.perform()
            time.sleep(2) # wait some time to finish
            driver.close() # close this tab
            driver.switch_to.window(driver.window_handles[0]) # switch back
            print(output(Message, "Cookies e Cache limpos com sucesso!"))
            return True
        else:
            print(output(Warn, "Pulando limpeza dos dados de navegação..."))
            return True
    except:
        return False

def wax_sign(email, password, register = True):
    try:
        print(output(Warn, "Acessando https://wallet.wax.io ..."))
        driver.get("https://wallet.wax.io")

        userName = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[5]/div/div/div/div[1]/div[1]/input')))
        print(output(Warn, "Inserindo email..."))
        userName.send_keys(email+"@yopmail.com")

        print(output(Warn, "Inserindo senha..."))
        pw = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[5]/div/div/div/div[1]/div[2]/input')
        pw.send_keys(password)

        print(output(Warn, "Aguardando resolução do CAPTCHA..."))
        if(register):
            sing_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[5]/div/div/div/div[5]/button[2]')))
        else:
            sing_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[5]/div/div/div/div[5]/button[1]')))
        print(output(Message, "Captcha resolvido!"))
        sing_button.click()
        return True
    except:
        return False

def confirm_email(email):
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("http://www.yopmail.com/en/")
    login = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]')))
    login.send_keys(email)
    login.submit()
    
    confirm = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="butmail"]/tbody/tr/td[6]/a')))
    confirm.click()
    time.sleep(10)
    confirm.send_keys(Keys.TAB * 9 + Keys.ENTER)
    
cmd = 'mode 75,50'
clear = lambda: os.system('cls')
os.system(cmd)

#Fake enum:
Error = "error"
Message = "message"
Warn = "warn"
Black = "black"

PATH = return_cfg("path")
anticaptcha_path= os.getcwd()+'\essentials\Anticaptcha-plugin_v0.53'

#Inicio do programa
print(output(Message, "[ AlienWorlds Account Creator v0.1 ]", False, True)+"\n")

options = webdriver.ChromeOptions()
options.add_argument(f"--load-extension={anticaptcha_path}")
#options.add_argument("--proxy-server='88.157.149.250:8080'")

options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

email = generate_email()
password = generate_pw()

if(clear_browser()):
    if(wax_sign(email, password)):
        if(confirm_email(email)):
            if(wax_sign(email, password, False)):
                print(output(Message, "Conta criada com sucesso!"))
else:
    print("Erro")

