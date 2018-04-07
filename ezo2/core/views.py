from django.shortcuts import render

import blog.global_var as global_var

def home(request):
    return render(request, 'core/home.html')