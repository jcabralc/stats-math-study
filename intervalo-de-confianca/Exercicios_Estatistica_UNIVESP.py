# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:30:15 2019

@author: Jessica Cabral
"""

## Exercicios Sobre Intervalo de Confiança

### Video com Explicação: https://www.youtube.com/watch?v=unNyFOmbovo

### Caso 1 - Notas da Prova

#A nota média numa determinada prova de estatistica é tal que seu desvio padrão é conhecido e igual a
#5.0 pontos

#Uma amostra de 100 provas realizadas pelos alunos foi selecionada aleatoriamente e obteve-se nota média amostral
#de 7.0 pontos

#Deseja-se construir um intervalo de confiança para a verdadeira nota média desta prova com nivel de 95% de confiança

from scipy.stats import sem, t
from scipy import mean
import scipy.stats as stats
import math

confidence = 0.95

sample_size = 100
sample_mean = 7
pop_stdev = 5

# Let's calculate a 95% confidence 
z_critical = stats.norm.ppf(q = 0.975)  # Get the z-critical value*
#*Note: We use stats.norm.ppf(q = 0.975) to get the desired z-critical value instead 
# of q = 0.95 because the distribution has two tails.

print("z-critical value:")              # Check the z-critical value
print(z_critical)                        

margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  

print("Confidence interval:")
print(confidence_interval)