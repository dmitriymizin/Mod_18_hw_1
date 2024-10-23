from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def class_template(request):
    return render(request, 'second_task/class_template.html')

# def func_template(request):
#     return render(request, 'func_templates.html')

# from django.conf import settings
# print(settings.TEMPLATES[0]['DIRS'])