from django.shortcuts import render

# Create your views here.

def games_view(request):
    games = {
        'Atomic Heard': 'Купить',
        'Cyberpunk 2077': 'Купить',
        'Pay Day 2': 'Купить',
    }
    return render(request, 'third_task/games.html', {'games': games})

def platform_view(request):
    return render(request, 'third_task/platform.html')

def cart_view(request):
    cart_items = []
    return render(request, 'third_task/cart.html', {'cart_items': cart_items})
