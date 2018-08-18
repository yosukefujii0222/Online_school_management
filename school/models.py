from django.db import models

# レッスンのオブジェクトを作成
class Lesson(models.Model):

  GENRE_CHOICES = (
    (1, '英語'),
    (2, 'ファイナンス'),
    (3, 'プログラミング'),
  )

  genre = models.IntegerField(verbose_name='ジャンル', choices=GENRE_CHOICES, blank=True, null=True)
  charge = models.IntegerField(verbose_name='基本料金')
  usage_fee = models.IntegerField(verbose_name='従量料金')


  def __str__(self):
    return self.genre
