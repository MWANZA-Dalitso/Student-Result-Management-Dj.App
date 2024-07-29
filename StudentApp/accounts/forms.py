from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile, University, LevelOfStudy
from .utils import get_academic_years

def validate_passport_number(value):
    if not value.startswith('ZN') or len(value) != 8:
        raise ValidationError('Passport number must start with "ZN" and be 8 characters long.')

def validate_phone_number(value):
    if not value.startswith('+212') or len(value) != 13:
        raise ValidationError('Phone number must start with "+212" and be 13 characters long.')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-control medium',
                'placeholder': f'Enter {fieldname.capitalize()}'
            })

class ProfileForm(forms.ModelForm):
    city = forms.CharField(max_length=100, required=False)
    passport_number = forms.CharField(label='Passport Number', max_length=8, required=False)
    phone_number = forms.CharField(label='Phone Number', max_length=13, required=False)
    bc_number = forms.CharField(label='BC Number', max_length=100)
    university = forms.ModelChoiceField(queryset=University.objects.all(), empty_label="Select University")
    level_of_study = forms.ModelChoiceField(queryset=LevelOfStudy.objects.all(), empty_label="Select Level of Study")
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    inscription_year = forms.ChoiceField(choices=get_academic_years(), label='Inscription Year')
    city_of_birth = forms.CharField(max_length=100, required=False)  # Updated
    province_of_birth = forms.CharField(max_length=100, required=False)  # Updated

    class Meta:
        model = Profile
        fields = [
            'student_name', 'email', 'phone_number', 'passport_number',
            'date_of_birth', 'bc_number', 'university', 'program_of_study',
            'level_of_study', 'city', 'avatar', 'civil_status', 'gender',
            'city_of_birth', 'province_of_birth', 'province_in_morocco',
            'postal_code', 'address', 'inscription_year'
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-control medium',
                'placeholder': f'Enter {fieldname.capitalize()}'
            })

    def clean_passport_number(self):
        passport_number = self.cleaned_data.get('passport_number')
        if passport_number and (not passport_number.startswith('ZN') or len(passport_number) != 8):
            raise ValidationError('Passport number must start with "ZN" and be 8 characters long.')
        return passport_number

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and (not phone_number.startswith('+212') or len(phone_number) != 13):
            raise ValidationError('Phone number must start with "+212" and be 13 characters long.')
        return phone_number

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['student_name', 'email', 'date_of_birth', 'passport_number', 'bc_number',
                  'phone_number', 'program_of_study', 'level_of_study', 'university', 'city_of_birth',
                  'province_of_birth', 'province_in_morocco', 'postal_code', 'address',
                  'inscription_year', 'avatar', 'civil_status', 'gender']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['student_name', 'email', 'phone_number', 'passport_number',
                  'program_of_study', 'level_of_study', 'university', 'city_of_birth',
                  'province_of_birth', 'province_in_morocco', 'postal_code', 'address',
                  'inscription_year', 'avatar', 'civil_status', 'gender']

class UserEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
