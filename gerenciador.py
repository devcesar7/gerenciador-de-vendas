import os  # Importa a biblioteca para interagir com o sistema operacional
import pandas as pd  # Importa a biblioteca para manipulação de dados
import plotly.express as px  # Importa a biblioteca para criar gráficos interativos

# Exibe um cabeçalho informativo no console
print("****************************************")
print("** Gerenciador de Vendas e Devoluções **")
print("****************************************")

# Define o caminho da pasta onde estão os arquivos de vendas
local_da_pasta = r"C:/Users/User/Documents/Programação/gerenciador-de-vendas/Vendas"

# Lista todos os arquivos dentro da pasta especificada
lista_de_arquivos = os.listdir(local_da_pasta)

# Cria um DataFrame vazio para armazenar todas as vendas
tabela_total = pd.DataFrame()

# Percorre todos os arquivos na pasta
for arquivos in lista_de_arquivos:
    # Verifica se o nome do arquivo contém a palavra "Vendas"
    if "Vendas" in arquivos:
        # Lê o arquivo CSV e adiciona os dados ao DataFrame
        tabela = pd.read_csv(f"{local_da_pasta}/{arquivos}")
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)  # Concatena os dados

# Agrupa os produtos e soma os valores das colunas numéricas (exemplo: quantidade vendida)
tabela_de_produtos = tabela_total.groupby("Produto").sum()

# Ordena os produtos pela quantidade vendida em ordem decrescente
tabela_de_produtos_quantidade = tabela_de_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)

# Calcula o faturamento total de cada venda (quantidade vendida * preço unitário)
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]

# Agrupa os produtos novamente, agora considerando o faturamento total
tabela_faturamento = tabela_total.groupby("Produto").sum()

# Ordena os produtos pelo faturamento em ordem decrescente
tabela_de_produtos_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

# Agrupa as vendas por loja e soma os valores das colunas numéricas (como faturamento)
tabela_lojas = tabela_total.groupby("Loja").sum()

# Ordena as lojas pelo faturamento em ordem decrescente
tabela_lojas_mais_vendidas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

# Exibe os relatórios no console
print("===================== VENDAS =====================")
print(tabela_de_produtos_quantidade)  # Exibe os produtos mais vendidos
print("==================================================")
print(tabela_de_produtos_faturamento)  # Exibe os produtos que geraram mais faturamento
print("==================================================")
print(tabela_lojas_mais_vendidas)  # Exibe as lojas que mais faturaram
print("==================================================")

# Cria um gráfico de barras mostrando o faturamento por loja
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento", title="Faturamento por Loja")

# Exibe o gráfico
grafico.show()
