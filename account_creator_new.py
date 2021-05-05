from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium.webdriver.common.action_chains import ActionChains
from colored import fg, bg, attr
from datetime import datetime

import os
import unidecode
import unicodedata
import time
import string
import random

def generate_email(): #Gera email aleatório com o <head> do wikipedia.
    """
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
    print(cMessage+get_time()+"Email "+cGreenBg+cBlack+email+cReset+cMessage+" gerado com sucesso.")
    driver.execute_script("window.close();") #Fecha aba aberta
    driver.switch_to.window(driver.window_handles[0])
    return email
    """
    config = open("config.txt", "r")
    content = config.readlines()
    config.close()

def return_cfg(cfg):
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

def output(Type, String, Timestamp = True, Center = False):

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
    else:
        print(output(Warn, "Pulando limpeza dos dados de navegação..."))

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
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

clear_browser()    

driver.get("https://patrickhlauke.github.io/recaptcha/")