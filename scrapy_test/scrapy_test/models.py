from peewee import *

db = MySQLDatabase('spider', host='127.0.0.1', port=3306, user='root', password='123456')


class BaseModel(Model):
    class Meta:
        database = db  # This model uses the "people.db" database.


# 注意设置字段类型，以及有没有默认值
class Topic(BaseModel):
    title = CharField()
    content = TextField(default="")
    id = IntegerField(primary_key=True)
    author = CharField()
    create_time = DateTimeField()
    answer_nums = IntegerField(default=0)
    click_nums = IntegerField(default=0)
    praised_nums = IntegerField(default=0)
    jtl = FloatField(default=0.0)  # 结帖率
    score = IntegerField(default=0)  # 赏分
    status = CharField()  # 状态
    last_answer_time = DateTimeField()


class Answer(BaseModel):
    topic_id = IntegerField()
    answer_id = IntegerField()
    author = CharField()
    content = TextField(default="")
    create_time = DateTimeField()
    parised_nums = IntegerField(default=0)  # 点赞数


class Author(BaseModel):
    name = CharField()  # 博客
    id = CharField(primary_key=True,max_length=50)  # 博客
    click_nums = IntegerField(default=0)  # 访问数 博客
    original_nums = IntegerField(default=0)  # 原创数 博客
    forward_nums = IntegerField(default=0)  # 转发数 无
    rate = IntegerField(default=-1)  # 排名 博客
    answer_nums = IntegerField(default=0)  # 评论数 博客
    parised_nums = IntegerField(default=0)  # 获赞数 博客
    desc = TextField(null=True)  # 主页
    industry = CharField(null=True)  # 无
    location = CharField(null=True)  # 无
    follower_nums = IntegerField(default=0)  # 粉丝数 博客
    following_nums = IntegerField(default=0)  # 关注数 主页


# utf8mb4的数据库会报错字符超长，改成utf8就可以了
if __name__ == "__main__":
    db.create_tables([Topic, Answer, Author])
