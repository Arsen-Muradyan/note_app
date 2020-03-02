from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def index(request): 
  notes = Note.objects.filter(user=request.user)
  return render(request, 'notes/index.html', {
    "notes":notes
  })
@login_required
def add(request):
  return render(request, 'notes/create.html')
@login_required
def create(request):
  title   = request.POST.get('title')
  content = request.POST.get('content')
  if title and content:
    note = Note(title=title, content=content, user=request.user)
    note.save()
    messages.success(request, 'Your Note Successfuly Created')
    return redirect('/notes/')
  messages.error(request, "Title and Markdown's Content is Required")
  return redirect('/notes/add')
@login_required
def show(request, id):
  note = Note.objects.get(pk=id, user=request.user)
  return render(request, 'notes/show.html', {
    "note": note
  })
@login_required
def edit(request, id):
  note = Note.objects.get(pk=id, user=request.user)
  return render(request, 'notes/edit.html', {
    "note":note
  })