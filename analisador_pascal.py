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
nome_arquivo = "input.p"
codigo_entrada = open("lib/input/" + nome_arquivo, "r", encoding="utf8").read()


# %%
print(codigo_entrada)

# %% [markdown]
# ## Definição de DataFrame resultante

# %%
rows = []
df = pd.DataFrame(rows, columns=["Tipo", "Palavra", "Linha", "Posicao_Inicio", "Posicao_Fim"])
df


# %%
def procurar_palavras(row, tipo, lista_palavras = ["entrada"]):
    for idx, palavra in enumerate(lista_palavras):
        if tipo in ["operadores","pontuação"]:
            regex = rf"(?<!:){re.escape(palavra)}(?!=)"
        elif tipo in ["inteiro"]:
            regex = r"[-+]?(?<!\w)(?<![\d.])\d+(?![\d.])"
        elif tipo in ["real"]:
            regex = r"[-+]?[0-9]*(\.[0-9]+)"
        else:
            regex = rf"(?i)\b{re.escape(palavra)}\b"

        matches = re.finditer(regex, codigo_entrada, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            
            line = codigo_entrada[0:match.end()].count('\n') + 1   
            rows.append([tipo, match.group(), line, match.start(), match.end()])
    
    return rows

# %% [markdown]
# ## Procurar Palavras Reservadas no Código

# %%
palavra_procurada = pd.read_csv("lib/model/palavras_reservadas.csv", header=None)
palavra_procurada = list(palavra_procurada[0])
tipo = "palavra reservada"


# %%
rows = procurar_palavras(rows, tipo, palavra_procurada)

# %% [markdown]
# ## Procurar Variáveis no Código

# %%
palavra_procurada = pd.read_csv("lib/model/variaveis.csv", header=None)
palavra_procurada = list(palavra_procurada[0])
tipo = "variável"


# %%
rows = procurar_palavras(rows, tipo, palavra_procurada)

# %% [markdown]
# ## Procurar Operadores no Código

# %%
palavra_procurada = pd.read_csv("lib/model/operadores.csv", header=None)
palavra_procurada = list(palavra_procurada[0])
tipo = "operadores"


# %%
rows = procurar_palavras(rows, tipo, palavra_procurada)

# %% [markdown]
# ## Procurar Pontuação no Código

# %%
palavra_procurada = pd.read_csv("lib/model/pontuacoes.csv", header=None)
palavra_procurada = list(palavra_procurada[0])
tipo = "pontuação"


# %%
rows = procurar_palavras(rows, tipo, palavra_procurada)

# %% [markdown]
# ## Procurar Números Inteiros no Código

# %%
tipo = "inteiro"


# %%
rows = procurar_palavras(rows, tipo)

# %% [markdown]
# ## Procurar Números Decimais no Código

# %%
tipo = "real"


# %%
rows = procurar_palavras(rows, tipo)

# %% [markdown]
# ## DataFrame resultante

# %%
df = pd.DataFrame(rows, columns=["Tipo", "Palavra", "Linha", "Posicao_Inicio", "Posicao_Fim"])


# %%
df = df.sort_values(by=['Posicao_Inicio']).reset_index(drop=True)

# %% [markdown]
# ## Adicionar Coluna Quantidade_Por_Tipo

# %%
df["Quantidade"] = df.index + 1
df["Quantidade_Por_Tipo"] = ""


# %%
for tipo in df["Tipo"].unique():
    lista_indices = df[df["Tipo"]==tipo].index
    for idx, row in enumerate(lista_indices, start = 1):
        df.loc[row,'Quantidade_Por_Tipo'] = str(idx).zfill(2) + "/" + str(df.loc[row,'Quantidade']).zfill(2)
    

# %% [markdown]
# ## Preparar DataFrames

# %%
total_linhas = df["Linha"].max()
total_tokens = df["Quantidade"].max()


# %%
## Isolando colunas desejadas

df = df[['Tipo','Palavra','Linha','Quantidade_Por_Tipo']]


# %%
## Renomeando colunas

df = df.rename(columns = {
    'Tipo' : 'Classe'
    , 'Palavra' : 'token'
    , 'Linha' : 'linha'
    , 'Quantidade_Por_Tipo' : 'quantidade (1ª coluna(qtdade da classe), 2ª qtdade de tokens)'
    })


# %%
df


# %%
df_agrupado = df.groupby(by = 'Classe').size().reset_index(name='quantidade')


# %%
df_agrupado.loc[len(df_agrupado)] = ["Total linhas", total_linhas]
df_agrupado.loc[len(df_agrupado)] = ["Total tokens", total_tokens]


# %%
df_agrupado

# %% [markdown]
# ## Arquivo de Saída

# %%
nome_arquivo_saida = f'output/{nome_arquivo}.csv'
df.to_csv(nome_arquivo_saida)


# %%
print(df.to_markdown(index = False, tablefmt="fancy_grid"))


# %%
print(df_agrupado.to_markdown(index = False, tablefmt="fancy_grid"))


# %%



