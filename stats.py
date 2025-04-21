def get_num_words(text):
    num_words = text.split()
    print("----------- Word Count ----------")
    print(f"Found {len(num_words)} total words")

def character_count(text):
    dict = {}
    new_text = text.lower()
    for char in new_text:
        if (char not in dict) and char.isalpha():
            x = new_text.count(char)
            dict[char] = x
        else: 
            pass
    return dict

def sort_on(dict):
    return dict["num"]

def sort_list(dict):
    print("--------- Character Count -------")
    new = []
    for char in dict:
        new.append({"char": char, "num": dict[char]})
    new.sort(reverse=True, key=sort_on)
    key = "char"
    count = "num"
    for i in new:
        print(f"{i[key]}: {i[count]}")