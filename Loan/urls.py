from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.index,name='home'),
    path('',include('LoanDeployment.urls'))
]

