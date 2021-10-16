from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.MainView.as_view(), name="mainpage"),
    path("contats/", mainapp.ContactsView.as_view(), name="contacts"),
    path("work", mainapp.WorksView.as_view(), name="work"),
]
