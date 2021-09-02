from django.shortcuts import render
from .models import Todo
# Create your views here.
def home(request):
    todos_list = Todo.objects.all()
    return render(request, 'index.html',{"todos":todos_list})
     