from django.http import HttpResponse
from django.shortcuts import render
from .forms import PeselForm


# Create your views here.
def pesel_validation_view(request):
    result = None
    if request.method == "POST":
        form = PeselForm(request.POST)
        form.is_valid()

        pesel_result = form.cleaned_data["result"]

        # Extract data from operation result
        if not pesel_result["is_valid"]:
            result = "PESEL is not valid. Reason: " + str(pesel_result["reason"])
        else:
            result = "PESEL is valid, Birth date: " + str(pesel_result["birth_date"]) + ", Gender: " + str(pesel_result["gender"])
    else:
        form = PeselForm()

    return render(request, "index.html", {"form": form, "result": result})
