from django.shortcuts import render,redirect
from django import forms
from models import Rusers
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.core.urlresolvers import reverse_lazy


class indexview(generic.ListView):
    template_name = 'LoCatr/render.html'
    context_object_name = 'form'
    def get_queryset(self):
        return Rusers.objects.all()

class updateview(generic.UpdateView):
    model = Rusers
    context_object_name = 'form'
    fields = ('name', 'email', 'password', 'pump_name', 'address_line1', 'address_line2', 'telephone', 'zip_code', 'state',
    'pump_status')


class registerer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Rusers
        fields = ('name', 'email', 'password','pump_name' , 'address_line1', 'address_line2', 'telephone', 'zip_code', 'state', 'pump_status')
    def check(self):
        name = self.cleaned_data.get('name')
        if Rusers.objects.filter(name=name).exists():
            return False
        else:
            return True

def register(request):
    if request.method == "POST":
        form = registerer(request.POST)
        if form.is_valid():
            if form.check():
                post = form.save(commit=False)
                post.save()
                error = "registration successful"
                return render(request, 'LoCatr/login.html',{'success':error})
            else:
                error = "User name already exists"
                return render(request, 'LoCatr/register.html', {'error': error})
    else:
        form = registerer()
        return render(request, 'LoCatr/register.html', {'form': form})


class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   def check(self):
       username = self.cleaned_data.get('username',False)
       password = self.cleaned_data.get('password',False)
       results = Rusers.objects.filter(name=username).first()
       if results!= None and results.password == password:
           return True
       return False
def login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        result = Rusers.objects.filter(name=username).first()
        request.session['username'] = username
        return render(request, 'LoCatr/home.html', {"username": result})
    elif request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid() and MyLoginForm.check():
            username = MyLoginForm.cleaned_data['username']
            result = Rusers.objects.filter(name=username).first()
            request.session['username'] = username
            return render(request, 'LoCatr/home.html', {"username": result})
        else:
            error = "wrong username or password";
            return render(request, 'LoCatr/login.html',{'error':error})
    else:
        return render(request, 'LoCatr/login.html')


def home(request):
    if request.session.has_key('username'):
        username = request.session['username']
        result = Rusers.objects.filter(name=username).first()
        request.session['username'] = username
        return render(request, 'LoCatr/home.html', {"username": result})
    else:
        return redirect('index')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('index')


def update(request,id):
    username = request.session['username']
    results = Rusers.objects.filter(id=id).first()
    cmpr = Rusers.objects.filter(name=username).first()
    if results.name == cmpr.name:
        if cmpr.pump_status == True:
            cmpr.pump_status = False
            cmpr.save()
        else:
            cmpr.pump_status = True
            cmpr.save()
    return redirect('home')
