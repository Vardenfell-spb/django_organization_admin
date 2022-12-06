from django.urls import path
from accounts.views import AccountsLoginView, MainView, LogoutView, OgrUserListView, UserCreateView, UserDetailView, \
    UserEditView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('accounts/user_list/', OgrUserListView.as_view(), name='user_list'),
    path('accounts/user_create/', UserCreateView.as_view(), name='user_create'),
    path('accounts/<int:user_id>/user_edit/', UserEditView.as_view()),
    path('accounts/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
]