from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import Note

def main(request):
    notes: QuerySet = Note.objects.all()
    return render(request, "index.html", locals())

def add_note(request: HttpRequest):
    if request.method != "POST":
        return redirect("/")

    content = request.POST.get("content")
    print(request.POST)
    note = Note(content=content)
    note.save()
    return redirect("/")
