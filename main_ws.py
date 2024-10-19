
from imports import *


# PROJETO


site = bs(cursos, 'html.parser') 

# PEGA O NOME DOS CURSOS

nomes = site.find_all("a", class_ = classe_curso)
nomes = [i.text.strip() for i in nomes]

# PEGA A CARGA HORÁRIA DOS CURSOS
ch = site.find_all("p", class_ = classe_ch)
ch = [i.text.strip() for i in ch]

# PEGA O PREÇO DOS CURSOS
# Aqui há uma certa dificuldade porque existem cursos gratuitos e outros promocionais. Então, faremos:

precos_div = site.find_all('div', class_=classe_preco)

precos = []
for div in precos_div:
    preco_promocional = div.find('span', class_=classe_promocional)
    
    if preco_promocional:
        precos.append(preco_promocional.text.strip())
    else:
        preco_nao_promocional = div.find('strong')
        if preco_nao_promocional:
            precos.append(preco_nao_promocional.text.strip())



dados = []
for nome, preco in zip(nomes, precos):
    dados.append({"Curso": nome, "Preço": preco})


# CRIANDO O DATAFRAME

df = pd.DataFrame(dados, columns=['Curso', 'Preço'])
df['Carga Horaria'] = ch
print(df.head())

df.to_csv('cursos.csv', index=False)

