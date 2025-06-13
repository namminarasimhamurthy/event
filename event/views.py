from django.shortcuts import render,redirect
from .models import UserRegistration
from .models import EventBooking


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def registerup(request):
    if request.method == "POST":
        print("POST request received")  # Debug line
        x = request.POST['name']
        y = request.POST['email']
        z = request.POST['password']
        a = request.POST['confirm_password']

        if z != a:
            return render(request, 'register.html', {'error': "Passwords do not match"})

        mem = UserRegistration(name=x, email=y, password=z, confirm_password=a)
        mem.save()
        print("User saved!")  # Debug line
        return redirect('/login')
    return redirect('/register')

def loginup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Fetch user with the provided email
            user = UserRegistration.objects.get(email=email)
            
            # Check if the password matches
            if user.password == password:
                # Set session for logged-in user (optional)
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                
                # Redirect to the home page after successful login
                return redirect('home')  # This assumes you have a named URL pattern for 'home'
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except UserRegistration.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist'})

    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')



def booking(request):
    mem = EventBooking.objects.all()  
    return render(request, 'booking.html', {'mem': mem})

def bookingup(request):
    if request.method == "POST":
        x = request.POST['full_name']
        y = request.POST['email']
        z = request.POST['event_name']
        a = request.POST['mobile_number']
        b = request.POST['event_date']
        c = request.POST['amount']
        d = request.POST['description']
        mem = EventBooking(full_name=x,email=y,event_name =z,mobile_number=a,event_date=b,amount=c,description=d)
        mem.save()
        return redirect('/sucessfully')
    
def sucessfully(request):
    return render(request,'sucessfully.html')

def signout(request):
    return redirect('/')

def about(request):
    return render(request,'about.html')