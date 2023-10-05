from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_type = models.CharField(max_length=200, default="Others")
    def __str__(self):
        return f"{self.author} - {self.title}"
