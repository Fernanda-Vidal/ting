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


def remove(instance: Queue):
    if not instance or instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    remove = instance.dequeue()['nome_do_arquivo']
    return sys.stdout.write(f"Arquivo {remove} removido com sucesso\n")


def file_metadata(instance: Queue, position):
    try:
        file = instance.search(position)
        return sys.stdout.write(str(file))
    except IndexError:
        print("Posição inválida\n", file=sys.stderr)
