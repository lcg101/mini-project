from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['date', 'mood', 'weather', 'image', 'tags', 'content']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mood': forms.RadioSelect(),
            'weather': forms.RadioSelect(),
            'tags': forms.TextInput(attrs={'placeholder': '예: 맛집, 여행, 일상'}),
            'content': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'date': '날짜',
            'mood': '감정',
            'weather': '날씨',
            'image': '파일 선택',
            'tags': '태그',
            'content': '내용',
        }

