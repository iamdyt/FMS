from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth import get_user_model,logout
from . models import Dam,Department,Staff, Fish, TimeLine,Sales,Debtors
from django.contrib.auth.views import LoginView, TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,View
from .forms import LoginForm, DamForm,StaffForm,DebtorsForm, DepartmentForm,RegisterForm,FishForm,HarvestForm,SalesForm

# Create your views here.

class Index(TemplateView):
    template_name = 'fmsapp/home/index.html'
class Dashboard(LoginRequiredMixin,TemplateView):
    template_name = 'fmsapp/dashboard/index.html'
    login_url = 'fms:login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workerscount"] = Staff.objects.all().count()
        context["workers"] = Staff.objects.all()
        context['depts'] = Department.objects.all().count()
        context['fishes'] = Fish.objects.all().aggregate(Sum('total'))
        return context
    

class Login(LoginView):
    template_name = 'fmsapp/home/login.html'
    form_class = LoginForm
    model = get_user_model()
    def get_success_url(self):
        query = get_user_model().objects.get(pk=self.request.user.pk)
        self.request.session['username'] = query.username
        #self.request.session['']
        url = resolve_url('fmsapp:dashboard')
        return url

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('fmsapp:login', permanent=True)

class AccountUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'fms:login'
    model = get_user_model()
    form_class = RegisterForm
    template_name = 'fmsapp/account.html'
    success_url = reverse_lazy('fmsapp:dashboard')

class Register(CreateView):
    template_name = 'fmsapp/home/signup.html'
    form_class = RegisterForm
    model = get_user_model()
    success_url =  reverse_lazy('fmsapp:login')


class DamNew(LoginRequiredMixin,CreateView):
    login_url = 'fms:login'
    model = Dam
    form_class = DamForm
    template_name = 'fmsapp/dam/create.html'
    success_url = reverse_lazy('fmsapp:all_dam')

class DamList(LoginRequiredMixin,ListView):
    model = Dam
    login_url = 'fms:login'
    template_name = 'fmsapp/dam/index.html'
    context_object_name = 'damlist'

class DamEdit(LoginRequiredMixin,UpdateView):
    model = Dam
    login_url = 'fms:login'
    template_name = 'fmsapp/dam/edit.html'
    form_class = DamForm
    success_url = reverse_lazy('fms:all_dam')    

#Staff Controller
class StaffNew(LoginRequiredMixin,CreateView):
    model  = Staff
    login_url = 'fms:login'
    form_class = StaffForm
    template_name = 'fmsapp/staff/create.html'
    
class StaffSingle(LoginRequiredMixin,DetailView):
    model = Staff
    login_url = 'fms:login'
    template_name = 'fmsapp/staff/single.html'
    context_object_name = 'staffer'

class Staffers(LoginRequiredMixin,ListView):
    model = Staff
    login_url = 'fms:login'
    template_name = 'fmsapp/staff/index.html'
    context_object_name = 'staffs'

class StaffEdit(LoginRequiredMixin,UpdateView):
    model =Staff
    login_url = 'fms:login'
    template_name = 'fmsapp/staff/edit.html'
    form_class =  StaffForm

