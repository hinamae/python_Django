# README

## requirement

- Python 3.7.6 
- pip
- virtualenv
- virtualenvwrapper

```
Successfully installed appdirs-1.4.4 distlib-0.3.0 filelock-3.0.12 importlib-metadata-1.7.0 pbr-5.4.5 six-1.15.0 stevedore-2.0.1 virtualenv-20.0.25 virtualenv-clone-0.5.4 virtualenvwrapper-4.8.4 zipp-3.1.0
Successfully installed coverage-5.1 pytest-cov-2.10.0
Successfully installed pytest-filter-subpackage-0.1.1   
pytest-astropy
typed-ast
astroid
Successfully installed asgiref-3.2.10 django-3.0.2 pytz-2020.1 sqlparse-0.3.1
```

## 場所


## 参考

(https://qiita.com/kaki_k/items/e824cfcf089e75d43551)[https://qiita.com/kaki_k/items/e824cfcf089e75d43551]

## 参考URLから変えた部分

```.bashrc
export WORKON_HOME=$HOME/.virtualenvs
source /Users/hina/opt/anaconda3/bin/virtualenvwrapper.sh
```

- env1という環境を作成
```
mkvirtualenv --no-site-package --python /Users/hina/opt/anaconda3/lib/python3.7 env1
```

ターミナル 開き直した時には以下を叩く
```
 workon env1
```

- env1にインストールされたモジュールとバージョン
```
(env1) (base) HinaMaeamanoAir:~ hina$ pip freeze -l
asgiref==3.2.10
Django==3.0.2
pytz==2020.1
sqlparse==0.3.1
```