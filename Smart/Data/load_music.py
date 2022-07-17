
#credentials
username = str(input('email:    '))
password = str(input('password:    '))

#driver = webdriver.Chrome("edgedriver")

#Ids of the elements to be clicked
enter_user_id = "account_name_text_field"
push_user_id = "sign-in"

import os
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
print(os.getcwd())
driver_path = os.path.join(os.getcwd() + '\msedgedriver.exe')
print(str(driver_path))
service = Service(driver_path)
options = Options()
options.add_argument(f'user_agent={user_agent}')
options.add_argument('--diasble-gpu-sandbox')
#options.add_argument('user-data-dir=C:/Users/Mrsno/AppData/Local/Microsoft/Edge/User data 2')
#options.add_argument('profile-directory=Profile 3')
#options.add_argument('start-fullscreen')
options.add_argument('kiosk')
options.add_argument('window-position=-2000,0')
options.add_argument('enable-force-dark')
browser = webdriver.Edge(service=service, options=options)


'''browser.get('https://microsoft.com/')
print(browser.find_element_by_id("shellmenu_4-mo"))'''

browser.get('https://music.apple.com/login')
#browser.get("https://www.stealmylogin.com/demo.html")
''
WebDriverWait(driver=browser, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
''
'''
element = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "account_name_text_field"))
    )

'''
#Login form is contained within an iphrame and loading into the iframe takes a while?
frame_0 = browser.find_element_by_id('aid-auth-widget-iFrame')
browser.switch_to.frame('frame_0')

#browser.find_element_by_id("account_name_text_field").click
browser.find_element_by_id("account_name_text_field").send_keys(username)
sleep(2)
#browser.find_element_by_id("password").send_keys(password)

browser.find_element_by_id("sign-in").click()

for i in range(0, 30):
    sleep(1)
    