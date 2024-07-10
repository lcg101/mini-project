from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiaryEntryForm
from .models import DiaryEntry
from datetime import datetime
from django.db.models import Q

def home(request):
    now = datetime.now()
    return render(request, 'diary/home.html', {'now': now})

def calendar(request):
    entries = DiaryEntry.objects.all()
    entries_data = []
    for entry in entries:
        entry_data = {
            'date': entry.date.strftime('%Y-%m-%d'),
        }
        entries_data.append(entry_data)
    return render(request, 'diary/calendar.html', {'entries_data': entries_data})



def new_entry(request):
    date = request.GET.get('date', None)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm(initial={'date': date})
    return render(request, 'diary/new_entry.html', {'form': form})

def edit_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            entry.image1 = request.FILES.get('image1', entry.image1)
            entry.image2 = request.FILES.get('image2', entry.image2)
            entry.image3 = request.FILES.get('image3', entry.image3)
            entry.image4 = request.FILES.get('image4', entry.image4)
            entry.image5 = request.FILES.get('image5', entry.image5)
            form.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/edit_entry.html', {'form': form, 'entry': entry, 'entry_date': entry.date.strftime('%Y-%m-%d')})


def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = DiaryEntry.objects.filter(
            Q(tags__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'diary/search_results.html', {'query': query, 'results': results})

def diary_list(request):
    entries = DiaryEntry.objects.all().order_by('-date')
    return render(request, 'diary/diary_list.html', {'entries': entries})

def diary_detail(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    return render(request, 'diary/diary_detail.html', {'entry': entry})

def diary_delete(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)
    entry.delete()
    return redirect('diary_list')

