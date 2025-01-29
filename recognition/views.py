from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserFace
from .utils import verify_face
import os

@csrf_exempt
def register_face(request):
    if request.method == 'POST' and request.FILES.get('image'):
        name = request.POST.get('name')
        image = request.FILES['image']
        user_face = UserFace.objects.create(name=name, image=image)
        return JsonResponse({'message': 'Face registered successfully', 'user_id': user_face.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def recognize_face(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        all_faces = UserFace.objects.all()
        
        for face in all_faces:
            if verify_face(face.image.path, uploaded_image):
                return JsonResponse({'message': f'Face recognized as {face.name}'})
        
        return JsonResponse({'message': 'Face not recognized'}, status=404)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
