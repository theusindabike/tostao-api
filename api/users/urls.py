from django.urls import path


from api.users import views

app_name = 'users'

urlpatterns = [
    path('api/users/', views.Users.as_view())
]
