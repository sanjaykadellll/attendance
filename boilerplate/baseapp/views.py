from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,('index.html'))

# def signup(request):
# 	return render(request,('signup.html'))


# def login(request):
# 	return render(request,('login.html'))

def certificate(request):
	return render(request,('certificate.html'))