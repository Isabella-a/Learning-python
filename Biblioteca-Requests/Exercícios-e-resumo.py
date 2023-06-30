import requests
from parsel import Selector

# Requisição do tipo GET
# response = requests.get("https://www.betrybe.com/")
# código de status
# print(response.status_code)
# conteúdo no formato html
# print(response.headers["Content-Type"])

# Conteúdo recebido da requisição
# print(response.text)

# Bytes recebidos como resposta
# print(response.content)

# Requisição do tipo post
# response = requests.post("http://httpbin.org/post", data="some content")
# print(response.text)

# Requisição enviando cabeçalho (header)
# response = requests.get("http://httpbin.org/get", headers={"Accept": "application/json"})
# print(response.text)

# Requisição a recurso binário
# response = requests.get("http://cloudflare.com")
# print(response.content)

# Recurso JSON
# response = requests.get("http://httpbin.org/get")
# Equivalente ao json.loads(response.content)
# print(response.json())

"""Para realizar a extração de dados de um conteúdo web vamos utilizar uma biblioteca chamada parsel. Ela pode ser 
instalada com o seguinte comando abaixo:

python3 -m pip install parsel """

response = requests.get("http://books.toscrape.com/")
selector = Selector(text=response.text)
# print(selector)

# Extraia todos os livros desta primeira página e busque seus títulos e preços:

# Dentro de um h3 em elementos que possuem classe product_pod
# a::attr(title) -- captura somente o valor contido no texto do seletor
# titles = selector.css(".product_pod h3 a::attr(title)").getall()
# prices = selector.css(".product_price .price_color::text").getall()
# print(titles, prices)

# for product in selector.css('.product_pod'):
#     title = product.css('h3 a::attr(title)').get()
#     price = product.css('.price_color::text').get()
#     print(price, title)

# Buscando em todas as páginas:
URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'
while next_page_url:
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").get()
        print(title, price)
    next_page_url = selector.css(".next a::attr(href)").get()
