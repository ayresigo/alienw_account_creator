from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium.webdriver.common.action_chains import ActionChains
from colored import fg, bg, attr
from datetime import datetime

import unidecode
import unicodedata
import time
import string
import random

def get_time(): #Pega o timestamp pelo horário atual.
    now = datetime.now()
    return "[ " + now.strftime("%H:%M:%S") + " ] "

def get_random_email(): #Gera email aleatório com o <head> do wikipedia.

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

def get_random_password(): #Gera senha aleatória.
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
    print(cMessage+get_time()+"Senha "+cGreenBg+cBlack+password+cReset+cMessage+" gerada com sucesso.")
    return password

"""
def set_account_txt():
    accounts_ = open("accounts.txt", "r")
    accounts_content = accounts_.read()
    email_ = get_random_email()+"@yopmail.com"
    password_ = get_random_password()
    accounts_ = open("accounts.txt", "w")
    accounts_.write(accounts_content+email_+"\n"+password_+"\n----\n")
    accounts_.close()

def get_email(accountNumber):
    accounts_ = open("accounts.txt", "r")
    accounts = accounts_.readlines()
    count = 0

    for line in accounts:
        count += 1
        if((accountNumber*3)-2 == count):
            getEmail = line.strip()

    accounts_.close()    
    return getEmail
"""

def solve_captcha(url, _site_key, _api_key): #Codigo dado pela anti-captcha.
    api_key = _api_key
    site_key = _site_key  

    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)

    job = client.createTask(task)

    print(cMessage+get_time()+"Aguardando resolução do captcha...")
    job.join()
    # Receive response
    response = job.get_solution_response()
    print(cMessage+get_time()+"Captcha resolvido!")
    # Inject response in webpage
    driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % response)
    # Wait a moment to execute the script (just in case).
    time.sleep(1) 

def confirm_email(_api_key, yopmail): #Confirma email na yopmail.

    yopmail_site_key = '6LcG5v8SAAAAAOdAn2iqMEQTdVyX8t0w9T3cpdN2'
    yopmail_url = "http://www.yopmail.com/en/"
    anticaptcha_key = _api_key

    driver.execute_script("window.open();") #Abre nova aba
    driver.switch_to.window(driver.window_handles[1])

    print(cMessage+get_time()+"Abrindo yopmail...")
    driver.get(yopmail_url)

    print(cMessage+get_time()+"Logando na conta "+yopmail)
    yopLogin = driver.find_element_by_id('login')
    yopLogin.click()
    yopLogin.send_keys(yopmail)
    yopLogin.submit()

    print(cGreenBg+cBlack+"\n## CAPTCHA YOPMAIL ##"+cReset+"\n"+cMessage)
    solve_captcha(yopmail_url, yopmail_site_key, anticaptcha_key)
    print("breakpoint 1")
    time.sleep(2)
    
    yopLogin = driver.find_element_by_id('login')
    yopLogin.click()
    yopLogin.submit()
    print("breakpoint 2")

    print(cMessage+get_time()+"Ativando conta da wax...")
    try:
        activateAccount = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mailmillieu"]/div[2]/table/tbody/tr/td/table/tbody/tr[4]/td/table[1]/tbody/tr[2]/td[2]/a')))
        activateAccount.click()
        driver.execute_script("window.close();")
    except:
        print(cError+get_time()+"Botão de confirmação não encontrado."+cReset)

def delete_cache(): #Limpa a cache do navegador ao abri-lo.
    
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back

def wax_login(_email, _password, _api_key): #Faz o login na página da wax.

    wax_email = _email
    wax_pw = _password
    api_key = _api_key

    print(cMessage+get_time()+"Abrindo wallet.wax.io...")
    driver.get("https://wallet.wax.io")
    #driver.switch_to.window(driver.window_handles[0])
    #driver.execute_script("window.close();")

    time.sleep(5)
    print(cMessage+get_time()+"Logando pelo reddit...")
    redditButton = driver.find_element_by_xpath('//*[@id="reddit-social-btn"]')
    driver.execute_script('arguments[0].click()', redditButton)

    current_url = driver.current_url
    try:
        current_url.index("reddit.com/login")
    except ValueError:
        print(cMessage+get_time()+"Pulando inserção de login/senha reddit...")
    else:
        print(cMessage+get_time()+"Inserindo username: "+wax_email)
        redditLogin = driver.find_element_by_id('loginUsername')
        redditLogin.send_keys(wax_email)
        print(cMessage+get_time()+"Inserindo senha: "+wax_pw)
        redditPassword = driver.find_element_by_id('loginPassword')
        redditPassword.send_keys(wax_pw)
        print(cMessage+get_time()+"Logando...")
        redditPassword.submit()

    time.sleep(2)    
    #allowButton = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div/input[1]')
    #allowButton.click()

    try:
        print(cMessage+get_time()+"Autorizando nova conta...")
        allowButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/form/div/input[1]')))
        allowButton.click()
    except TimeoutError:
        print ("Botão de autorização não encontrado")

    time.sleep(5)
    print(cMessage+get_time()+"Confirmando email na wax...")
    waxEmail = driver.find_element_by_name('email')
    waxEmail.send_keys(wax_email+"@yopmail.com")
    waxEmail.submit()

    print(cMessage+get_time()+"Confirmando email na yopmail... ("+wax_email+"@yopmail.com)")
    confirm_email(api_key, wax_email)
    #driver.execute_script("window.close();")
    #driver.switch_to.window(driver.window_handles[0])

