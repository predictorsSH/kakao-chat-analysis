from django.db import models

# Create your models here.
class FileUpload(models.Model):

    f_id = models.BigAutoField(help_text="File id",
                               primary_key=True)
    attached = models.FileField('첨부파일', upload_to='uploads/')


class Basic_stats(models.Model):

    f_id = models.ForeignKey("FileUpload",
                             related_name="File",
                             on_delete=models.CASCADE,
                             db_column='f_id',
                             )

    user_count = models.TextField() #유저별 채팅 횟수
    active_time = models.IntegerField(default=3) #대화가 가장 활발한 시간
    user_words_count = models.TextField(null=True) # 유저별 많이 사용한 단어 5개 # null=True 면 안됨.

class Advanced_analyis(models.Model):
    test = models.TextField() #개발 미정