import json  # json é um modulo que vem embutido, porém precisamos importá-lo


with open("pokemons.json") as file:
    # leitura do arquivo
    content = file.read()
    # o conteúdo é transformado em estrutura python equivalente, dicionário neste caso.
    pokemons = json.loads(content)["results"]

print(pokemons[0])

# A leitura pode ser feita diretamente do arquivo, utilizando o método load ao invés de loads.
# O loads carrega o JSON a partir de um texto e o load carrega o JSON a partir de um arquivo.
with open("pokemons.json") as file:
    pokemons = json.load(file)['results']

print(pokemons[0])

# Separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if 'Grass' in pokemon['type']
]

# Abre o arquivo para escrevermos apenas o pokemons do tipo grama
with open("grass_pokemons.json", "w") as file:
    json_to_write = json.dumps(
        grass_type_pokemons
    )  # conversão de Python para o formato json (str)
    file.write(json_to_write)

with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)

