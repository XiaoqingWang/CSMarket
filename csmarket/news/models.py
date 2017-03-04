#-*-coding:utf-8-*-
from django.db import models

# Create your models here.

class cate(models.Model):
    cate_name=models.CharField(verbose_name="类别标题",max_length=30)
    cate_time = models.DateTimeField(verbose_name="添加时间")
    cate_num = models.IntegerField(verbose_name="类别编号",unique=True)

    def __str__(self):
        return self.cate_name

    class Meta:
        db_table = "cate_table"
        verbose_name = u'类别'
        verbose_name_plural = u'类别管理'

class News(models.Model):
    new_title = models.CharField(verbose_name='标题', max_length=30, blank=False)
    new_author = models.CharField(verbose_name='发布人', max_length=15, blank=False)
    new_time = models.DateTimeField(verbose_name='发布时间')
    new_seenum = models.IntegerField(verbose_name='浏览次数',default=0)
    new_content = models.TextField(verbose_name='内容',blank=False)
    new_cate = models.ForeignKey(cate,verbose_name='类别',blank=False)

    def __str__(self):
        return self.new_title

    class Meta:
        db_table = "news_table"
        verbose_name = u'CSM动态'
        verbose_name_plural = u'动态管理'