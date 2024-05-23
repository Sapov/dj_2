from django import forms
from .models import *


class CalculatorForm(forms.Form):
    material = forms.ModelChoiceField(queryset=Material.objects.all(),
                                      label="Материал для печати",
                                      help_text="Выберите материал",
                                      initial=1)
    quantity = forms.FloatField(max_value=1000, label="Количество", initial=1)
    length = forms.FloatField(max_value=100, label="Длина в метрах")
    width = forms.FloatField(max_value=100, label="Ширина в метрах")

    finishka = forms.ModelChoiceField(queryset=FinishWork.objects.all(), label="Обработка", initial=True)