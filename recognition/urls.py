from django.urls import path
from .views import register_face, recognize_face

urlpatterns = [
    path('register/', register_face, name='register_face'),
    path('recognize/', recognize_face, name='recognize_face'),
]
