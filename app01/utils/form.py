from app01 import models
from django import forms
from django.core.validators import RegexValidator, ValidationError
from app01.utils.bootstrap import BootstrapModelForm






class UserModelForm(BootstrapModelForm):
    name = forms.CharField(max_length=10, label="Name")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "balance", "entry_time", "gender", "depart"]

class MobileModelForm(BootstrapModelForm):
    # Check the form of phone number input
    mobile = forms.CharField(max_length=13,
                             label="Mobile",
                             validators=[RegexValidator(r'^1[3-9]\d{9}$', 'Wrong mobile number'), ],
                             )

    class Meta:
        model = models.AccountAdmin
        fields = ["mobile", "price", "level", "status"]


    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.AccountAdmin.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            # Validation fails
            raise ValidationError("The number has already existed")
        return txt_mobile
