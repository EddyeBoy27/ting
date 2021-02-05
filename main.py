from src.deque import Deque
from ting_file_management.file_process import process, remove, file_metadata
from ting_word_searches.word_search import search_by_word, exist_word

ting = Deque()

process(ting, "./statics/arquivo_teste.txt")
process(ting, "./statics/teste2")
process(ting, "./statics/teste2.txt")
process(ting, "./statics/testando_3.txt")
remove(ting)
file_metadata(ting, 0)
search_by_word(ting, "lado")
exist_word(ting, "comprometimento")
