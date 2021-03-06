from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_password = models.CharField(max_length=18)
    user_name = models.CharField(max_length=18)
    user_email = models.CharField(max_length=30)
    user_phone = models.IntegerField(default=0)


class goods(models.Model):

    Goods_Category = (
        ('1', "鞋服配饰"),
        ('2', "生活用品"),
        ('3', "交通工具"),
        ('4', "图书电子"),
    )

    Goods_SubCategory = (
        ('1', "女装"),
        ('2', "男装"),
        ('3', "鞋靴"),
        ('4', "配饰箱包"),
        ('5', "美妆洗护"),
        ('6', "家具"),
        ('7', "家纺/家饰"),
        ('8', "百货"),
        ('9', "自行车"),
        ('10',"电动车"),
        ('11', "配饰/箱包"),
        ('12', "图书"),
        ('13', "文具"),
        ('14', "数码/电器"),
    )
    goods_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(user, on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=30)
    goods_category = models.CharField(max_length=5, choices=Goods_Category)
    goods_subcategory = models.CharField(max_length=6, choices=Goods_SubCategory)
    goods_picture = models.ImageField(upload_to='./sell/', height_field=None, width_field=None)
    goods_price = models.FloatField(max_length=15)
    goods_info = models.CharField(max_length=400)
    goods_other_info = models.CharField(max_length=400)

class order(models.Model):
    orderNo = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='order_sell_id', verbose_name="the seller's id",)
    seller_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name='order_buyer_id', verbose_name="the buyer's id",)
