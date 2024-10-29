from django.shortcuts import render

# Create your views here.
def menu_view(request):
    return render(request, 'fourth_task/menu.html')

def games_view(request):
    games = [
        'Atomic Heart',
        'Cyberpunk 2077',
        'Pay Day 2',
    ]
    return render(request, 'fourth_task/games.html', {'games': games})

def platform_view(request):
    return render(request, 'fourth_task/platform.html')

def cart_view(request):
    cart_items = []
    return render(request, 'fourth_task/cart.html', {'cart_items': cart_items})
