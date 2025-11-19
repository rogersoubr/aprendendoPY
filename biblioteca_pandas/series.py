import pandas as pd #coloca pd como nome da lib pandas
print('MOSTRANDO SERIES')
serie_com_nomes = pd.Series({1:"um", 2:"dois", 3:"tres", 4:"quatro", 5:"cinco"})
print(serie_com_nomes.loc[1])
print(serie_com_nomes[1])
#vai mostrar o "um"
print('*'*30)
serie = pd.Series(
    {
        "a": 0, "b": 10, "c": 20, "d": 30, "e": 40, "f": 50, "g": 60, "h": 70, "i": 80, "j": 90, "k": 100, "l": 110, "m": 120, "n": 130, "o": 140, "p": 150, "q": 160, "r": 170, "s": 180, "t": 190, "u": 200, "v": 210, "w": 220, "x": 230, "y": 240, "z": 250
    }
)

print(serie.loc['j'])#acessa dado que tem o index j
print(serie['j'])
print(serie.iloc[5])
print('*'*30)
print(serie.iloc[0:10])
print(serie.iloc[[0, 2, 4, 6, 8]])

print('\nALTERANDO SERIES')
serie.loc['b'] = 'letra b'
serie['j'] = 'letra j'
serie.iloc[15] = 'letra p'
print(serie)