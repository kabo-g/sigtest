from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect


from . models import Signature
# Create your views here.

class SignatureView(View):

    model = Signature
    template_name = "index.html"
    context = {"model" : model}

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)


    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            signature = request.POST.get('signature')

            self.model.create(
                firstname = firstname, lastname = lastname,
                email = email, signature = signature
            )
            self.model.save()

            if self.model.save():
                print("successfully saved to db")

        return redirect(request.path)



class EditSignature(View):

	template_name = 'data.html'
