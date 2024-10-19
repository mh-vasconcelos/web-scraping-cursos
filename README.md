# web-scraping-cursos
Um webscraping básico dos cursos do site da Data Science Academy usando Beautiful Soup.
Este projeto realiza a extração de dados sobre cursos de um site educacional, coletando informações como nome dos cursos, carga horária e preços. Os dados extraídos são organizados em um DataFrame e salvos em um arquivo CSV para análise posterior.


## Descrição dos Arquivos

### `imports.py`
Contém variáveis e classes que são usadas em outros scripts. Este arquivo serve para centralizar as configurações e evitar poluição do código principal.

### `main_ws.py`
O script principal que realiza o web scraping. Ele:

- Faz a requisição ao site.
- Extrai o nome dos cursos, carga horária e preços.
- Organiza os dados em um DataFrame.
- Salva os dados em um arquivo CSV (`cursos.csv`).

### `dicionario.py`
Um script que define conceitos iniciais do web scraping e um dicionário de variáveis que são usadas para melhor entendimento do código.

### `tratamento.ipynb`
Um Jupyter Notebook onde os dados extraídos são tratados e analisados.

### cursos.csv
O DataFrame inicial bruto, sem ajustes

### cursos_ajustado.csv
O DataFrame depois de passar pelo tratamento no notebook Jupyter
