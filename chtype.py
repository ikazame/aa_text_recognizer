def is_hiragana(ch):
    return 0x3040 <= ord(ch) <= 0x309F

def is_katakana(ch):
    return 0x30A0 <= ord(ch) <= 0x30FF

def get_character_type(ch):
    if ch.isspace():
        return 'ZSPACE'
    elif ch.isdigit():
        return 'ZDIGIT'
    elif ch.islower():
        return 'ZLLET'
    elif ch.isupper():
        return 'ZULET'
    elif is_hiragana(ch):
        return 'HIRAG'
    elif is_katakana(ch):
        return 'KATAK'
    else:
        return 'OTHER'

def get_chtype(string):
    character_types = map(get_character_type, string)
    character_types_str = '-'.join(sorted(set(character_types)))

    return character_types_str

def get_word_type(word):
    chtypes = [get_character_type(char) for char in word]
    chtype = chtypes[0] 
    if all([ct == chtype for ct in chtypes]):
        return chtype
    else:
        return 'MIX'

if __name__ == '__main__':
    print(get_chtype('記事'))
    print(get_chtype('カ'))
    print(get_word_type('記事'))
    print(get_word_type('カ'))