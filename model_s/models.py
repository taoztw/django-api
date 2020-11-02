from django.db import models

# Create your models here.


# 基模型，定义一些共有字段
class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        # 原元数据中声明此字段后  不会再数据库为此表创建对应的表结构
        # 其他模型在继承此模型后,可以继承表中的字段
        abstract = True

class User(BaseModel):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "ts_login_user"
        verbose_name = "登陆用户"
        verbose_name_plural = verbose_name


class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to="img", default="img/1.jpg")
    publish = models.ForeignKey(to="Press", on_delete=models.CASCADE, db_constraint=False,
                                related_name="books")  # 出版社
    authors = models.ManyToManyField(to="Author", db_constraint=False, related_name="books")

    class Meta:
        db_table = "ts_book"
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name

    # 自定义序列化属性
    @property
    def press_name(self):
        return self.publish.press_name

    @property
    def author_list(self):
        return self.authors.values("author_name", "age", "detail_phone")


class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to="p_img", default="p_img/1.jpg")
    address = models.CharField(max_length=256)

    class Meta:
        db_table = "ts_press"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.press_name


class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = "ts_author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    author = models.OneToOneField(to="Author", on_delete=models.CASCADE, related_name="detail")

    class Meta:
        db_table = "ts_author_detail"
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.author.author_name}的详情"
