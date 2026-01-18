from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from .models import Category, Category


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)


def topic_list(request):
    # pobieramy wszystkie obiekty Topic z bazy poprzez QuerySet
    topics = Category.objects.all()
    return HttpResponse(topics)


def category_list(request):
    categories = Category.objects.all()

    return render(request,
                  "posts/category/list.html",
                  {'categories': categories})


def category_detail(request, id):
    # pobieramy konkretny obiekt Category
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404(f"Obiekt Category o id={id} nie istnieje")

    return render(request,
                  "posts/category/detail.html",
                  {'category': category})