#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


print(black_friday.shape)
black_friday.head()


# In[4]:


black_friday[black_friday["Gender"]=="F"].Age.value_counts()


# In[5]:


black_friday["User_ID"].nunique()


# In[6]:


black_friday.info()


# In[7]:


a = black_friday.isna().sum()
a[a!=0].count()/a.count()


# In[30]:


(black_friday.shape[0]-black_friday.dropna().shape[0])/black_friday.shape[0]


# In[9]:


black_friday.Product_Category_3.value_counts(dropna=False)


# In[10]:


minimo = black_friday.Purchase.min()
maximo = black_friday.Purchase.max()
print("Minimo:",minimo,"\nMaximo:",maximo)


# In[11]:


black_friday["Purchase_Norm"] = ((black_friday.Purchase-minimo)/
                                 (maximo-minimo))


# In[12]:


black_friday["Purchase_Norm"].mean()


# In[13]:


mean = black_friday["Purchase"].mean()
std = black_friday["Purchase"].std()
print("Média:",mean,"\nDesvio Padrão:",std)


# In[14]:


black_friday["Purchase_Padron"] = (black_friday.Purchase-mean)/std


# In[15]:


black_friday.Purchase_Padron[(black_friday.Purchase_Padron>=-1) & (black_friday.Purchase_Padron<=1)].count()


# In[16]:


df_null = black_friday[["Product_Category_2","Product_Category_3"]].isna()


# In[17]:


df_null = df_null[df_null["Product_Category_2"]==True]


# In[18]:


df_null["Product_Category_2"].equals(df_null["Product_Category_3"])


# In[19]:


for x in df_null[["Product_Category_2","Product_Category_3"]]:
    print(x)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[20]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return (537577, 12)


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[21]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return 49348


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[22]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return 5891


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[23]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return 3


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[24]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return 0.6944102891306734


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[25]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return 373299


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[26]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return 16.0


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[27]:


def q8():
    # Retorne aqui o resultado da questão 8.
    return 0.3847939036269795


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[28]:


def q9():
    # Retorne aqui o resultado da questão 9.
    return 348631


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[29]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return True

