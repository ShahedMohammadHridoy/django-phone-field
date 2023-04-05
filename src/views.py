from django.shortcuts import render
from .forms import PersonForm


def save_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            pass
        else:
            return render(request, 'person.html', {'form': form})

    form = PersonForm()
    return render(request, 'person.html', {'form': form})


def success(request):
    return render(request, 'success.html')
