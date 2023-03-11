from sys import stderr


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print("Formato Inválido", file=stderr)

    try:
        with open(path_file, mode="r") as file:
            return file.read().split('\n')

    except FileNotFoundError:
        print(f"Arquivo{path_file} não encontrado", file=stderr)
