#!/usr/bin/env python
# coding: utf-8

# # Desafio 3
# 
# Neste desafio, iremos praticar nossos conhecimentos sobre distribuições de probabilidade. Para isso,
# dividiremos este desafio em duas partes:
#     
# 1. A primeira parte contará com 3 questões sobre um *data set* artificial com dados de uma amostra normal e
#     uma binomial.
# 2. A segunda parte será sobre a análise da distribuição de uma variável do _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2), contendo 2 questões.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


# In[2]:


#%matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# ## Parte 1

# ### _Setup_ da parte 1

# In[3]:


np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})


# ## Inicie sua análise a partir da parte 1 a partir daqui

# In[4]:


# Sua análise da parte 1 começa aqui.
print(dataframe.normal.describe(),"\n")
print(dataframe.binomial.describe())


# ## Questão 1
# 
# Qual a diferença entre os quartis (Q1, Q2 e Q3) das variáveis `normal` e `binomial` de `dataframe`? Responda como uma tupla de três elementos arredondados para três casas decimais.
# 
# Em outra palavras, sejam `q1_norm`, `q2_norm` e `q3_norm` os quantis da variável `normal` e `q1_binom`, `q2_binom` e `q3_binom` os quantis da variável `binom`, qual a diferença `(q1_norm - q1 binom, q2_norm - q2_binom, q3_norm - q3_binom)`?

# In[5]:


def q1():
    a=float(dataframe.normal.quantile(0.25)-dataframe.binomial.quantile(0.25))
    b=float(dataframe.normal.quantile(0.50)-dataframe.binomial.quantile(0.50))
    c=float(dataframe.normal.quantile(0.75)-dataframe.binomial.quantile(0.75))
    a=round(a,3)
    b=round(b,3)
    c=round(c,3)
    return (a,b,c)
    # Retorne aqui o resultado da questão 1.
q1()   


# Para refletir:
# 
# * Você esperava valores dessa magnitude?
# 
# * Você é capaz de explicar como distribuições aparentemente tão diferentes (discreta e contínua, por exemplo) conseguem dar esses valores?

# ## Questão 2
# 
# Considere o intervalo $[\bar{x} - s, \bar{x} + s]$, onde $\bar{x}$ é a média amostral e $s$ é o desvio padrão. Qual a probabilidade nesse intervalo, calculada pela função de distribuição acumulada empírica (CDF empírica) da variável `normal`? Responda como uma único escalar arredondado para três casas decimais.

# In[6]:


m=dataframe.normal.mean()
s=dataframe.normal.std()


# In[7]:


ecdf = ECDF(dataframe["normal"])


# In[8]:


ecdf(m+s)-ecdf(m-s)


# In[9]:


df = dataframe[(dataframe["normal"]<m+s) & (dataframe["normal"]>m-s)]


# In[10]:


print("CDF para [ẍ−𝑠,ẍ+𝑠]: ",len(df)/len(dataframe))


# In[11]:


def q2():
    media=dataframe.normal.mean()
    sd=dataframe.normal.std()
    
    x1=media-sd
    x2=media+sd
    
    f = ECDF(dataframe["normal"])
    
    cdf = f(x2)-f(x1)
    
    return round(float(cdf),3)
q2()


# Para refletir:
# 
# * Esse valor se aproxima do esperado teórico?
# * Experimente também para os intervalos $[\bar{x} - 2s, \bar{x} + 2s]$ e $[\bar{x} - 3s, \bar{x} + 3s]$.

# In[12]:


df = dataframe[(dataframe["normal"]<=m+s*2) & (dataframe["normal"]>=m-s*2)]
print("CDF para [ẍ−2𝑠,ẍ+2𝑠]: ",len(df)/len(dataframe))
df = dataframe[(dataframe["normal"]<=m+s*3) & (dataframe["normal"]>=m-s*3)]
print("CDF para [ẍ−3𝑠,ẍ+3𝑠]: ",len(df)/len(dataframe))


# ## Questão 3
# 
# Qual é a diferença entre as médias e as variâncias das variáveis `binomial` e `normal`? Responda como uma tupla de dois elementos arredondados para três casas decimais.
# 
# Em outras palavras, sejam `m_binom` e `v_binom` a média e a variância da variável `binomial`, e `m_norm` e `v_norm` a média e a variância da variável `normal`. Quais as diferenças `(m_binom - m_norm, v_binom - v_norm)`?

