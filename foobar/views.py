from django.db.models.query import QuerySet
from django.db.models.functions import Extract
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

import sys
import logging

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

def search(request: HttpRequest):
    if request.method != "GET":
        return redirect("/")
    logger = logging.getLogger("django")
    notes = None
    if request.GET.get("show_plan"):
        req:str = request.GET.get("date")
        found = False
        for s in ["year", "month", "day"]:
            if req.startswith(s):
                found = True
                break
        if not found:
            print("DID NOT FIND")
            redirect("/")
        try:
            date = Extract("date", req)

            notes = Note.objects.filter(date__year=date)
            logger.info(notes)
        except Exception as e:
            print("Exception: ", e)
    else:
        query = request.GET.get("content")
        notes = Note.objects.filter(content=query)
    return render(request, "index.html", locals())

def delete(request: HttpRequest):
    pass
