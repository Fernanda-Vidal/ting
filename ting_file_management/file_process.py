from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    for item in range(len(instance)):
        if instance.search(item)['nome_do_arquivo'] == path_file:
            return None
    txt = txt_importer(path_file=path_file)
    dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt),
        'linhas_do_arquivo': txt,
    }
    instance.enqueue(dict)
    return sys.stdout.write(str(dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
