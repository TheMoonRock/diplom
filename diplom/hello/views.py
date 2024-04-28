from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.template.response import TemplateResponse
from datetime import datetime

def index(request):
    road = request.get_port()
    something = request.META["REMOTE_ADDR"]
    cook = request.scheme
    return HttpResponse(f"""
        <h3>Главная</h3>
        <p>path: {road}</p>
        <p>IP: {something}</p>
        <p>Cookie: {cook}</p>
    """, headers={"SecretCode": "123"})

def about(request, name, age):
    return HttpResponse(f"""
        <h2>О пользователе</h2>
        <p>Имя: {name}</p>
        <p>Возраст: {age}</p>
    """)

def contact(request, name, age, organization):
    return HttpResponse(f"""
        <h3>Контакты</h3>
        <p>Имя: {name}</p>
        <p>Возраст: {age}</p>
        <p>Организация: {organization}</p>
    """)

def zapros(request, name="Undefined", age=0):
    return HttpResponse(f"<h1>Запрос: {name} Возраст: {age}</h1>")

def products(request, id):
    return HttpResponse("Список товаров")

def discussion(request, id):
    return HttpResponse(f"Спор: {id}")

def returnback(request, id):
    return HttpResponse(f"Возврат: {id}")

def reason(request, id):
    return HttpResponse(f"Причина возврата товара: {id}")

def feedback(request, id):
    return HttpResponse(f"Отзыв о товаре: {id}")

def something(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")

def some_about(request):
    return HttpResponse("Some_About")

def some_contact(request):
    return HttpResponseRedirect("/some_about")

def some_details(request):
    return HttpResponsePermanentRedirect("/")

def testedtest(request, id):
    people = ["Artyom", "Nikita", "Damir"]
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Not Found")

def access(request, agen):
    if agen not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if (agen > 17):
        return HttpResponse("Доступ разрешён")
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

def rice(request):
    Artyom = rice_serialization("Artyom", 22)
    return JsonResponse(Artyom, safe=False, encoder=PersonEncoder)

class rice_serialization:

    def __init__(self, name, agen1):
        self.name = name
        self.agen1 = agen1

class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, rice_serialization):
            return {"name": obj.name, "age": obj.agen1}
        return super().default(obj)

def set(request):
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    response.set_cookie("username", username)
    return response

def get(request):
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")

def razmetka(request):
    header = "Данные пользователя"
    langs = ["Python", "Java", "C#"]
    user = {"name" : "Artyom", "age" : 22}
    address = ("Абрикосовая", 23, 45)

    data = {"header" : header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)

def razmetka_about(request):
    return render(request, "about.html", context={"body": "<h1>Hello World!</h1>"})

def razmetka_contact(request):
    data = {"n" : 5}
    return TemplateResponse(request, "contact.html", context=data)

def razmetka_cycle(request):
    langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    return render(request, "cycle.html", context={"langs": langs, "mydate": datetime.now()})

def something_123(request):
    return render(request, "something.html")

