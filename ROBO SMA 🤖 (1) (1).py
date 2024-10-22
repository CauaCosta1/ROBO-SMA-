#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Importar bibliotecas
import time
import chromedriver_autoinstaller
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instala o ChromeDriver automaticamente
chromedriver_autoinstaller.install()

# Configurar o WebDriver do Chrome
driver = webdriver.Chrome()

# Navegar para o Google
driver.get("https://www.google.com/")
print('MAPS')
time.sleep(5)

# Configurar seletores
time.sleep(5)

# segmento = input('Qual é o segmento? ')
# localizacao = input('Qual é o localização? ')

# busca = segmento + " " +  localizacao
# busca

# pesquisar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')))
# pesquisar.send_keys(busca,Keys.ENTER)
# print('\nPesquisando no Google Maps: ',busca)

time.sleep(5)

mais_lugares = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div[12]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/g-more-link/a/div')))
mais_lugares.click()
time.sleep(5)

colunas = ['Nome do estabelecimento','Endereço','Telefone']
df = pd.DataFrame(columns=colunas)

qtd_pag = 0
for i in range(2, 11):
    try:
        time.sleep(2)
        paginas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[{}]'.format(i))))
        paginas = paginas.get_attribute('outerHTML')
        qtd_pag = i
    except:
        pass

pag_atual = 1
print('\nTotal de paginas: ', qtd_pag)

while qtd_pag > pag_atual:
    print('\nPagina Atual: ', pag_atual)
    i = 0
    for i in range(4, 43, 2):
        try:
            nome_estabelecimento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]/div[{}]/div[2]/div/div/a[1]/div/div/div[1]/span'.format(i))))
            nome_estabelecimento.click()
            nome_estabelecimento = nome_estabelecimento.text
            print('\nEstabelecimento: ', nome_estabelecimento)
            time.sleep(5)
        except:
            pass
        try:
            nome_estabelecimento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[{}]/div[3]/div/div/a/div/div/div[1]/span'.format(i))))
            nome_estabelecimento.click()
            nome_estabelecimento = nome_estabelecimento.text
            print('\nEstabelecimento: ', nome_estabelecimento)
            time.sleep(5)
        except:
            pass
        try:
            nome_estabelecimento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[{}]/div/div/div/a/div/div/div[1]/span'.format(i))))
            nome_estabelecimento.click()
            nome_estabelecimento = nome_estabelecimento.text
            print('\nEstabelecimento: ', nome_estabelecimento)
            time.sleep(5)
        except:
            pass

        endereco = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'LrzXr')))
        print('Endereço:', endereco.get_attribute('outerHTML')[20:-7])

        try:
            telefone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'kno-fv')))
            tell = telefone.get_attribute('outerHTML')
            print('Telefone:', tell.split()[14][-4:16]+' '+tell.split()[14][-0:10])
        except:
            print('Telefone: Não localizado')

        df = df.append({'Nome do estabelecimento': nome_estabelecimento,
                        'Endereço': endereco.get_attribute('outerHTML')[20:-7],
                        'Telefone': tell.split()[14][-4:16]+' '+tell.split()[14][-0:10]}, ignore_index=True)

        time.sleep(3)

    try:
        proxima = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[12]/a/span[2]')))
        proxima.click()
    except:
        pass
    try:
        proxima = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[12]/a/span[1]')))
        proxima.click()
    except:
        pass
    try:
        proxima = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr/td[8]/a/span[2]')))
        proxima.click()
    except:
        pass
    try:
        proxima = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pnnext"]/span[2]')))
        proxima.click()
    except:
        pass

    pag_atual += 1


# In[ ]:




