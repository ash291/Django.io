# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<title> Menu </title><head> Menu </head><br><a href='http://google.com'>1. Google</a><br><a href='http://facebook.com'>2. Facebook</a><br><a href='http://youtube.com'>3. youtube</a><br><a href='/'>4. Back</a><br>")

# from django.http import HttpResponse

# def hello(request):
#   return HttpResponse("<p>This is may first App<p><br><a href=''></a>")
# def main(request):
#  	  return HttpResponse("<p> Welcome to Django Website<p><br><a href=/menu>Menu</a>")
 #from django.http import HttpResponseRedirect
# from django.http import HttpResponse
# from django.shortcuts import render
# from .forms import InputForm

# def add(request):
#     if request.method == 'POST':        # If the form has been submitted...
#      form = InputForm(request.POST)     # A form bound to the POST data
#      if form.is_valid():                # All validation rules pass
#         cd = form.cleaned_data     # Process the data in form.cleaned_data
#         input1 = cd['x']
#         input2 = cd['y']
#         output = input1 + input2
#         return HttpResponseRedirect(request,'/thanks/')# Redirect to new url
#    else:
#         form = InputForm()   # An unbound form


#    return render(request, 'scraper/base.html', {'form': form })     


# def thanks(request,output):
# return render(request, 'scraper/base.html', output)

# from django import forms

# class InputForm(forms.Form):
#      x = forms.IntegerField(label='Value of x')
#      y = forms.IntegerField(label='Value of y')

# <html>
#   <head>
#   <title>Thanks</title>
#   </head>
#   <body>
#   <h1>Thanks</h1>
#   <h1> Output = {{output}} </h1>
#   </body>
#  </html>  
from django.shortcuts import render

def home(request):
	return render(request,'home.html')