def exist_word(class_deque, word):
    dados = list(class_deque._data)
    result = []
    ocorrencias = []
    for arquivo in dados:
        for index, frase in enumerate(arquivo['linhas_do_arquivo']):
            if word.lower() in frase.lower():
                ocorrencias.append({
                    "linha": index,
                })
        if len(ocorrencias) > 0:
            result.append({
                "palavra": word,
                "arquivo": arquivo['nome_do_arquivo'],
                "ocorrencias": ocorrencias,
            })
            ocorrencias = []
    print(result)
    return result


def search_by_word(class_deque, word):
    dados = list(class_deque._data)
    result = []
    ocorrencias = []
    for arquivo in dados:
        for index, frase in enumerate(arquivo['linhas_do_arquivo']):
            if word.lower() in frase.lower():
                ocorrencias.append({
                    "linha": index,
                    "conteudo": frase,
                })
        if len(ocorrencias) > 0:
            result.append({
                "palavra": word,
                "arquivo": arquivo['nome_do_arquivo'],
                "ocorrencias": ocorrencias,
            })
            ocorrencias = []
    print(result)
    return result