class StaffDestroy (LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect('fms:all_staff')

#Department Controller
class DepartmentNew(LoginRequiredMixin,CreateView):
    model = Department
    login_url = 'fms:login'
    form_class = DepartmentForm
    template_name  = 'fmsapp/department/create.html'

class DepartmentDetail(LoginRequiredMixin,DetailView):
    model = Department
    login_url = 'fms:login'
    template_name = 'fmsapp/department/index.html'
    context_object_name = 'dpt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        staff = Staff.objects.filter(department=pk)
        context["staffer"] = staff 
        return context
    

class DepartmentUpdate(LoginRequiredMixin,UpdateView):
    model = Department
    login_url = 'fms:login'
    template_name = 'fmsapp/department/edit.html'
    form_class = DepartmentForm

class DepartmentDestroy(LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request,pk):
        dept = Department.objects.get(pk=pk)
        dept.delete()
        return redirect('fms:dashboard')

#Fish Views

class AddFish(LoginRequiredMixin,CreateView):
    model = Fish
    login_url = 'fms:login'
    form_class = FishForm
    template_name = 'fmsapp/fish/create.html'
    success_url = reverse_lazy('fms:all_fish')

class UpdateFish(LoginRequiredMixin,UpdateView):
    model = Fish
    login_url = 'fms:login'
    form_class = FishForm
    template_name = 'fmsapp/fish/edit.html'
    success_url = reverse_lazy('fms:dashboard')

class ListFish(LoginRequiredMixin,ListView):
    model = Fish
    login_url = 'fms:login'
    template_name = 'fmsapp/fish/index.html'
    context_object_name = 'fishes'


class FishDestroy(LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request,pk):
        fish = Fish.objects.get(pk=pk)
        fish.delete()
        return redirect('fms:dashboard')

#Harvest Views
class AllHarvest(LoginRequiredMixin,ListView):
    model = TimeLine
    login_url = 'fms:login'
    template_name = 'fmsapp/timeline/index.html'
    context_object_name = 'timelines'

class AddHarvest(LoginRequiredMixin,CreateView):
    login_url = 'fms:login'
    model = TimeLine
    template_name = 'fmsapp/timeline/create.html'
    form_class = HarvestForm
    success_url = reverse_lazy('fms:harvests')

class EditHarvest(LoginRequiredMixin,UpdateView):
    login_url = 'fms:login'
    model = TimeLine
    template_name = 'fmsapp/timeline/edit.html'
    form_class = HarvestForm
    success_url = reverse_lazy ('fms:harvests')


class DeleteHarvest(LoginRequiredMixin,View):
    login_url = 'fms:login'

    def get(self, request,pk):
        harvest = TimeLine.objects.get(pk=pk)
        harvest.delete()
        return redirect('fms:harvests')

class SingleHarvest(LoginRequiredMixin,DetailView):
    model = TimeLine
    login_url = 'fms:login'
    template_name = 'fmsapp/timeline/single.html'
    context_object_name = 'harvest'

# Sales All
class SalesAdd(LoginRequiredMixin,CreateView):
    model = Sales
    login_url = 'fms:login'
    form_class = SalesForm
    template_name = 'fmsapp/sales/create.html'
    success_url = reverse_lazy('fms:sales')
class SalesAll(LoginRequiredMixin,ListView):
    login_url = 'fms:login'
    model = Sales
    template_name = 'fmsapp/sales/index.html'
    context_object_name = 'sales'

class SalesUpdate (LoginRequiredMixin,UpdateView):
    model = Sales
    login_url = 'fms:login'
    form_class = SalesForm
    template_name = 'fmsapp/sales/edit.html'
    success_url = reverse_lazy ('fms:sales')

class DeleteSales(LoginRequiredMixin,View):
    login_url = 'fms:login'

    def get(self, request,pk):
        sale = Sales.objects.get(pk=pk)
        sale.delete()
        return redirect('fms:sales')

#Creditors/Debitors
class DebtorsAdd(LoginRequiredMixin,CreateView):
    model = Debtors
    login_url = 'fms:login'
    form_class = DebtorsForm
    template_name = 'fmsapp/credit/create.html'
    success_url = reverse_lazy('fms:debts')
class DebtorsAll(LoginRequiredMixin,ListView):
    model = Debtors
    login_url = 'fms:login'
    template_name = 'fmsapp/credit/index.html'
    context_object_name = 'debts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = Debtors.objects.all().aggregate(Sum('amount'))
        return context
    

class DebtorsUpdate (LoginRequiredMixin,UpdateView):
    model = Debtors
    login_url = 'fms:login'
    form_class = DebtorsForm
    template_name = 'fmsapp/credit/edit.html'
    success_url = reverse_lazy ('fms:debts')

class DeleteDebtors(LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request,pk):
        debt = Debtors.objects.get(pk=pk)
        debt.delete()
        return redirect('fms:debts')