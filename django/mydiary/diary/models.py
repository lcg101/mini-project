from django.db import models

class DiaryEntry(models.Model):
    date = models.DateField(verbose_name="날짜")
    title = models.CharField(max_length=200, verbose_name="제목", blank=True)
    mood_choices = [
        ('happy', '😊'),
        ('sad', '😢'),
        ('angry', '😡'),
        ('neutral', '😐'),
    ]
    mood = models.CharField(max_length=10, choices=mood_choices, verbose_name="감정")
    weather_choices = [
        ('sunny', '☀️'),
        ('rainy', '🌧️'),
        ('cloudy', '☁️'),
        ('snowy', '❄️'),
    ]
    weather = models.CharField(max_length=10, choices=weather_choices, verbose_name="날씨")
    image1 = models.ImageField(upload_to='diary_images/', blank=True, null=True, verbose_name="이미지 1")
    image2 = models.ImageField(upload_to='diary_images/', blank=True, null=True, verbose_name="이미지 2")
    image3 = models.ImageField(upload_to='diary_images/', blank=True, null=True, verbose_name="이미지 3")
    image4 = models.ImageField(upload_to='diary_images/', blank=True, null=True, verbose_name="이미지 4")
    image5 = models.ImageField(upload_to='diary_images/', blank=True, null=True, verbose_name="이미지 5")
    tags = models.CharField(max_length=100, blank=True, verbose_name="태그")
    content = models.TextField(verbose_name="내용")
    memo = models.CharField(max_length=20, blank=True, null=True, verbose_name="메모")  # 메모 필드 추가

    def __str__(self):
        return f"{self.date} - {self.title}"

