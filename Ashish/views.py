# from django.http import HttpResponse

# def hello(request):
# 	return HttpResponse("<p>This is may first App<p><br><a href=''></a>")
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<title> Menu </title><head> Menu </head><br><a href='http://google.com'>1. Google</a><br><a href='http://facebook.com'>2. Facebook</a><br><a href='http://youtube.com'>3. youtube</a><br><a href='/'>4. Back</a><br>")

# def main(request):
# 	return HttpResponse("<p> Welcome to Django Website<p><br><a href=/menu>Menu</a>")
# from django.http import HttpResponseRedirect
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
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'index.html')
def add(request):
	a=int(request.GET.get('num1'))
	b=int(request.GET.get('num2'))
	addition=request.GET.get('add','off')
	sub= request.GET.get('sub','off')
	mul=request.GET.get('mul','off')
	div=request.GET.get('div','off')

	if addition=="on":
		re=a+b
		params ={'A':re,'b':'Addition:'}
	elif sub=="on":
		re=a-b
		params={'A':re,'b':'Substraction:'}
	elif mul=="on":
		re = a*b
		params={'A':re,'b':'Multiply:'}
	elif div =="on":
		re=a//b
		params={'A':re,'b':'Divide:'}
	return render(request,'add.html',params)



