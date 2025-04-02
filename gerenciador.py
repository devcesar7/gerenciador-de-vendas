import os
import pandas as pd
import plotly.express as px

print("****************************************")
print("** Gerenciador de Vendas e Devoluções **")
print("****************************************")

local_da_pasta = r"C:/Users/User/Documents/Programação/gerenciador-de-vendas-e-devolucoes/Vendas"
lista_de_arquivos = os.listdir(local_da_pasta)
tabela_total = pd.DataFrame()

for arquivos in lista_de_arquivos:
    if "Vendas" in arquivos:
        tabela = pd.read_csv(f"{local_da_pasta}/{arquivos}")
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

tabela_de_produtos = tabela_total.groupby("Produto").sum()

tabela_de_produtos_quantidade = tabela_de_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]

tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_de_produtos_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

tabela_lojas = tabela_total.groupby("Loja").sum()

tabela_lojas_mais_vendidas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

print("===================== VENDAS =====================")
print(tabela_de_produtos_quantidade)
print("==================================================")
print(tabela_de_produtos_faturamento)
print("==================================================")
print(tabela_lojas_mais_vendidas)
print("==================================================")

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento", title="Faturamento por Loja")
grafico.show()