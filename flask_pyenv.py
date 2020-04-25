これをしてやらないと、flask動かない。開かない
firewall-cmd --zone=public --add-port=5000/tcp --permanent
5000のポートを開放する
firewall-cmd --reload
firewall-cmd --list-all


pip3 install pipenv
$pipenv install


pipenv shell
pipenv shellをしても実行できないとき
pipenv shellをしてもShell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.と

いうメッセージが出てきて実行できないとき
pipenv shellで仮想環境を立ち上げたときは、最後にexitでサブシェル自体も終了させ

るのをお忘れなきよう。


#ソースコード
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'これはmypjフォルダ内'

if __name__ == '__main__':    
	app.run(debug=False, host="192.168.179.5") 


http://192.168.179.5:5000/hello
にアクセスしてやると開く

どこのフォルダ下に置いてもいいぽい
前提条件として
pipenvをインストールした仮想環境内でflaskのインストールしとかなくてはいけない

<!------------------------------------->
https://tekunabe.hatenablog.jp/entry/2018/12/28/pyenv_pipenv
前提条件
pip の準備
curl https://bootstrap.pypa.io/get-pip.py | sudo python
確認
pip --version

pyenv の準備
pyenv のインストールには git が必要なため予めインストールします
yum install git

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init 

-)"\nfi' >> ~/.bash_profile
$ exec "$SHELL" -l
確認
$ pyenv --version
$ pyenv install --list
その他必要なパッケージインストール
$ sudo yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite 

sqlite-devel openssl-devel tk-devel libffi-devel



pipenv の準備
インストール
$ sudo pip install pipenv

$ pipenv --version 3.6.7


■ 仮想環境の作成
準備ができたので、特定の Python のバージョンとパッケージをインストールした仮想

環境を作ってみます。

プロジェクトディレクトリの作成
mkdir mypj
cd mypj

使用する Python バージョンの選択
今回は、 3.6.7 を指定します。
$ pipenv --python 3.6.7


パッケージの追加
ここでは、netmiko というネットワーク機器を操作するパッケージをインストールして

みます。
$ pipenv install netmiko


作成された仮想環境に入る
先ほどと同じく、Pipfile たちがあるディレクトリで、 pipenv shell コマンドを実行

すると、仮想環境に入れます。
$ pipenv shell

(mypj) $ python --version

仮想環境から抜けるために deactivate コマンドを実行します。
(mypj) $ deactivate


(おまけ)コピペ用
「環境の準備」の一連のコマンドをコピペだけで実行できるようにしたものです。

# pip
curl https://bootstrap.pypa.io/get-pip.py | sudo python

# git
sudo yum -y install git

# pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init 

-)"\nfi' >> ~/.bash_profile
exec "$SHELL" -l
sudo yum -y install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite 

sqlite-devel openssl-devel tk-devel libffi-devel

# pipenv
sudo pip install pipenv


pip install -U simplejson
pip install -U flask


Flask のバージョン確認
python -c "import flask; print( flask.__version__ )"



