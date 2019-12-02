import MeCab
import chtype
import re
from enum import Enum
m = MeCab.Tagger('-d /usr/lib/mecab/dic/unidic --node-format %M\\t%f[0],%f[1],%f[2],%f[3],%f[4],%f[5],%f[6],%f[7],%f[8]\\n --unk-format %M\\t%f[0],%f[1],%f[2],%f[3],%f[4],%f[5]\\n')

def seq2features(**kwargs):
    sent_features = []
    beos_flag = ['BOS', 'BOS+1', '', 'EOS-1', 'EOS']
    length = len(kwargs[list(kwargs.keys())[0]])

    for i in range(length):
        features = {}
        for pos in range(-2, +3):
            if i+pos in range(0, length):
                row = {key:kwargs[key][i+pos] for key in kwargs}
                features.update({str(pos) + ':' + key: value for key, value in row.items()})
            else:
                features.update({beos_flag[pos+2]: '1'})
        sent_features.append(features)
    return sent_features

def make_word_postag_seq(txt):
    word_seq, postag_seq = [], []

    result = m.parse(txt).split('\n')[:-2]

    for line in result:
        surface_info = line.split('\t')
        word = surface_info[0]
        if word == '':
            word, postag = '\n', 'newline'
        else:
            # postag = surface_info[1].split(',')[0]
            postag = surface_info[4].split('-')[0]

        word_seq += [word]
        postag_seq += [postag]

    return word_seq, postag_seq

def make_char_seq(word_seq):
    # return sum([[char for char in word] for word in word_seq], [])
    return list(''.join(word_seq))

def make_chtype_seq(char_seq):
    return [chtype.get_character_type(char) for char in char_seq]

def flatten_cseq(word_seq, *seqs):
    flat_seqs = []

    for feats in zip(word_seq, *seqs):
        for char in feats[0]:
            flat_seqs += [[*feats]]
    return list(map(list, zip(*flat_seqs))) # 転置

def format_txt(txt):
    txt = txt.replace(' ', '　') # ^[SP]\n$の半角スペースをMeCabは無視する仕様．全角スペースは必ず認識するので力技
    # txt = re.sub('\n+$', '', txt) # テキスト最後の改行の連続はどうあがいてもMeCabに無視される．なのでここで消す
    txt = txt.replace('\n', '⏎') # テキスト最後の改行の連続はMeCabに無視される．なので全ての改行文字を記号に変える
    return txt

def make_x(txt):
    txt = format_txt(txt)
    word_seq, postag_seq = make_word_postag_seq(txt) 
    char_seq = make_char_seq(word_seq)
    chtype_seq = make_chtype_seq(char_seq)

    # charベースに変換
    word_seq, postag_seq = flatten_cseq(word_seq, postag_seq)
    features = seq2features(word=word_seq, postag=postag_seq, char=char_seq, chtype=chtype_seq)
    return features

class LabelGranularity(Enum):
    TEXT_AA = 1
    SERIFU_JINOBUN_AA = 2
    ALL = 3

text_aa_dic = {
    'O':'O',
    'AA':'AA',
    'Serifu':'Text',
    'Jinobun':'Text',
    'Gion':'AA',
    'Hidden_Text':'Text',
    'Res_Header':'Text',
    'Scene_Description':'Text',
    'Text_in_AA':'AA',
    'Textbox':'AA',
}
serifu_jinobun_aa_dic = {
    'O':'O',
    'AA':'AA',
    'Serifu':'Serifu',
    'Jinobun':'Jinobun',
    'Gion':'AA',
    'Hidden_Text':'Jinobun',
    'Res_Header':'Jinobun',
    'Scene_Description':'Jinobun',
    'Text_in_AA':'AA',
    'Textbox':'AA',
}

def encoarse_label(label, level):
    if level == LabelGranularity.TEXT_AA:
        return text_aa_dic[label]
    elif level == LabelGranularity.SERIFU_JINOBUN_AA:
        return serifu_jinobun_aa_dic[label]
    else:
        return label

def encoarse_label_seq(label_seq, level):
    return list(map(lambda label: encoarse_label(label, level), label_seq))

if __name__ == '__main__':
    pass

    # $ python -m pytest
