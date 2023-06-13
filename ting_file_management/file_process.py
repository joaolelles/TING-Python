import ting_file_management.file_management
import sys


def process(path_file, instance):
    if path_file not in instance._data:
        instance.enqueue(path_file)
        file_management = ting_file_management.file_management.txt_importer(
            path_file
        )
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_management),
            "linhas_do_arquivo": file_management,
        }
        print(result)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        remove = instance.dequeue()
        print(f"Arquivo {remove} removido com sucesso")


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        file_management = ting_file_management.file_management.txt_importer(
            path_file
        )
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_management),
            "linhas_do_arquivo": file_management,
        }
        print(result)
    except IndexError:
        sys.stderr.write("Posição inválida")
