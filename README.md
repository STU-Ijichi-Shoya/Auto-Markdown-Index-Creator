# Auto MarkDown Index Creator

自動でマークダウンから目次を付加します．  
<!-- INDEX SCENE -->

- [install](#INDEX-install0)
- [How to Use](#INDEX-HowtoUse1)
- [option](#INDEX-option2)
  - [Attention](#INDEX-Attention3)

<!-- INDEX SCENE END -->

<a id="INDEX-install0" name="install"></a>

## install

```bash
git clone 
```

<a id="INDEX-HowtoUse1" name="How to Use"></a>

## How to Use

1. 目次を入れたいmarkdownを開く．
1. commandを実行

```python
python mdex.py
```

目次は，タイトル（heading）から自動で取得し，idを生成，`a`タグに関連づけられます．  

<a id="INDEX-option2" name="option"></a>

## option

- ディレクトリ再帰モード(`-d`,`--inputDirctory`)

    指定のディレクトリ下にあるmarkdownファイルを再帰的にすべて処理します．

- ファイル指定モード (`-i`,`--inputFile`)

    指定のファイルのみを処理します．

<a id="INDEX-Attention3" name="Attention"></a>

### Attention

同時に`-d`と`-i`を指定した場合，`-d`を優先します．
