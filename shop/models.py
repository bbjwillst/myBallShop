from django.db import models


# Create your models here.
class Product(models.Model):
    item_number = models.CharField(max_length=100, default='', db_index=True, blank=True, verbose_name='商品编号')
    name = models.CharField(max_length=100, default='', db_index=True, verbose_name='商品名称')
    click_count = models.IntegerField(default=0, verbose_name='浏览次数')
    quantity = models.IntegerField(default=0, verbose_name='库存数量')
    price = models.FloatField(default=0.0, verbose_name='价格')
    market_price = models.FloatField(default=0.0, verbose_name='市场价')
    description = models.TextField(blank=True, verbose_name='详细描述')
    sort_order = models.IntegerField(default=0, verbose_name='排序序号')
    is_publish = models.BooleanField(default=False, verbose_name='上架')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
