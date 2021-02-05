import sys
from os import path
from ting_file_management.file_management import txt_importer


def process(class_deque, path_file):
    exist = path.exists(path_file) or path.exists(f"./{path_file}")

    if not exist:
        print(f"Arquivo {path_file} não existe", file=sys.stderr)
        return
    if not path_file.endswith(".txt"):
        print("Formato Inválido", file=sys.stderr)
        return

    text_read = txt_importer(path_file)

    if class_deque.file_name(path_file):
        print(f"Arquivo {path_file} já incluso", file=sys.stderr)
        return
    list_text = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_read),
        "linhas_do_arquivo": text_read,
    }
    class_deque.push_back(list_text)
    print(list_text)
    return


def remove(class_deque):
    if len(class_deque) == 0:
        print("Não há arquivos a serem removidos", file=sys.stderr)
        return
    arquivo = class_deque.pop_front()
    print(f"Arquivo {arquivo['nome_do_arquivo']} removido com sucesso")
    return


def file_metadata(class_deque, position):
    arquivo = class_deque.peek_any(position)
    if arquivo == "Posição Inválida":
        print("Posição Inválida", file=sys.stderr)
        return
    print(arquivo)
    return
