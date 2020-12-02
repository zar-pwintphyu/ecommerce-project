from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.conf import settings
from django.core.mail import send_mail
from phone_field import PhoneField
from django.contrib.admin.widgets import AdminDateWidget




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True,label='姓 ')
    last_name = forms.CharField(max_length=100, required=True,label='名')
    zip11 = forms.RegexField(
        regex=r'^[0-9]+$',
        max_length=7,
        label='郵便番号  ※ハイフン「-」は入力不要です。',
        widget=forms.TextInput(attrs={'onKeyUp' : "AjaxZip3.zip2addr(this,'','addr11','addr11')"}),
    )
    addr11 = forms.CharField(label='都道府県.市区町村')
    addr12 = forms.CharField(label='番地.マンション名等')
    email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com',label='メールアドレス')
    email1 = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com',label='メールアドレス(確認用)')

    phone = forms.CharField(max_length=100,label='電話番号')
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=[x for x in range(1930, 2020)]),label='生年月日')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','phone','birthday', 'zip11','addr11','addr12','email','email1','password1', 'password2',)

    