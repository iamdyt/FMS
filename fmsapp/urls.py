from django.urls import path
from . import views

app_name = 'fmsapp'

urlpatterns = [
    path('', views.Login.as_view(), name='loginform' ),
    path("dashboard/", views.Dashboard.as_view(), name="dashboard"),
   
   #Dam Routes

   path("dashboard/dam/new", views.DamNew.as_view(), name="create_dam"),
   path("dashboard/dam/", views.DamList.as_view(), name="all_dam"),
   path("dashboard/dam/<int:pk>/edit/", views.DamEdit.as_view(), name="dam_edit"),

   #Staff Path
   #path("dashboard/staff/new/", .as_view(), name="create_staff"),
   #path("dashboard/staff/", .as_view(), name="all_staff"),

   #Department Routes

   path("dashboard/department/new/",views.DepartmentNew.as_view(), name="create_dept"),
   path("dashboard/department/<int:pk>/single/",views.DepartmentDetail.as_view(), name="dept_single"),
   path("dashboard/department/<int:pk>/edit/",views.DepartmentUpdate.as_view(), name="dept_edit"),
   path("dashboard/department/<int:pk>/delete/",views.DepartmentDestroy.as_view(), name="dept_delete"),
]
