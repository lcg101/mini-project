from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['date', 'title', 'mood', 'weather', 'image1', 'image2', 'image3', 'image4', 'image5', 'tags', 'content', 'memo']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mood': forms.RadioSelect(),
            'weather': forms.RadioSelect(),
            'tags': forms.TextInput(attrs={'placeholder': '예: 맛집, 여행, 일상'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': '내용을 입력하세요'}),
        }
        labels = {
            'date': '날짜',
            'title': '제목',
            'mood': '감정',
            'weather': '날씨',
            'image1': '이미지 1',
            'image2': '이미지 2',
            'image3': '이미지 3',
            'image4': '이미지 4',
            'image5': '이미지 5',
            'tags': '태그',
            'content': '내용',
        }

