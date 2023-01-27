from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import DetailView

from .forms import UserForm
from .models import Product

# Create your views here.


def box(request):
    return HttpResponse("<h1>Hello </h1>") #проверка


def main(request):
    return TemplateResponse(request, "main.html")#1a whole page


def base(request):
    return render(request, "base.html")


def base2(request):
    return render(request, "base2.html")


# def base3(request):
#     return render(request, "base3.html")


def base4(request):
    return render(request, "base4.html")


# def base5(request):
#     return render(request, "base5.html")


# def post(request):
#     return HttpResponse("<p>Сообщение успешно отправлено!</p><p>Спасибо за обратную связь</p>")


def post(request):
    return render(request, "index.html")


def review(request):
    return render(request, "payment.html")


def review2(request):
    return render(request, "payment2.html")


def review3(request):
    return render(request, "payment3.html")


def review4(request):
    return render(request, "payment4.html")


def review5(request):
    return render(request, "payment5.html")


def congratulation(request):
    return render(request, "index2.html")


def card(request):
    return render(request, "card.html")


def card2(request):
    return render(request, "card2.html")


def card3(request):
    return render(request, "card3.html")


def card4(request):
    return render(request, "card4.html")


def card5(request):
    return render(request, "card5.html")


def card6(request):
    return render(request, "card6.html")


def card7(request):
    return render(request, "card7.html")


def card8(request):
    return render(request, "card8.html")


def card9(request):
    return render(request, "card9.html")


def card10(request):
    return render(request, "card10.html")


def card11(request):
    return render(request, "card11.html")


def card12(request):
    return render(request, "card12.html")


def pay(request):
    return render(request, "PAYCARD.HTML.html")


# def postuser(request):
#     name = request.POST.get("name", "Undefined")
#     email = request.POST.get("email", "Undefined")
#     comment = request.POST.get("comment", "Undefined")
#     return HttpResponse(f"<h3>Enter name:</h3> {name} <br> <h3>Enter email:</h3> {email} <br> "
#                         f"<h3>Your comment:</h3> {comment}")


def contact(request):
    forms = UserForm()
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data["name"]
            email = forms.cleaned_data["email"]
            # message = forms.cleaned_data["message"]
            return TemplateResponse(request, "postm.html")
        else:
            return TemplateResponse(request, "postm2.html")
    return render(request, "base5.html", context={"forms": forms})


def table(request):
    return render(request, "base5.html")


def base55(request):
    return render(request, "base5.5.html")


def read(request):
    products = Product.objects.all()
    return render(request, "base3.html", context={"products":products})


def message(request):
    return render(request, "postm.html")


def message2(request):
    return render(request, "postm2.html")


class PostDetailView(DetailView):
    model = Product
    template_name = "card.html"
    context_object_name = "product"


class PostDetailView2(DetailView):
    model = Product
    template_name = "payment.html"
    context_object_name = "total"
