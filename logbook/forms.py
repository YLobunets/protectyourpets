from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from core.models import Person


class PersonForm(forms.ModelForm):
    # MIN_BIRTH_YEAR = 1900

    # второй подход проверки данных
    # birth_year = forms.IntegerField(
    #     required=True,
    #     validators=[MinValueValidator(MIN_BIRTH_YEAR)]
    # )

    class Meta:
        model = Person
        # fields = "__all__"
        fields = ("id", "full_name", "birth_year", "hobby")

    # первый подход проверки данных
    # def clean_birth_year(self):
    #     birth_year = self.cleaned_data["birth_year"]
    #     if birth_year < PersonForm.MIN_BIRTH_YEAR:
    #         raise ValidationError(f"Ensure that value is >= {PersonForm.MIN_BIRTH_YEAR}")
    #
    #     return birth_year


class PersonFormOld(forms.Form):
    full_name = forms.CharField(max_length=255, required=True)
    birth_year = forms.IntegerField(required=True)
    hobby = forms.CharField(max_length=255, required=False)
