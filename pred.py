import nerpare
import pickle
import json
import argparse
import re
from tqdm import tqdm

if __name__ == '__main__':
    txt = \
'''
　 　 　　　＿＿＿_ 
　 　　　／⌒　　⌒＼ 
　　　／（ ●） 　（●）＼ 
　 ／::::::⌒（__人__）⌒::::: ＼ 　　だからニュー速でやるお! 
　 |　　　　　|r┬-|　　　　　| 
　 ＼ 　　 　 `ー'´ 　 　 ／
'''
    features = nerpare.make_x(txt)
    model = pickle.load(open('model/model_full.pickle', 'rb'))
    pred = model.predict([features])

    print(pred[0])
