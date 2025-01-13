from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import base64
from io import BytesIO
from PIL import Image
from .models import Doodle

@method_decorator(csrf_exempt, name='dispatch')
class DoodleView(TemplateView):
    template_name = 'doodle/doodle_page.html'

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            doodle_data = data.get('doodle_data')
            title = data.get('title', 'Untitled Doodle')
            
            # Create doodle record
            doodle = Doodle.objects.create(
                title=title,
                doodle_data=doodle_data
            )
            
            # If you want to store as image too:
            if data.get('image_data'):
                # Remove data URL prefix
                image_data = data['image_data'].split(',')[1]
                image_binary = base64.b64decode(image_data)
                
                # Create PIL Image
                image = Image.open(BytesIO(image_binary))
                
                # Save to BytesIO
                buffer = BytesIO()
                image.save(buffer, format='PNG')
                
                # Save to Doodle model
                doodle.image.save(f'{title}.png', buffer, save=True)
            
            return JsonResponse({'status': 'success', 'id': doodle.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)