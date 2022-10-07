from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseError


from . models import Signature
# Create your views here.

class SignatureView(View):

    model = Signature
    template_name = ""
    context = {}

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)


    def post(self, request, *args, **kwargs):

        return redirect(request.path)
