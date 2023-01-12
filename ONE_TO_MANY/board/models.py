from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
        content = models.CharField(max_length=200)
        # article_id
        # foreign key 쓰면 필드명에 _id 붙이지 않기
        # migrate하면 알아서 뒤에 _id 붙음
        article = models.ForeignKey(Article, on_delete=models.CASCADE)  # on_delete CASCADE: article이 삭제되면 관련된 comment들은 다 지우겠다.
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)