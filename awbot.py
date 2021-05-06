from selenium import webdriver

PROXY = "88.157.149.250:8080" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://google.com")