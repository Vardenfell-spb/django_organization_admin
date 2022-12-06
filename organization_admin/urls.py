from django.contrib import admin
from django.urls import path
from django.urls import include

from accounts.views import AccountsLoginView, AccountsLogoutView

urlpatterns = [
    path('login/', AccountsLoginView.as_view(), name='login'),
    path('logout/', AccountsLogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
