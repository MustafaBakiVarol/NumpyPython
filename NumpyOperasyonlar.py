#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


benimDizim = np.arange(0,15)


# In[4]:


benimDizim


# In[5]:


benimDizim[5] ## indeks alma.


# In[7]:


benimDizim[3:5]


# In[13]:


benimDizim[3:8] = -5 
## yeni degerler atadım. 


# In[14]:


benimDizim


# In[15]:


baskaDizi = np.arange(0,24)


# In[16]:


baskaDizi


# In[17]:


slicingDizi = baskaDizi[4:9]
## belirli konumdan yeni bir dizi olusturur.


# In[19]:


slicingDizi


# In[20]:


baskaDizi 
##baska dizide degisiklik olmaz. 


# In[23]:


slicingDizi[:] = 700
slicingDizi
## butun elemanlar 700 olur.


# In[24]:


baskaDizi
## Baska dizi icindeki degerler de 700 diye degisir.
## Bir parcayi alip isleyip degisiklik yaparsak eger ana dizide degisiklik yapar.
## Peki ana dizi degismesin istiyorsam ne yapmam lazim. 


# In[25]:


ornekDizi = np.arange(0,24)


# In[26]:


ornekDizi


# In[27]:


ornekDiziKopyasi = ornekDizi.copy()
## Ana dizi degismesin istiyorsam eger kopyalamam lazım. 


# In[28]:


ornekDiziKopyasi


# In[29]:


ornekDizi


# In[32]:


ornekDiziKopyasiSlicing = ornekDiziKopyasi[3:6]


# In[33]:


ornekDiziKopyasiSlicing[:] = 800


# In[34]:


ornekDiziKopyasiSlicing


# In[35]:


ornekDiziKopyasi


# In[36]:


ornekDizi
## ornek dizide bir degisiklik yok. Kopya olusturup calistirmak daha mantikli.


# ## Matris

# In[37]:


benimListem = [[10,20,30] , [20,30,40] , [30,40,50] , [40,50,60]]


# In[38]:


benimMatrisDizim = np.array(benimListem)


# In[39]:


benimMatrisDizim


# In[42]:


benimMatrisDizim[0]


# In[44]:


benimMatrisDizim[1][2]


# In[45]:


benimMatrisDizim[1,2] 


# In[48]:


benimMatrisDizim[1:,2]
## 1. satır başından 2. indekse kadar olan elemanları getir.


# In[52]:


benimMatrisDizim[2:,0]


# In[53]:


yeniListe = [[0,1,2,3,4] , [5,6,7,8,9] , [10,11,12,13,14] , [15,16,17,18,19,] , [20,21,22,23,24]]


# In[54]:


yeniMatris = np.array(yeniListe)


# In[55]:


yeniMatris


# In[57]:


yeniMatris[[4,2,0]] 
## indeks yerine ayrı bir liste veriyorsun sana dizi olusturuyor. Basit.


# ## Operasyonlar

# In[72]:


yeniBirDizi = np.random.randint(1,100,20)


# In[73]:


yeniBirDizi


# In[74]:


yeniBirDiziMatrisi = yeniBirDizi.reshape(4,5)


# In[75]:


yeniBirDiziMatrisi


# In[77]:


yeniBirDiziMatrisi > 24


# In[76]:


sonucDizisi = yeniBirDizi > 24


# In[78]:


sonucDizisi.reshape(5,4)


# In[79]:


yeniBirDizi


# In[81]:


yeniBirDizi[sonucDizisi] 
## Nolacak , true deger verenleri teker teker yazdıracak.


# In[82]:


yeniBirDizi[yeniBirDizi > 24]


# In[83]:


sonDizi = np.arange(0,24)


# In[84]:


sonDizi


# In[86]:


sonDizi + sonDizi
## Ne oldu , elemanlar kendisi ile toplandı. Adet olarak değil değer olarak degistiler.


# In[87]:


sonDizi * sonDizi


# In[88]:


sonDizi - sonDizi


# In[89]:


np.sqrt(sonDizi)
## kok alındı. 


# In[ ]:




