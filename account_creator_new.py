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

def get_time(): #Pega o timestamp pelo horário atual.
    now = datetime.now()
    return "[ " + now.strftime("%H:%M:%S") + " ] "

def output(Type, String, Timestamp = True, Center = False):

    #Cores do console
    cBlack = fg(0) #Preto
    cError = fg(1) #Vermelho
    cMessage = fg(84) #Verde
    cWarning = fg(3) #Amarelho
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


cmd = 'mode 75,50'
clear = lambda: os.system('cls')
os.system(cmd)

#Fake enum:
Error = "error"
Message = "message"
Warn = "warn"
Black = "black"

#Inicio do programa
print(output(Message, "[ AlienWorlds Account Creator v0.1 ]", False, True))

PATH='D:\GitHub\Alienw_account_creator\essentials\chromedriver.exe'
path = 'D:\GitHub\Alienw_account_creator\essentials\Anticaptcha-plugin_v0.53'
options = webdriver.ChromeOptions() 
options.add_argument(f"--load-extension={path}")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox-explicit.php")
