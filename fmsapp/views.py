from django.shortcuts import render,redirect,resolve_url
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from . models import Dam,Department,Staff
from django.contrib.auth.views import LoginView, TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,View
from .forms import LoginForm, DamForm,StaffForm, DepartmentForm
# Create your views here.

class Dashboard(TemplateView):
    template_name = 'fmsapp/dashboard/index.html'

class Login(LoginView):
    template_name = 'fmsapp/login.html'
    form_class = LoginForm
    model = get_user_model()
    
    def get_success_url(self):
        query = get_user_model().objects.get(pk=self.request.user.pk)
        self.request.session['username'] = query.username
        #self.request.session['']
        url = resolve_url('fmsapp:dashboard')
        return url

class DamNew(CreateView):
    model = Dam
    form_class = DamForm
    template_name = 'fmsapp/dam/create.html'
    success_url = reverse_lazy('fmsapp:all_dam')

class DamList(ListView):
    model = Dam
    template_name = 'fmsapp/dam/index.html'
    context_object_name = 'damlist'
class DamEdit(UpdateView):
    model = Dam
    template_name = 'fmsapp/dam/edit.html'
    form_class = DamForm
    success_url = reverse_lazy('fms:all_dam')    

class StaffNew(CreateView):
    model  = Staff
    form_class = StaffForm
    template_name = 'fmsapp/staff/create.html'
    success_url = reverse_lazy('fmsap:all_staff')

class DepartmentNew(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name  = 'fmsapp/department/create.html'

class DepartmentDetail(DetailView):
    model = Department
    template_name = 'fmsapp/department/index.html'
    context_object_name = 'dpt'

class DepartmentUpdate(UpdateView):
    model = Department
    template_name = 'fmsapp/department/edit.html'
    form_class = DepartmentForm

class DepartmentDestroy(View):

    def get(self, request,pk):

        dept = Department.objects.get(pk=pk)
        dept.delete()
        return redirect('fms:dashboard')


