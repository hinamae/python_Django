#django.dbからmodelsファイルをインポートしている
#フォルダ名.ファイル名　フォルダ名/ファイル名
from django.db import models

# ファイル名.そのファイルの中で定義されている変数
# ファイル名.そのファイルの中で定義されている関数

# Create your models here.

# modelsファイルの中のクラス(＝Model)を継承している
# インポートした　ファイル名.そのファイルの中で定義されているクラス
class Book(models.Model):
    # 書籍
    name = models.CharField('書籍名',max_length=255)
    publisher = models.CharField('著者',max_length=255,blank = True)
    page = models.IntegerField('ページ数',blank = True , default=0)

    #コンストラクタ Bookクラスのインスタンス生成時に必ず実行される
    def __str__(self):
        return self.name

class Impression(models.Model):
    # 感想
    book = models.ForeignKey(Book,verbose_name='書籍',related_name='impression',on_delete=models.CASCADE)
    comment= models.TextField('コメント',blank = True)

    def __str__(self):
        return self.comment