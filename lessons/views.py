from django.contrib.sessions.middleware import SessionMiddleware
from django.shortcuts import render
from django.template.response import TemplateResponse
from lessons.forms import PersonEditingForm
from lessons.models import Person, Log


def index(request):
    person = Person.objects.all()
    context = {
        'person': person
    }
    response = TemplateResponse(
        request=request,
        template='index.html',
        context=context
    )
    return response


def log_table(request):
    logs = Log.objects.all()
    context = {
        'logs': logs
    }
    response = TemplateResponse(
        request=request,
        template='log_table.html',
        context=context
    )
    return response


def person_editing(request, person_pk):
    person = Person.objects.get(pk=person_pk)
    form = PersonEditingForm(instance=person)
    context = {
        'person': person,
        'person_form': form
    }
    response = TemplateResponse(
        request=request,
        template='edit_form.html',
        context=context
    )
    return response