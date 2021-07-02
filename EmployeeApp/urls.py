from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^department$',views.departmentApiDjango),
    url(r'^department/([0-9]+)$',views.departmentApiDjango),

    url(r'^employee$',views.employeeApiDjango),
    url(r'^employee/([0-9]+)$',views.employeeApiDjango),

    url(r'^employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)