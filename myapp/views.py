from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage


from . models import Signature
# Create your views here.

class SignatureView(View):

    model = Signature
    template_name = "index.html"
    context = {"model" : model}

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)


    def post(self, request, *args, **kwargs):

        if request.method == "POST" and request.FILES == 'signaturePreview':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            signature = request.FILES.get('signaturePreview')

            fs = FileSystemStorage()
            filename = fs.save(signature.name, signature)
            uploaded_file_url = fs.url(filename)

            print(signature)

            sig = self.model.objects.create(
                firstname = firstname, lastname = lastname,
                email = email, signature = signature
            )
            sig.save()

            if sig.save():
                print("successfully saved to db")

        return redirect(request.path)



class EditSignature(View):

	template_name = 'data.html'