# In[13]:


m_binom=dataframe.binomial.mean()
v_binom=dataframe.binomial.var()
m_norm=dataframe.normal.mean()
v_norm=dataframe.normal.var()


# In[14]:


print("m_binom:",m_binom,"\nm_norm:\t",m_norm,"\nv_binom:",v_binom,"\nv_norm:\t",v_norm)


# In[15]:


print((m_binom-m_norm,v_binom-v_norm))


# In[16]:


print(v_binom)
print(dataframe.binomial.std()**2)


# In[17]:


def q3():
    m_binom=dataframe.binomial.mean()
    v_binom=dataframe.binomial.var()
    m_norm=dataframe.normal.mean()
    v_norm=dataframe.normal.var()
    x1=round(float(m_binom-m_norm),3)
    x2=round(float(v_binom-v_norm),3)
    return (float(x1),float(x2))
q3()


# Para refletir:
# 
# * Você esperava valore dessa magnitude?
# * Qual o efeito de aumentar ou diminuir $n$ (atualmente 100) na distribuição da variável `binomial`?

# In[18]:


pd.DataFrame(sct.binom.rvs(1000, 0.2, size=10000)).describe()


# ## Parte 2

# ### _Setup_ da parte 2

# In[19]:


stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)


# ## Inicie sua análise da parte 2 a partir daqui

# In[20]:


# Sua análise da parte 2 começa aqui.
stars


# ## Questão 4
# 
# Considerando a variável `mean_profile` de `stars`:
# 
# 1. Filtre apenas os valores de `mean_profile` onde `target == 0` (ou seja, onde a estrela não é um pulsar).
# 2. Padronize a variável `mean_profile` filtrada anteriormente para ter média 0 e variância 1.
# 
# Chamaremos a variável resultante de `false_pulsar_mean_profile_standardized`.
# 
# Encontre os quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função `norm.ppf()` disponível em `scipy.stats`.
# 
# Quais as probabilidade associadas a esses quantis utilizando a CDF empírica da variável `false_pulsar_mean_profile_standardized`? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[21]:


mean_profile = stars[stars["target"]==0]["mean_profile"]


# In[22]:


m=mean_profile.mean()
s=mean_profile.std()


# In[23]:


false_pulsar_mean_profile_standardized = (mean_profile-m)/s


# In[24]:


false_pulsar_mean_profile_standardized


# In[25]:


sct.norm.ppf(0.8)


# In[26]:


sct.norm.ppf(0.9)


# In[27]:


sct.norm.ppf(0.95)


# In[28]:


stars["false_pulsar_mean_profile_standardized"]=false_pulsar_mean_profile_standardized


# In[29]:


f = ECDF(false_pulsar_mean_profile_standardized)
q80 = sct.norm.ppf(0.8)
q90 = sct.norm.ppf(0.9)
q95 = sct.norm.ppf(0.95)
f([q80, q90, q95])


# In[30]:


def q4():
    f = ECDF(false_pulsar_mean_profile_standardized)
    q80 = sct.norm.ppf(0.8)
    q90 = sct.norm.ppf(0.9)
    q95 = sct.norm.ppf(0.95)
    return tuple(f([q80, q90, q95]).round(3))
q4()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?

# In[31]:


false_pulsar_mean_profile_standardized.hist(bins=40)


# ## Questão 5
# 
# Qual a diferença entre os quantis Q1, Q2 e Q3 de `false_pulsar_mean_profile_standardized` e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[33]:


def q5():
    f_m_s = stars["false_pulsar_mean_profile_standardized"].quantile([0.25,0.50,0.75])
    q1 = sct.norm.ppf(q = 0.25, loc = 0, scale = 1)
    q2 = sct.norm.ppf(q = 0.50, loc = 0, scale = 1)
    q3 = sct.norm.ppf(q = 0.75, loc = 0, scale = 1)
    n_q = (q1,q2,q3)
    
    return tuple((f_m_s-n_q).round(3))
q5()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?
# * Curiosidade: alguns testes de hipóteses sobre normalidade dos dados utilizam essa mesma abordagem.
