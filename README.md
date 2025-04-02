# Gerenciador de Vendas

## 📌 Descrição
Este projeto é um Gerenciador de **Vendas e Devoluções desenvolvido em Python.** Ele analisa e organiza os dados de vendas armazenados em arquivos CSV, gerando relatórios e gráficos para auxiliar na tomada de decisão.Este projeto é um Gerenciador de Vendas e Devoluções desenvolvido em Python. Ele analisa e organiza os dados de vendas armazenados em arquivos CSV, gerando relatórios e gráficos para auxiliar na tomada de decisão.

## 🚀 Funcionalidades
**Leitura de arquivos CSV** com dados de vendas.
**Agrupamento e soma de dados** por produto e loja.
**Cálculo do faturamento** por produto e loja.
**Geração de relatórios** de produtos mais vendidos e lojas com maior faturamento.
**Criação de um gráfico** interativo para visualização do faturamento por loja.

## 🛠️ Tecnologias Utilizadas
**Python**
**Pandas** (para manipulação de dados)
**Plotly** (para visualização de dados)
**OS** (para manipulação de arquivos)

## 📂 Estrutura do Projeto
   ```sh
  Gerenciador-Vendas-Devolucoes/
  │-- Vendas/  # Pasta contendo os arquivos CSV das vendas
  │   ├── Vendas_Janeiro.csv
  │   ├── Vendas_Fevereiro.csv
  │   ├── ...
  │-- gerenciador.py  # Script principal do projeto
  │-- README.md  # Documentação do projeto
   ```

## ▶️ Como Executar o Projeto
**Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/gerenciador-de-vendas.git
   ```
**Acesse a pasta do projeto:**
   ```sh
   cd gerenciador-de-vendas
   ```
**Instale as dependências:**
   ```sh
   pip install pandas plotly
   ```
**Execute o script:**
   ```sh
   python gerenciador.py
   ```

## 📊 Exemplo de Saída
   ```sh
   ****************************************
   ** Gerenciador de Vendas e Devoluções **
   ****************************************
   ===================== VENDAS =====================
                   Quantidade Vendida
   Produto                                 
   Produto A                 500
   Produto B                 320
   Produto C                 150
   ==================================================
                   Faturamento
   Produto                                
   Produto A            15000.00
   Produto B             9600.00
   Produto C             4500.00
   ==================================================
                   Faturamento
   Loja                                   
   Loja X             20000.00
   Loja Y             12000.00
   Loja Z              7000.00
   ==================================================
   ```
