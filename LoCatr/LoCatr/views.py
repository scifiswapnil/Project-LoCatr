from django.shortcuts import render
from django import forms
from models import pumps_stations,Rusers

class registerer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Rusers
        fields = ('name', 'email', 'password', 'address_line1', 'address_line2', 'telephone', 'zip_code', 'state')

def register(request):
    if request.method == "POST":
        form = registerer(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            error = "registration successful";
            return render(request, 'LoCatr/index.html', {'error': error})
    else:
        form = registerer()
        return render(request, 'LoCatr/register.html', {'form': form})

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

def login(request):
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            password = MyLoginForm.cleaned_data['password']
            results = Rusers.objects.filter(name=username)
            if len(results) != 0:
                if results[0].password == password:
                    request.session['username'] = username
                    return render(request, 'LoCatr/home.html', {"username": username})
            else:
                error = "registration successful";
                return render(request, 'LoCatr/index.html', {'error': error})
        else:
            error = "registration successful";
            return render(request, 'LoCatr/index.html',{'error':error})
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'LoCatr/home.html', {'username': username})
    else:
        return render(request, 'LoCatr/index.html')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request,'LoCatr/index.html')



# def post_new(request):
#     if request.method == "POST":
#         form = register(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return render(request, 'music/index.html', {'form': form})
#     else:
#         form = register()
#     return render(request, 'music/post_edit.html', {'form': form})

# if request.method == "POST":
#     try:
#         tname = request.POST['username']
#         passwd = request.POST['password']
#         results = Rusers.objects.filter(name=tname)
#         if results[0].password == passwd:
#             return render(request, 'LoCatr/home.html')
#         else:
#             return render(request, 'LoCatr/index.html',{'error' : 'login fail'})
#     except:
#         return render(request, 'LoCatr/index.html', {'error': 'login fail'})
