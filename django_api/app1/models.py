from django.db import models


# Create your models here.
class Obj(models.Model):
    #modelの内部に設定するオプション
    class Meta:
        #管理画面での詳細表示
        verbose_name = 'オブジェクト名'
        #複数形：指定しないとsが付けられる
        verbose_name_plural = 'オブジェクト名'

    name = models.CharField("オブジェクト名",max_length=32)
    obj_code = models.CharField("コード",max_length=32)

    #adminの管理画面などで表示される文字列を定義
    def __str__(self):
        return self.name

class Branch(models.Model):
    class Meta:
        verbose_name = "ブランチ名"
        verbose_name_plural = "ブランチ名"

    #親を指定、on_deleteで親が消えたら消える
    obj_name = models.ForeignKey(Obj, on_delete=models.CASCADE)
    branch_name = models.CharField("ブランチ名",max_length=32)
    branch_code = models.CharField("ブランチコード",max_length=32)

    def __str__(self):
        return self.branch_name
