from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm
from .shuffler import shuffle_text

# Create your views here.
def home(request):
    result_text = None

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            text = file.read().decode("utf-8")
            result_text = shuffle_text(text)

            request.session["result_text"] = result_text
            return redirect(reverse("result"))
    else:
        form = UploadFileForm()

    return render(request, "index.html", {"form": form, "result": result_text})


def result(request):
    result_text = request.session.get("result_text", "")
    return render(request, "result.html", {"result": result_text})