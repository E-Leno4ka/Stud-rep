
def single_root_words(root_word, *other_words):
    same_words=[]
    for w in other_words:
        if root_word.lower() in w.lower():
            same_words.append(w)
        elif w.lower() in root_word.lower():
            same_words.append(w)
        else: continue
    return same_words

print(single_root_words('стол', 'Столешка', 'диван', 'стол-книжка', 'тумба'))