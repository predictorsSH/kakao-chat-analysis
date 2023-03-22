from django.db import models

# Create your models here.
class FileUpload(models.Model):

    # title = models.TextField(max_length=10, null=True)
    attached = models.FileField('첨부파일', upload_to='uploads/')

    # def __str__(self):
    #     return self.title

class Basic_stats(models.Model):

    count = models.TextField() #유저별 채팅 횟수
    active_time = models.IntegerField(default=3) #대화가 가장 활발한 시간
    # active_time : 대화가 가장 활발한 시간

