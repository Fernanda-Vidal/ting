from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    words_found = []
    for item in range(len(instance)):
        search_item = instance.search(item)
        occurr = []

        for it, line in enumerate(search_item['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurr.append({'linha': it + 1})

        if occurr:
            words_found.append({
                'palavra': word,
                'arquivo': search_item['nome_do_arquivo'],
                'ocorrencias': occurr
            })

    return words_found


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
