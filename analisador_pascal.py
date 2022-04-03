# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import re


# %%
from tabulate import tabulate

# %% [markdown]
# ## Codigo de Entrada

# %%
nome_arquivo = "lights.p"
codigo_entrada = open("lib/" + nome_arquivo, "r", encoding="utf8").read()


# %%
print("Codigo de Entrada:\n")
print(codigo_entrada)

# %% [markdown]
# ## Definição de DataFrame resultante

# %%
rows = []
df = pd.DataFrame(rows, columns=["Tipo", "Palavra", "Linha", "Posicao_Inicio", "Posicao_Fim"])

df

# %% [markdown]
# ## Procurar Palavras Reservadas no Código

# %%
palavras_reservadas = pd.read_csv("lib/palavras_reservadas.csv", header=None)
palavras_reservadas = list(palavras_reservadas[0])


# %%
tipo = "Palavras Reservadas"


# %%
for idx, palavra in enumerate(palavras_reservadas):
    # print(f'id = {idx}, palavra = {palavra}')
    regex = rf"(?i){palavra}"

    matches = re.finditer(regex, codigo_entrada, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        
        line = codigo_entrada[0:match.end()].count('\n') + 1   
        rows.append([tipo, match.group(), line, match.start(), match.end()])

# %% [markdown]
# ## Procurar Símbolos no Código

# %%
simbolos = pd.read_csv("lib/simbolos.csv", delimiter=";", header = None)
simbolos = list(simbolos[0])


# %%
tipo = "Símbolos"


# %%
for idx, palavra in enumerate(simbolos):
    # print(f'id = {idx}, palavra = {palavra}')
    regex = rf"(?i){re.escape(palavra)}"

    try:
        matches = re.finditer(regex, codigo_entrada, re.MULTILINE)
    except:
        print(f'Não foi possível a palavra: {palavra}')

    for matchNum, match in enumerate(matches, start=1):
        
        line = codigo_entrada[0:match.end()].count('\n') + 1   
        rows.append([tipo, match.group(), line, match.start(), match.end()])

# %% [markdown]
# ## Procurar Variáveis no Código

# %%
tipo = "Variáveis"


# %%
# print(f'id = {idx}, palavra = {palavra}')
regex = rf"(?i).*:="

matches = re.finditer(regex, codigo_entrada, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    line = codigo_entrada[0:match.end()].count('\n') + 1 
    variable = match.group().split(":=")[0].split(" ")[-1]
    rows.append([tipo, variable, line, match.start(), match.end()])

# %% [markdown]
# ## Procurar Números Inteiros no Código

# %%
tipo = "Números Inteiros"


# %%
# print(f'id = {idx}, palavra = {palavra}')
regex = r"[-+]?(?<![\d.])\d+(?![\d.])"

matches = re.finditer(regex, codigo_entrada, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    line = codigo_entrada[0:match.end()].count('\n') + 1 
    variable = match.group()
    rows.append([tipo, variable, line, match.start(), match.end()])

# %% [markdown]
# ## Procurar Números Decimais no Código

# %%
tipo = "Números Decimais"


# %%
# print(f'id = {idx}, palavra = {palavra}')
regex = r"[-+]?[0-9]*(\.[0-9]+)"


matches = re.finditer(regex, codigo_entrada, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    line = codigo_entrada[0:match.end()].count('\n') + 1 
    variable = match.group()
    rows.append([tipo, variable, line, match.start(), match.end()])

# %% [markdown]
# ## DataFrame resultante

# %%
df = pd.DataFrame(rows, columns=["Tipo", "Palavra", "Linha", "Posicao_Inicio", "Posicao_Fim"])


# %%
df = df.sort_values(by=['Linha','Tipo']).reset_index(drop=True)

# %% [markdown]
# ## Adicionar Coluna Quantidade_Por_Tipo

# %%
df["Quantidade"] = df.index + 1
df["Quantidade_Por_Tipo"] = ""


# %%
for tipo in df["Tipo"].unique():
    lista_indices = df[df["Tipo"]==tipo].index
    for idx, row in enumerate(lista_indices, start = 1):
        df.loc[row,'Quantidade_Por_Tipo'] = str(idx) + "/" + str(df.loc[row,'Quantidade'])
    

# %% [markdown]
# ## Arquivo de Saída

# %%
nome_arquivo_saida = f'output/{nome_arquivo}.csv'
df.to_csv(nome_arquivo_saida)


# %%
df[df["Tipo"]=="Variáveis"]


# %%
df[df["Tipo"]=="Números Inteiros"]


# %%
print(df.to_markdown())


