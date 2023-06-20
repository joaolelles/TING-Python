def exists_word(word, instance):
    result = []
    new_word = word.lower()

    for i in range(len(instance)):
        file_info = instance.search(i)
        file_name = (
            file_info["file"] if isinstance(file_info, dict) else file_info
        )

        lines_with_word = []

        with open(file_name, "r") as file:
            for line_number, line in enumerate(file, start=1):
                if new_word in line.lower():
                    lines_with_word.append(line_number)

        if lines_with_word:
            result.append(
                {
                    "palavra": new_word,
                    "arquivo": file_name,
                    "ocorrencias": lines_with_word,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
