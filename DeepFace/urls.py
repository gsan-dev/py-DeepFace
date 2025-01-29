from django.contrib import admin
from django.urls import path
from recognition import views  # Asegúrate de importar tus vistas

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register_face, name="register"),
    path("recognize/", views.recognize_face, name="recognize"),
]
