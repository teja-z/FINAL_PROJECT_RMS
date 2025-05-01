from django.shortcuts import render

# Example views for each category
def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def cart_view(request):
    return render(request, 'cart.html')

def dairy(request):
    return render(request, 'dairy.html')

def cold_drink(request):
    return render(request, 'cold_drink.html')

def snacks(request):
    return render(request, 'snacks.html')

def instant_food(request):
    return render(request, 'instant_food.html')

def sweet(request):
    return render(request, 'sweet.html')

def bakery(request):
    return render(request, 'bakery.html')

def tea_coffee(request):
    return render(request, 'tea_coffee.html')

def atta_rice_dal(request):
    return render(request, 'atta_rice_dal.html')

def masala_oil(request):
    return render(request, 'masala_oil.html')

def sauce_spread(request):
    return render(request, 'sauce_spread.html')

def baby_care(request):
    return render(request, 'baby_care.html')

def pharma_wellness(request):
    return render(request, 'pharma_wellness.html')

def cleaning_essentials(request):
    return render(request, 'cleaning_essentials.html')

def personal_care(request):
    return render(request, 'personal_care.html')

def love_corner(request):
    return render(request, 'love_corner.html')

def checkout(request):
    return render(request, 'checkout.html')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')
