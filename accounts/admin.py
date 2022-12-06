from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import Organization, Profile


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.unregister(User)


class ProfileInLine(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'get_organization']
    list_filter = ['username']
    inlines = [ProfileInLine]

    def get_organization(self, instance):
        return instance.profile.organization
    get_organization.short_description = 'Organization'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)
