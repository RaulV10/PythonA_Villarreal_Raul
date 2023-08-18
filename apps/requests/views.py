from django.shortcuts import redirect, render
from django.views import View
from .models import Request
from django.http import JsonResponse

class UserRequestListView(View):
    template_name = "requests/user_requests.html"

    def get(self, request):
        if request.user.is_staff:  # Verifica si el usuario tiene permisos de staff
            user_requests = Request.objects.all()
        else:
            user_requests = Request.objects.filter(user=request.user)
        context = {'user_requests': user_requests}
        return render(request, self.template_name, context)

def create_request(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        
        if title and description and location:
            new_request = Request.objects.create(
                title=title,
                description=description,
                location=location,
                status='pending',
                user=request.user
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return render(request, 'create_request.html')

def edit_request(request, request_id):
    # Obtener la solicitud a editar
    try:
        request_obj = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        return JsonResponse({'success': False})

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            request_obj.title = title
            request_obj.description = description
            request_obj.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    
    return JsonResponse({'success': False})

def delete_request(request, request_id):
    try:
        request_obj = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        return JsonResponse({'success': False})

    if request.method == 'POST':
        request_obj.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

def change_status(request, request_id):
    if request.method == 'POST':
        new_status = request.POST.get('new_status')

        try:
            request_obj = Request.objects.get(pk=request_id)
            request_obj.status = new_status
            request_obj.save()
            return JsonResponse({'success': True})
        except Request.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Solicitud no encontrada'})
    
    return JsonResponse({'success': False, 'message': 'Petición inválida'})