#!/usr/bin/env python
# coding: utf-8

# In[29]:


from selenium import webdriver
from selenium.webdriver.common.by import By
navegador = webdriver.Chrome()
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element(By.XPATH, '//*[@id="slick-slide10"]/div/div/div/div/div/div/a').click()
navegador.find_element(By.XPATH, '//*[@id="ContentInternal_ContentPlaceHolderConteudo_rptResultados_linkArq_Release3T_0"]/img').click()


# In[ ]:





# In[ ]:





# In[25]:





# In[ ]:




