def txt_importer(path_file):
    text_list = []
    with open(path_file, "r") as text:
        text_read = text.read()
        for line in text_read.split('\n'):
            text_list.append(line)
    return text_list
