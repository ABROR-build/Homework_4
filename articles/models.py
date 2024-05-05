
from django.db import models


class Topics(models.Model):
    topic_name = models.CharField(max_length=300)

    class Meta:
        db_table = 'Topics'

    def __str__(self):
        return self.topic_name


class News(models.Model):
    topic_name = models.ForeignKey(Topics, on_delete=models.CASCADE)
    title = models.CharField(max_length=700)
    summary = models.TextField(max_length=2000)
    article = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
