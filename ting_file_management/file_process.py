import ting_file_management.file_management


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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
