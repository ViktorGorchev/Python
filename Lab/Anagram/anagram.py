try:
    file_name = input() #'C:/Users/Admin/Desktop/PythonFiles/words.txt'
    input_word = input()

    def check_if_word_exists(word_from_file, word_input):
        if len(word_from_file) == len(word_input):
            if sorted(word_from_file) == sorted(word_input):
                return True
            else:
                return False

        else:
            return False


    words_list = []
    with open(file_name, encoding='utf-8') as file:
        for word_in_line in file:
            word_in_file = word_in_line.strip()

            if word_in_file == input_word:
                continue

            if check_if_word_exists(word_in_file, input_word):
                words_list.append(word_in_file)

    if len(words_list) > 0:
        words_list.sort()
        for input_word in words_list:
            print(input_word)
    else:
        print('NO ANAGRAMS')

except:
    print('INVALID INPUT')