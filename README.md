# AA・テキスト領域検出器
本アプリケーションは入力文書からAA領域とテキスト領域を自動的に認識する識別機です．  
機械学習アルゴリズム（条件付き確率場）を用いて領域認識を実現しています．  
各スクリプトは以下の意味を持ちます

+ train.py: 教師データからモデルの訓練を行う
  + nerpare.py: 教師データの前処理を行う（素性テンプレート設計，窓幅の考慮等）
  + chtype.py: 文字種素性用のスクリプト [オリジナル](https://qiita.com/Hironsan/items/326b66711eb4196aa9d4)
+ pred.py: 学習したモデルから入力文書に対する予測を行う
+ aahtml.py: 入力テキストと予測されたラベル列からhtmlファイルを作成しビジュアライズする

train.py, pred.py, aahtml.pyはそれぞれ独立したスクリプトです．


## Usage
本アプリケーションは内部で形態素解析器MeCabを利用しています．別途MeCabをインストールしてからご利用ください．

UbuntuでのMeCabインストール例：
```bash
$ sudo apt install mecab libmecab-dev mecab-ipadic-utf8
```

ついで，pipを用いて依存パッケージのインストールを行います
```bash
$ pip3 install -r requirements.txt
```

最後にpred.pyを実行し，以下のような出力が出れば成功です
```bash
$ python3 pred.py
['AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'O', 'O', 'O', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'O', 'O', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA']
```

## Training
教師データの再学習はtrain.pyを用いて行えます．
教師データ自身はdataset/以下に置かれており，入力テキストのtxt/とラベル列のann/に分かれています．  
教師データの追加はdataset/内を参考にして行ってください．

再学習はtrain.pyのTEXT_SETを編集した上で以下のコマンドで実行します．
```
$ python3 train.py
```

## Visualize
結果の可視化はaahtml.pyを用いて行います．  
aahtml.pyはpred.pyで作成した予測結果を利用し，認識結果を可視化したhtmlを生成します．  
使い方はaahtml.pyの中身を見てみてください．

```
$ python3 aahtml.py
```

## 注意事項
model/以下にはmodel.pickleとmodel_full.pickleが存在します．前者はdataset/に付属された教師データで学習したモデルで，  
後者は更に大規模な教師データで学習したモデルです．  
特別な事情がない限りは後者を利用することをおすすめします．