def create_account(_api_key): #Inicia o processo de criação de conta (reddit - wax - reddit - wax - yopmail - wax).

    reddit_url = "https://old.reddit.com/register"
    reddit_site_key = '6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC'
    api_key = _api_key

    try: #Limpa cookies e cache
        print(cMessage+get_time()+"Limpando Cookies...")
        driver.delete_all_cookies()
        print(cMessage+get_time()+"Limpando Cache...")
        delete_cache()
    except:
        print(cError+get_time()+"Não foi possível limpar cookies e cache..."+cReset)
        return

    try: #Gera novo email (get_random_email())
        print(cMessage+get_time()+"Gerando novo email/username...")
        email = get_random_email()
    except:
        print(cError+get_time()+"Não foi possivel gerar novo email/username..."+cReset)
        return

    try: #Gera nova senha (get_random_password())
        print(cMessage+get_time()+"Gerando nova senha...")
        password = get_random_password()
    except:
        print(cError+get_time()+"Não foi possivel gerar senha..."+cReset)
        return

    driver.get(reddit_url)

    try: #(reddit) Insere username
        print(cMessage+get_time()+"Inserindo username...")
        user_reg = driver.find_element_by_id('user_reg')
        user_reg.click()
        user_reg.send_keys(email)
    except:
        print(cError+get_time()+"Não foi possivel inserir o username..."+cReset)
        return

    try: #(reddit) Insere senha
        print(cMessage+get_time()+"Inserindo senha...")
        passwd_reg = driver.find_element_by_id('passwd_reg')
        passwd_reg.click()
        passwd_reg.send_keys(password)
    except:
        print(cError+get_time()+"Não foi possivel inserir a senha..."+cReset)
        return

    try: #(reddit) Insere confirmação de senha
        print(cMessage+get_time()+"Confirmando senha...")
        passwd2_reg = driver.find_element_by_id('passwd2_reg')
        passwd2_reg.click()
        passwd2_reg.send_keys(password)
    except:
        print(cError+get_time()+"Não foi possivel confirmar a senha..."+cReset)
        return
        
    try: #(reddit) Insere email
        print(cMessage+get_time()+"Inserindo email...")
        email_reg = driver.find_element_by_id('email_reg')
        email_reg.click()
        email_reg.send_keys(email+"@yopmail.com")
    except:
        print(cError+get_time()+"Não foi possivel inserir o email..."+cReset)
        return

    ## TROCAR O EXCEPT

    captcha_retry = True
    while(captcha_retry):
        try: #(reddit) Resolve captcha (solve_captcha())
            captcha_retry = False
            print(cGreenBg+cBlack+"\n## CAPTCHA REDDIT ##"+cReset+"\n"+cMessage)
            solve_captcha(reddit_url, reddit_site_key, api_key)
        except:
            print(cError+get_time()+"Não foi possivel realizar o captcha... Tentando novamente..."+cReset)
            captcha_retry = True

    try:
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/form/div[8]/button').click()
    except:
        print(cError+get_time()+"Botão de sign up não encontrado."+cReset)

    time.sleep(5)

    try:
        rateLimitString = driver.find_element_by_class_name("RATELIMIT").text
    except:
        (cMessage+get_time()+"Confirmando conta nova.")
    else:

        #TODO: RETRY

        print(cError+get_time()+rateLimitString)
        print(cError+get_time()+"Ratelimit!"+cReset)
        return 

    #try: #(wax) Realiza login na wax
    print(cMessage+get_time()+"Logando na wax...")
    wax_login(email, password, api_key)
    #except:
    #    print(cError+get_time()+"Não foi possivel realizar o login na wax...")
    #    return



#Cores do console
cBlack = fg(0) #Preto
cError = fg(1) #Vermelho
cMessage = fg(2) #Verde
cWarning = fg(3) #Amarelho
cGreenBg = bg(2) #Fundo verde
cReset = attr('reset') #Reset

#Inicio do programa
print(cMessage+"[ Alien Worlds Bot v0.1 !]")

try: #Testa se existe um config.txt na pasta
    config = open('config.txt', 'r')
except:
    print(cError+get_time()+"Arquivo config.txt não localizado.")
    config.close()
else: #Testa se o "PATH=" está presente no config.txt
    _PATH = config.readline()
    if(_PATH[:6] != "PATH='"): #Testa se tem algum endereço no "PATH="
        print(cError+get_time()+"Arquivo config não está configurado corretamente."+cReset)
        config.close()
    else: 
        PATH=_PATH[6:-2]
        try: #Verifica e inicia o chromedriver.exe
            options = webdriver.ChromeOptions() 
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver = webdriver.Chrome(options=options, executable_path=PATH)
        except: #TODO: Diferenciar o não localizado do erro ao iniciar
            print(cError+get_time()+"chromedriver.exe não localizado no endereço informado"+cReset)
            config.close()
        else: 
            print(cMessage+get_time()+"chromedriver.exe localizado e iniciado.")
            _api_key_ = config.readline()
            if(_api_key_[:9] != "api_key='"): #Testa a presença do "api_key dentro do config.txt"
                print(cError+get_time()+"Arquivo config não está configurado corretamente."+cReset)
                config.close()
            else: #Inicia a criação de conta.
                api_key = _api_key_[9:-1]
                config.close()
                create_account(api_key)

#_PATH = _PATH[6:-2]
#create_account()

#raise AnticaptchaException(python_anticaptcha.exceptions.AnticaptchaException: [ERROR_NO_SLOT_AVAILABLE:2]No idle workers are available at the moment. Please try a bit later or increase your maximum bid in menu Settings - API Setup in Anti-Captcha Customers Area.