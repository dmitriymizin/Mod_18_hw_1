from django.shortcuts import render
from .forms import UserRegister

users = ["user1", "user2"]

# Create your views here.

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get("login")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            info['error'] = f'Приветствуем, {username}!'

    return render(request, "fifth_task/registration_page.html", info)

def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["login"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif int(age) < 18:
                info["error"] = "Вы должны быть старше 18"
            elif username in users:
                info["error"] = "Пользователь уже существует"
            else:
                users.append(username)
                info["success"] = f"Приветствуем, {username}!"
        else:
            info["form"] = form
    else:
        info["form"] = UserRegister()

    return render(request, "fifth_task/registration_page.html", info)



