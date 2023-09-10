from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #id
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    #is_delete = models.BooleanField(default=False)
    #这里写错了，但是已经形成迁移文件了
    id_deltete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'   #修改表的名字
        verbose_name = '书籍管理'   #admin站点使用
    def __str__(self):
        return self.name


#人物
class PeopleInfo(models.Model):
    #定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female'),
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.BooleanField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    #外键，系统会自动为外键添加下划线 id
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    #这里使用外键的级联操作
    #主表 和 从表
    #一本书 对应多个人物
    #主表的一条数据删除了，从表的关联数据应该做出何种操作

    class Meta:
        db_table = 'peopleinfo'   #修改表的名字
        verbose_name = '人物信息'   #admin站点使用
    def __str__(self):
        return self.name


