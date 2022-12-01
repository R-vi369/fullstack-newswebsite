from django.shortcuts import render , redirect
import requests
from .models import Contact
import json
import urllib.request
# from .forms import signupform 
from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import signupform
# Create your views here.


from django.shortcuts import render

# def new(request):
#     return render(request, 'home.html')

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['text']
        print(name, phone, email,text)

        contact = Contact(name = name ,email = email ,phone = phone, text = text)
        contact.save()
        if len(name)<2 or len(email)<2 or len(text)<3 or len(phone)<5:
            return HttpResponse("<h1>404 Not Found</h1>")
        messages.success(request,"Successfull ")
        return redirect('home')
           
    return render(request, 'contact.html')

def home(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'home.html', {'api':api}
    )
def sports(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'sports.html', {'api':api}
    )
def science(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'science.html', {'api':api}
    )
def health(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'health.html', {'api':api}
    )
def technology(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'technology.html', {'api':api}
    )
def general(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'general.html', {'api':api}
    )
def entertainment(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'entertainment.html', {'api':api}
    )
def business(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f667f2f013184d4c8514c28ce2bf40ef&page=1&pageSize=70')
    # print(response)

    api = json.loads(response.content)

    return render(request, 'business.html', {'api':api}
    )



def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=86dcb980a68aa69ff780670f4b1f3687&units=metric').read()

        list_of_data = json.loads(source)
        data = {
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + "," + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + chr(176) +'C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : str(list_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data = {}
    return render(request, 'weather.html',data)
# def signup(request):
#     return render(request, 'signup.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # for bad input
        # if len(username)>10:
        #     messages.error(request,"username must be under 10 characters")
        #     return redirect('home')
        # if pass1 != pass2:
        #     messages.error(request,"Password do not match")
        #     return redirect('home')    
        # Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Successfull Signup")
        return redirect('home')
    else:
        return HTTPResponse("Not found")


 
       

def handlelogin(request):
        if request.method == 'POST':
            loginusername = request.POST['loginusername']
            loginpass = request.POST['loginpass']

            user = authenticate(username=loginusername,password=loginpass)

            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in")
                return redirect('home')
            else:
                messages.info(request,"Invalid Credentials")
                return redirect('home')
        else:
            return HTTPResponse("404 Not Found")

def handlelogout(request):
        logout(request)
        messages.success(request, "Successfully logged Out")
        return  redirect('home')