from django.db import models

# Create your models here.
class FileUpload(models.Model):
    # title = models.TextField(max_length=10, null=True)
    attached = models.FileField('첨부파일', upload_to='uploads/')

    # def __str__(self):
    #     return self.title

class Basic_stats(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField()