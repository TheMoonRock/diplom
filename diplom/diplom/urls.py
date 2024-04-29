"""
URL configuration for diplom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from hello import views

returnback_inner = [
    path("", views.reason),
    path("feedback", views.feedback)
]

product_patterns = [
    path("", views.products),
    path("discussion", views.discussion),
    path("returnback/", include(returnback_inner)),
]

urlpatterns = [
        re_path(r'^about/contact', views.contact, kwargs={"name":"Артём", "age":22, "organization": "НТЦ ПАО КАМАЗ"}, name='contact'),
    path('', views.index, name='home'),
    re_path(r'^about', views.about, kwargs={"name":"Tom", "age": 38},name='about'),
    re_path(r"^zapros/(?P<name>\D+)/(?P<age>\d+)", views.zapros),
    re_path(r"^zapros/(?P<name>\D+)", views.zapros),
    re_path(r"^zapros", views.zapros),
    path("products/<int:id>/", include(product_patterns)),
    path("something/", views.something),
    path("some_about/", views.about),
    path("some_contact/", views.contact),
    path("some_details/", views.some_details),
    path("testedtest/<int:id>", views.testedtest),
    path("access/<int:agen>", views.access),
    path("rice", views.rice),
    path("set", views.set),
    path("get", views.get),
    path("razmetka", views.razmetka),
    path("razmetka_about/", views.razmetka_about),
    path("razmetka_contact/", views.razmetka_contact),
    path("razmetka_cycle/", views.razmetka_cycle),
    path("something_123/", views.something_123),
    path("index1/", views.index1),
    path("contacts/", views.contacts1),
]
