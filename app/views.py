from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from app.forms import ListForm, NewUserForm
from .models import FAQ, Listing, Service,Team
from django.shortcuts import redirect, render,HttpResponse

 

# Create your views here.
def home(request):
    posts = Service.objects.all()
    fs = FAQ.objects.all()
    ts = Team.objects.all()
    if fs:
        print(fs)

    context = {"fs":fs, "posts":posts,'ts':ts}
    return render(request, "index.html", context)

 



@login_required(login_url=reverse_lazy('login'))
def businesslist(request):
    blist = ListForm()
    if request.method =='POST':
        blist = ListForm(request.POST)
        if blist.is_valid():
            blist.save()
            messages.success(request,("Your business is successfully added!"))
        else:
            messages.error(request,"Error saving form")
            print("error occured")

        return redirect("/")
    
    # listing = Listing.objects.all()

    return render(request,'add-listing.html',{'blist':blist})



def packages(request):
    return render(request,'digitalmarketing.html')



def seo(request):
    return render(request,'seo.html')





# class Register (CreateView):
#     template_name = "registration/register.html"
#     form_class = UserCreationForm
#     success_url = reverse_lazy('register-success')

#     def form_valid(self,form):
#         form.save()
#         return HttpResponseRedirect(self.success_url)


# def Register(request):
#     if request.method == 'POST':  # if the request is a 'post' then it will create a form
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#                 username = form.cleaned_data.get('username')
#                 messages.success(request, f'Account created for {username}!')
#                 return redirect('login')
#     else:
#         form = UserCreationForm()  # anything not a post request it will create a blank form
#     return render(request, 'registration/register.html', {'form': form})




def Register(request):
    if request.method =="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request,user)
            messages.error(request,'Registeration Successful')
            return redirect('login')

        messages.error(request,'Registeration un Successful')
    form = NewUserForm()
    return render(request=request,template_name='registration/register.html',context={'form': form})

    


# def Search(request):
#         search = Listing.objects.all()
#         return render(request,'add-listing.html',{'search':search})



from django.db.models import Q

@login_required(login_url=reverse_lazy('login'))
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(listing_title__icontains=query) | Q(description__icontains=query)

            results= Listing.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'add-listing.html', context)

        else:
            return render(request, 'add-listing.html')

    else:
        return render(request, 'add-listing.html')


