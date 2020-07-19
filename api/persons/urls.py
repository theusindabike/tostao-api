from django.urls import path


from api.persons import views

app_name = 'persons'

urlpatterns = [
    path('api/persons/', views.Persons.as_view())
]
