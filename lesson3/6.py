# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()

def conv2(word: str):
    little_char_list = list(range('a', 'z'))
    tile_char_list = list(range('A', 'Z'))
    symbol_position = little_char_list.index(word[0])
    result = tile_char_list[symbol_position]+word[1:]
    return result

def conv(word: str):
    first_ch = word[0]
    code_firs_char = ord(first_ch)-32
    convert_char = chr(code_firs_char)
    return convert_char+word[1:]

def conver_words(words: str):
    final_word_list = ''
    for word in words.split():
        final_word_list = final_word_list + conv(word) + ' '
    return final_word_list

words_list = input('Введите набор латинских слов разделенных пробелом:')
print (conver_words(words_list))
