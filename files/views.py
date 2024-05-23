from django.forms import model_to_dict
from django.shortcuts import render

from .forms import CalculatorForm
from .models import Material, FinishWork, UseCalculator


# Create your views here.
def index():
    ...


def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            length = request.POST["length"]
            width = request.POST["width"]
            quantity = request.POST["quantity"]
            material = request.POST["material"]
            finishka = request.POST["finishka"]

            materials = Material.objects.get(id=material)
            finishkas = FinishWork.objects.get(id=finishka)
            perimetr = (float(width) + float(length)) * 2
            material_price = materials.price_customer_retail
            finishka_price = finishkas.price_customer_retail
            finishka_price = perimetr * finishka_price
            results = (float(width) * float(length) * material_price) + finishka_price  # в см
            results = round(results, -1) * int(quantity)
            if results < 1000:  # если сумма получилась менее 1000 руб. округляю до 1000 руб.
                results = 1000

            # UseCalculator.objects.create(**form.cleaned_data)
            # return render(request, "files/calculator.html", {"form": form,
            #                                                  "title": "Калькулятор печати",
            #                                                  "results": results,
            #                                                  },
            #               )
            try:
                UseCalculator.objects.create(material=materials, quantity=quantity, width=width, length=length,
                                             results=results, FinishWork=finishkas)
                return render(request, "files/calculator.html", {"form": form,
                                                                 "title": "Калькулятор печати",
                                                                 "results": results,
                                                                 },
                              )

            except:
                form.add_error(None, 'Ошибка расчета')


    else:
        form = CalculatorForm()

    return render(request, 'files/calculator.html', {'form': form, 'title': 'Калькулятор'})


def view_calculator(request):
    items = UseCalculator.objects.all()
    return render(request, 'files/view_calculator.html', {'items': items, 'title': 'Расчеты'})
