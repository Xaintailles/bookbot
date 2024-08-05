def main():

    file_path = f"./books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)

        print(f"--- Begin report of {file_path} ---")
            
        print(f"The book contains {word_count} words")

        all_characters_count = count_lower_characters(file_contents)

        list_all_characters_count = []

        for key, value in all_characters_count.items():
            list_all_characters_count.append({"letter":key, "num": value})

        list_all_characters_count.sort(reverse=True, key=sort_on)

        for i in list_all_characters_count:
            print(f"The \'{i['letter']}\' character was found {i['num']} times")
    
def count_words(string_to_count: str) -> int:
    all_words = string_to_count.split()
    return(len(all_words))

def count_lower_characters(string_to_count: str):
    cleaned_string = string_to_count.lower()
    all_letters = sorted(list(set([*cleaned_string])))

    return_dict = {}

    for letter in all_letters:
        if letter.isalpha():
            return_dict[letter] = cleaned_string.count(letter)

    return(return_dict)

def sort_on(dict):
    return dict["num"]

main()