from django.shortcuts import render, redirect
from django.views import generic

from .models import Proyect, ProyectInstance

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def reg(request):
    if request.method=="POST":
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("<h1>Registration succesfully</h1>")
    else:
        user_form=RegistrationForm()
    return render(request, "registration.html", {"user_form": user_form})

from django.views.decorators.csrf import csrf_protect

from django.core.mail import send_mail
from django.conf import settings


def bid(request):
    if request.method =='POST':
        name=request.POST['name']
        proyect=request.POST['proyect']
        email=request.POST['email']
        date_acq=request.POST['date_acq']
        end_cont=request.POST['end_cont']
        amount=request.POST['amount']
        message = name + " se interesa en " + proyect + ". Su email es: " + email + ". Inicio: " + date_acq + ". Fin: " + end_cont + ". Monto: " + amount
        email_from=settings.EMAIL_HOST_USER,
        send_mail(
            'Puja',
            message,
            email_from,
            [email],
            
        
        )
        return render(request, 'index.html')
    return render(request, 'bid.html')
   
@csrf_protect
def login_buildout(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse("<h1> Disable account </h1>")
        else:
            return HttpResponse("<h1> Invalid login </h1>")
    else:
        pass
    return render(request, "login.html")


@login_required
def logout_buildout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def index(request):
    return render (request, 'index.html' )



class ProyectListView(generic.ListView):
    model = Proyect
    queryset = Proyect.objects.all()
    paginate_by = 10

class ProyectDetailView(generic.DetailView):
    model = Proyect

from django.contrib.auth.mixins import LoginRequiredMixin

class OwnedProyectsByUserListView(LoginRequiredMixin,generic.ListView):
    model = ProyectInstance
    template_name ='catalog/proyectinstance_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ProyectInstance.objects.filter(investor=self.request.user).order_by('date_acquired')
    
class OwnedProyectsByUserDetailView(LoginRequiredMixin,generic.DetailView):
    model = ProyectInstance
    template_name ='catalog/proyectinstance_detail_owned_user.html'
    paginate_by = 10
    context_object_name = 'pi'
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Proyect

from django.contrib.auth.mixins import PermissionRequiredMixin

class ProyectCreate(PermissionRequiredMixin, CreateView):
    model = Proyect
    fields = ['title','summary','mini_summary','company', 'date_published', 'expected_interest_rate']
    initial={'date_published':'01/01/2024'}
    permission_required = 'catalog.can_add_proyects'


class ProyectUpdate(PermissionRequiredMixin, UpdateView):
    model = Proyect
    fields = ['title','summary','mini_summary','company', 'date_published', 'expected_interest_rate']
    permission_required = 'catalog.can_add_proyects'

class ProyectDelete(PermissionRequiredMixin, DeleteView):
    model = Proyect
    success_url = reverse_lazy('proyects')
    permission_required = 'catalog.can_add_proyects'



class ProyectInstanceCreate(PermissionRequiredMixin, CreateView):
    model = ProyectInstance
    fields = ['id','proyect','date_acquired','date_of_end_contract', 'investment', 'investor']
    initial={'date_acquired':'01/01/2024', 'date_of_end_contract': '01/01/2024'}
    permission_required = 'catalog.can_add_instance_proyect'

class ProyectInstanceUpdate(PermissionRequiredMixin, UpdateView):
    model = ProyectInstance
    fields = ['id','proyect','date_acquired','date_of_end_contract', 'investment', 'investor']
    permission_required = 'catalog.can_add_instance_proyect'

class ProyectInstanceDelete(PermissionRequiredMixin, DeleteView):
    model = ProyectInstance
    success_url = reverse_lazy('proyects')
    permission_required = 'catalog.can_add_instance_proyect'





