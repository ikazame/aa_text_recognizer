import nerpare

def test_seq2features():
    word_seq = ['パリ', 'パリ', 'に', '行く', '行く']
    postag_seq = ['名詞', '名詞', '助詞', '動詞', '動詞']
    char_seq = ['パ', 'リ', 'に', '行', 'く']
    chtype_seq = ['KATAK', 'KATAK', 'HIRAG', 'OTHER', 'HIRAG']
    features = nerpare.seq2features(word=word_seq, postag=postag_seq, char=char_seq, chtype=chtype_seq)
    assert features[2] == {
        '-2:char': 'パ',
        '-2:chtype': 'KATAK',
        '-2:postag': '名詞',
        '-2:word': 'パリ',
        '-1:char': 'リ',
        '-1:chtype': 'KATAK',
        '-1:postag': '名詞',
        '-1:word': 'パリ',
        '0:char': 'に',
        '0:chtype': 'HIRAG',
        '0:postag': '助詞',
        '0:word': 'に',
        '1:char': '行',
        '1:chtype': 'OTHER',
        '1:postag': '動詞',
        '1:word': '行く',
        '2:char': 'く',
        '2:chtype': 'HIRAG',
        '2:postag': '動詞',
        '2:word': '行く'}

def test_make_x():
    txt = 'パリに行く'
    word_seq, postag_seq = nerpare.make_word_postag_seq(txt) 
    assert word_seq == ['パリ', 'に', '行く']
    assert postag_seq == ['名詞', '助詞', '動詞']
    char_seq = nerpare.make_char_seq(word_seq)
    assert char_seq == ['パ', 'リ', 'に', '行', 'く']
    chtype_seq = nerpare.make_chtype_seq(char_seq)
    assert chtype_seq == ['KATAK', 'KATAK', 'HIRAG', 'OTHER', 'HIRAG']

    # charベースでやる場合
    word_seq, postag_seq = nerpare.flatten_cseq(word_seq, postag_seq)
    assert word_seq ==  ['パリ', 'パリ', 'に', '行く', '行く']
    assert postag_seq == ['名詞', '名詞', '助詞', '動詞', '動詞']