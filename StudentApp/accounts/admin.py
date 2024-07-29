from django.contrib import admin
from .models import Profile, University, LevelOfStudy, ProvinceOfBirth, CityOfBirth

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_name', 'email', 'university', 'level_of_study']
    list_filter = ['university', 'level_of_study']
    search_fields = ['user__username', 'student_name', 'email']

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(LevelOfStudy)
class LevelOfStudyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ProvinceOfBirth)
class ProvinceOfBirthAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(CityOfBirth)
class CityOfBirthAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_province_of_birth']  # Adjusted list_display
    list_filter = ['province_of_birth']  # Adjusted list_filter
    search_fields = ['name', 'province_of_birth__name']  # Adjusted search_fields

    def get_province_of_birth(self, obj):
        return obj.province_of_birth.name if obj.province_of_birth else ''

    get_province_of_birth.short_description = 'Province of Birth'
