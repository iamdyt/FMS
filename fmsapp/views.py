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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workerscount"] = Staff.objects.all().count()
        context["workers"] = Staff.objects.all()
        context['depts'] = Department.objects.all().count()
        #context['fishes'] 
        return context
    

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

#Staff Controller
class StaffNew(CreateView):
    model  = Staff
    form_class = StaffForm
    template_name = 'fmsapp/staff/create.html'
    
class StaffSingle(DetailView):
    model = Staff
    template_name = 'fmsapp/staff/single.html'
    context_object_name = 'staffer'

class Staffers(ListView):
    model = Staff
    template_name = 'fmsapp/staff/index.html'
    context_object_name = 'staffs'

class StaffEdit(UpdateView):
    model =Staff
    template_name = 'fmsapp/staff/edit.html'
    form_class =  StaffForm

class StaffDestroy (View):
    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect('fms:all_staff')

#Department Controller
class DepartmentNew(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name  = 'fmsapp/department/create.html'

class DepartmentDetail(DetailView):
    model = Department
    template_name = 'fmsapp/department/index.html'
    context_object_name = 'dpt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        staff = Staff.objects.filter(department=pk)
        context["staffer"] = staff 
        return context
    

class DepartmentUpdate(UpdateView):
    model = Department
    template_name = 'fmsapp/department/edit.html'
    form_class = DepartmentForm

class DepartmentDestroy(View):

    def get(self, request,pk):
        dept = Department.objects.get(pk=pk)
        dept.delete()
        return redirect('fms:dashboard')