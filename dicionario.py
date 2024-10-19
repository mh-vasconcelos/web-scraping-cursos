from imports import *
from main_ws import *

# CONCEITOS INICIAIS

# 0 - Passamos o link da página e fazemos a requisição
link = "https://www.datascienceacademy.com.br/todoscursosdsa"
req = requests.get(link)
print(req.text)

# 1 - site = bs(requisicao, tipo da requisição)
#            bs(em formato de texto html, req.text, nome 'html.parser' indicando que é um arquivo html)
site = bs(req.text, 'html.parser') 



# 2 - print(site.prettify())
#     print(site(de um jeito mais bonito e visual()))
print(site.prettify())

# 3 - site.encontre(entrada de dados)
titulo = site.find("title")
print(titulo)
div = site.find("div")
print(div)
input = site.find("input")
print(input)

# 4 - site.encontre(todas entradas de dados na página) retorna uma lista bs4
input_all = site.find_all("input")
print(input_all)



# DICIONÁRIO DE VARIÁVEIS

cursos 
# está no arquivo imports e significa apenas a parte do código HTML que contém 

dados
# Dados de nome do curso e preço zipados, após pegarmos do site

classe_curso
# classe específica que nos dá o código que possui o nome de cada curso

classe_preco 
# Nos dá todo o código que tem como informações os preços e suas diferentes estruturas no produto

classe_promocional 
# classe específica na parte dos preços que nos dá se a condição de curso com promoção foi atendida

classe_ch
# classe específica da carga horária dos cursos

precos_div
# É todo o código que contém os elementos dos preços, seja promocional, gratuito ou não.








