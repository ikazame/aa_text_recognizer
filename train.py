import nerpare 
import json
import pickle
from tqdm import tqdm
import sklearn_crfsuite
from nerpare import LabelGranularity as lg

if __name__ == '__main__':
    TEXT_SET = ['bank1', 'bank2', 'bank3', 'bank4', 'bank5', 'bank6', 'bank7', 'bank8'] 
    doc_set = []
    label_set = []
    features_set = []

    for filehead in tqdm(TEXT_SET):
        txt = ''.join(open('dataset/txt/' + filehead + '.txt').readlines())
        txt = nerpare.format_txt(txt)

        features = nerpare.make_x(txt)
        label_seq = json.load(open('dataset/ann/' + filehead + '.json'))['label_seq']
        # label_seq = nerpare.encoarse_label_seq(label_seq, lg.TEXT_AA) # テキスト，AA，その他に分類
        # label_seq = nerpare.encoarse_label_seq(label_seq, lg.SERIFU_JINOBUN_AA) # セリフ，地の文，AA，その他に分類

        if len(txt) != len(label_seq):
            print('{} {} {}'.format(filehead, len(txt), len(label_seq)))
            exit()
        doc_set.append([txt])
        label_set.append(label_seq)
        features_set.append(features)

    print('学習開始')
    # X_dev = [features_set.pop(0)]
    # y_dev = [label_set.pop(0)]
    X_dev = [features_set[0]]
    y_dev = [label_set[0]]
    model = sklearn_crfsuite.CRF(algorithm='lbfgs', c1=0.1, c2=0.1, max_iterations=100, all_possible_transitions=True, verbose=True) \
            .fit(features_set, label_set, X_dev=X_dev, y_dev=y_dev)

    pickle.dump(model, open('model/model.pickle', 'wb'))
