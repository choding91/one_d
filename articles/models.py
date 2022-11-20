from django.db import models
from users.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_user")
    likes = models.ManyToManyField(User, related_name="article_likes")
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="%Y/%m/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.title} / {self.content}")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment_article")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.user} / {self.content}")
