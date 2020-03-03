from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Dashboard view
@login_required
def index(request): 
  notes = Note.objects.filter(user=request.user)
  return render(request, 'notes/index.html', {
    "notes":notes
  })
# 'Add Note' Page View
@login_required
def add(request):
  return render(request, 'notes/create.html')
# Note's Create action 
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
# Note's Single Page view
@login_required
def show(request, id):
  note = get_object_or_404(Note, pk=id, user=request.user)
  return render(request, 'notes/show.html', {
    "note": note
  })
# Note's Edit Page view
@login_required
def edit(request, id):
  note = get_object_or_404(Note, pk=id, user=request.user)
  return render(request, 'notes/edit.html', {
    "note":note
  })
# Note's Update Acition
@login_required
def update(request, id):
  title   = request.POST.get('title')
  content = request.POST.get('content')
  note = get_object_or_404(Note, pk=id, user=request.user)
  if title and content:
    note.title = title
    note.content = content
    note.save()
    messages.success(request, "Note Succesfuly updated")
    return redirect(f"/notes/{id}")
  messages.error(request, "Title and Markdown's Content is Required")
  return redirect(f"/notes/edit/{id}")
# Note's Delete Acition

@login_required
def delete(request, id):
  note = get_object_or_404(Note, pk=id, user=request.user)
  if request.method == "POST":
    note.delete()
    messages.success(request, "Note Successfuly Deleted")
    return redirect("/notes/")
  return redirect(f"/notes/{id}")
