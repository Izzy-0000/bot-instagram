from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import re
import requests

url = 'https://www.instagram.com/'

br = Firefox()

br.get(url)
print('https://www.instagram.com/ OK!')
sleep(3)

# Captura elemntos de login e senha
email_camp = br.find_element_by_name('username')
pass_camp = br.find_element_by_name('password')

# Faz o login
email_camp.send_keys('my-email')
pass_camp.send_keys('my-password')

pass_camp.submit()
print('Login OK!')
sleep(5)

# Vai para a página onde a mensagem será enviada
br.get('https://www.instagram.com/jairmessiasbolsonaro/')
print('https://www.instagram.com/jairmessiasbolsonaro/ OK!')
sleep(5)

# Clica no botão de mensagem
br.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/div/button').click()
print('Click message OK!')
sleep(5)

# Escreve a mensagem 
br.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys('Boa Tarde!')
sleep(1)

# Envia a mensagem
br.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(Keys.RETURN)
print('Mensagem enviada com sucesso!')
