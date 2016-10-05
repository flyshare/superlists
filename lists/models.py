from django.db import models

# Create your models here.


class Item(models.Model):
    text = models.TextField(default='')   # 不使用 CharField 是因为 text不用设置长度
