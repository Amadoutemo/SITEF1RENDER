from django.shortcuts import render
from .models import Pilote

def accueil(request):
    pilotes = Pilote.objects.all()
    return render(request, 'F1 test avancé.html', {'pilotes': pilotes})