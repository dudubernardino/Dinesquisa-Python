import Algorithmia

arquivo = open('resumo.txt', 'w')

def pesquisar(input):
    client = Algorithmia.client('simFhhDQMeECjRN/U9nagwtA5hy1')
    algo = client.algo('web/WikipediaParser/0.1.2?')
    algo.set_options(timeout=300)
    return algo.pipe(input).result

def resumir(input):
    client = Algorithmia.client('simFhhDQMeECjRN/U9nagwtA5hy1')
    algo = client.algo('nlp/Summarizer/0.1.8')
    algo.set_options(timeout=300)
    return algo.pipe(input).result


input = {
    "articleName": 'JavaScript',
    "lang": 'pt'
}
dados = pesquisar(input)
title = dados.get('title')
texto = dados.get('content')
url = dados.get('url')
referencias = dados.get('references')
resumo = resumir(texto)

arquivo.write(title+"\n\n")
arquivo.write("Resumo: \n")
arquivo.write(resumo.encode("utf-8"))
arquivo.write("\n\nUrl: ")
arquivo.write(url)


