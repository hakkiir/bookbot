def get_book_text(path):
    with open(path) as p:
        return p.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    #.lower()
    chars = {}
    for c in text:
        lower = c.lower()
        if lower.isalpha():
            if lower in chars:
                chars[lower] += 1
            else:
                chars[lower] = 1
    return(chars)

def sort_on(d):
    return(d["num"])

def dict_to_sorted_list(dict):
    sorted_list = []
    for d in dict:
        sorted_list.append({"char": d, "num" :dict[d]})
    sorted_list.sort(reverse=True, key=sort_on)
    print(sorted_list)
    return sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_cnt = word_count(text)
    character_count = char_count(text)
    sorted_count = dict_to_sorted_list(character_count)

    print(f"--- Begin of report of {book_path} ---")
    print(f"{word_cnt} words found in the document")
    print()
    for i in sorted_count:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End report ---")

main()