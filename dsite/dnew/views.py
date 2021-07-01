from django.shortcuts import render, redirect
from .forms import PersonForm, UserForm
from .models import Person, User
from django.http import HttpResponse
from django.views.generic.list import ListView


def index(request):
	# context ={"test":"member",
	# 			"list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# }
	form = Person.objects.all()
	return render(request, 'index.html', {'data': form})

def form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = PersonForm()

    return render(request, 'form.html', {'form': form})

def detail(request, id):
	sel= Person.objects.get(id=id)
	return render(request, 'detail.html', {'data': sel})

def update(request, id):
	sel = Person.objects.get(id=id)
	if request.method == 'POST':
		form = PersonForm(request.POST, instance=sel)
		form.save()
		return redirect('index')
	else:
		form = PersonForm(instance=sel)
	return render(request, 'form.html', {'form': sel})

def delete(request, id):
	sel= Person.objects.get(id=id)
	sel.delete()
	return redirect('index')


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=PersonForm()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'posts/create.html')  

        else:
                return render(request,'posts/create.html')

# Login System #
def home(request):
	if request.session['isLogged']:
		current_user = request.session['user']
		param = {'current_user': current_user}
		return render(request, 'lbase.html', param)
	else:
		return redirect('login')
	return render(request, 'login.html')

def signup(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')
        # print(uname, pwd)
		if User.objects.filter(username=uname).count()>0:
			return HttpResponse('Username already exists.')
		else:
			user = User(username=uname, password=pwd)
			user.save()
			return redirect('login')
	else:
		return render(request, 'signup.html')

def login(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')

		check_user = User.objects.filter(username=uname, password=pwd)
		if check_user:
			request.session['user'] = uname
			request.session['isLogged'] = True
			return redirect('home')
		else:
			return HttpResponse('Please enter valid Username or Password.')
	else:
		# request.session['isLogged'] = False
		if request.session['isLogged']:
			return redirect('home')
		else:
			return render(request, 'login.html')
		

def logout(request):
	try:
		del request.session['isLogged']
		request.session['isLogged'] = False
	except:
		return redirect('login')
	return redirect('login')