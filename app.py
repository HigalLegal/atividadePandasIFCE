import pandas as pd

# Questão 2: Extensões dos arquivos: .csv

# Questão 3: Músicas mais ouvidas por banda, estilo etc.

# Questão 4 e 5: Carregando os dados do arquivo e pegando número de linhas e colunas de cada.

alternativeMusicData = pd.read_csv("alternative_music_data.csv")
bluesMusicData = pd.read_csv("blues_music_data.csv")
hiphopMusicData = pd.read_csv("hiphop_music_data.csv")


linhas = alternativeMusicData.shape[0]
colunas = alternativeMusicData.shape[1]

print("Alternative Music Data || Linhas: " +
      str(linhas) + " || Colunas: " + str(colunas))

linhas = bluesMusicData.shape[0]
colunas = bluesMusicData.shape[1]

print("Blues Music Data || Linhas: " +
      str(linhas) + " || Colunas: " + str(colunas))

linhas = hiphopMusicData.shape[0]
colunas = hiphopMusicData.shape[1]

print("HipHop Music Data || Linhas: " +
      str(linhas) + " || Colunas: " + str(colunas))

# Questão 6: Pegando nome das colunas.

nomeColunas = alternativeMusicData.columns.to_list

print("Colunas de Alternative Music Data:")
print(nomeColunas)

nomeColunas = bluesMusicData.columns.to_list

print("Colunas de Blues Music Data:")
print(nomeColunas)

nomeColunas = hiphopMusicData.columns.to_list

print("Colunas de HipHop Music Data:")
print(nomeColunas)

# Questão 7: Pegando os tipos de dados das colunas.

print("Tipo de dado das colunas")
print(alternativeMusicData.info())

# Questão 8: Inserindo uma coluna nova em alternativeMusicData apenas com valores 1 inteiro.

alternativeMusicData2 = alternativeMusicData.assign(numero=1)
print(alternativeMusicData2.columns.tolist)

# Questão 9: Inserindo uma coluna nova em bluesMusicData apenas com valores 2 inteiro.

bluesMusicData2 = bluesMusicData.assign(numero=2)
print(bluesMusicData2.columns.tolist)

# Questão 10: Inserindo uma coluna nova em bluesMusicData apenas com valores 3 inteiro.

hiphopMusicData2 = hiphopMusicData.assign(numero=3)
print(hiphopMusicData2.columns.tolist)

# Questão 11: Fazendo a junção dos 3 novos arquivos de forma vertical.

musicData = pd.concat(
    [alternativeMusicData2, bluesMusicData2, hiphopMusicData2], axis=0)
print(musicData)

# Questão 12: Verificando se há valores nulos e a quantidade linhas.

print("Há valores nulos? " + str(musicData.isnull().values.any()))

# Questão 13: Não há valores nulos.

# Questão 14: Excluindo colunas com valores string.

colunasString = list(musicData.select_dtypes(include = "object").columns.tolist())

print("Colunas string: " + str(colunasString))

print("Excluindo colunas com valores string:")

musicData.drop(colunasString, axis = 1, inplace = True)

print(musicData)