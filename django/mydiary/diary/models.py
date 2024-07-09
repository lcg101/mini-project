from django.db import models

class DiaryEntry(models.Model):
    date = models.DateField(verbose_name="날짜")
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
    image = models.ImageField(upload_to='diary_images/', blank=True, null=True, verbose_name="이미지")
    tags = models.CharField(max_length=100, blank=True, verbose_name="태그")
    content = models.TextField(verbose_name="내용")

    def __str__(self):
        return f"일기 ({self.date})"

