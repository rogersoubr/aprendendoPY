import pandas as pd #coloca pd como nome da lib pandas
nome = pd.Series(['Kalebe','Heitor','Miguel','Jhuan','Bruno'])
idade = pd.Series([18,16,17,15,15])
peso = pd.Series([70,55.3,73.8,65,60.5])

df = pd.DataFrame ({'Sujeito':nome, 'Idade':idade, 'Peso':peso})#constroi uma atabela 
print(df)
df