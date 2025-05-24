def get_word_count(text_string):
    count = len(text_string.split())
    return count

def get_char_counts(text_string):
    char_dict = {}
    for i in range(0,len(text_string)):
        char = text_string[i].lower()
        #check if character is an alphabetical char
        #if not, ignore it and got to next entry
        if not char.isalpha():
            continue
        #check if character is already logged
        #if not, add initialize it to dict
        if not char in char_dict:
            char_dict[char] = 0
        #increase count by 1
        char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict_list(dict_list):
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def get_char_dicts(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        new_dict = {"char":key, "num":value}
        dict_list.append(new_dict)
    sort_dict_list(dict_list)
    if __name__ == '__main__':
        print(dict_list)
    return dict_list    

if __name__ == '__main__':
    a = get_char_counts("Hello World!@%")
    b = get_char_dicts(a)
    c = sort_dict_list(b)
    print(c)