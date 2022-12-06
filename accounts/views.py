from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic, View

from accounts.forms import AuthForm, RegisterForm, UserEditForm
from accounts.models import Profile


class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = '/'


class AccountsLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class MainView(View):
    def get(self, request):
        return render(request, 'accounts/main.html')


class OgrUserListView(View):

    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            organization = request.user.profile.organization
            user_list = map(lambda x: x.user, Profile.objects.filter(organization=organization))
            if user_list:
                context['user_list'] = user_list
        return render(request, 'accounts/user_list.html', context=context)


class UserCreateView(View):
    def get(self, request):
        if request.user.has_perm('auth.add_user'):
            context = {'user_form': RegisterForm()}
            return render(request, 'accounts/user_create.html', context=context)
        else:
            return HttpResponse('You have no permission for create users')

    def post(self, request):
        if request.user.has_perm('auth.add_user'):
            user_form = RegisterForm(request.POST)
            user_organization = request.user.profile.organization
            if user_form.is_valid():
                new_user = user_form.save()
                new_user.profile.organization = user_organization
                new_user.profile.save()
                return HttpResponseRedirect('/accounts/user_list')
            context = {'user_form': user_form}
            return render(request, 'accounts/user_create.html', context=context)
        else:
            return HttpResponse('You have no permission for create users')


class UserDetailView(View):

    def get(self, request, user_id):
        context = {}
        user = User.objects.get(id=user_id)
        context['object'] = user

        return render(request, 'accounts/user_detail.html', context=context)


class UserEditView(View):

    def get(self, request, user_id):
        if request.user.has_perm('auth.change_user'):
            user = User.objects.get(id=user_id)
            user_form = UserEditForm(instance=user)
            # profile_form = ProfileEditForm(instance=user.profile)
            return render(request, 'accounts/user_edit.html', context={'user_form': user_form,
                                                                       # 'profile_form': profile_form,
                                                                       'user_id': user_id})
        else:
            return HttpResponse("You can't edit profiles")

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user_form = UserEditForm(request.POST, instance=user)
        # profile_form = ProfileEditForm(request.POST, instance=user.profile)
        if user_form.is_valid(): # and profile_form.is_valid():
            user.save()
            # user.profile.save()
            return HttpResponseRedirect(f'/accounts/{user_id}/')

