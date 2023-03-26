from django.db import models

# Create your models here.
class FileUpload(models.Model):

    # title = models.TextField(max_length=10, null=True)
    attached = models.FileField('첨부파일', upload_to='uploads/')

    # def __str__(self):
    #     return self.title

class Basic_stats(models.Model):

    user_count = models.TextField() #유저별 채팅 횟수
    active_time = models.IntegerField(default=3) #대화가 가장 활발한 시간
    user_words_count = models.TextField(null=True) # 유저별 많이 사용한 단어 5개 # null=True 면 안됨.

