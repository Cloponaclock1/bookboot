


def main():
    file_to_read = "books/frankenstein.txt"



    def get_text(file):
        with open(file_to_read) as file:
            file_contents = file.read()
            return file_contents
      
    def get_words(file):
        words= file.split()
        return words
    






    def get_letters(word_list):
        letter_dict = {}
        sorted_dict = {}
        for word in word_list:
            for letter in word.lower():
                if letter not in letter_dict and letter.isalpha():
                    letter_dict[letter] = 1
                elif not letter.isalpha():
                    continue
                else:
                    letter_dict[letter]+=1
        sorted_dict  = dict(sorted(letter_dict.items()))
        return sorted_dict
    

    def report(file):
        data = get_text(file)
        words_list = get_words(data)
        print("---Begin report of "+file_to_read+" ---")
        print(f"{len(words_list)} words found in the document")

        letter_dict = get_letters(words_list)

        for letters in letter_dict:
            print(f"The {letters} character was found {letter_dict[letters]} times")
        print("--- End Report ---")

    report(file_to_read)


if __name__ == '__main__':
    main()
