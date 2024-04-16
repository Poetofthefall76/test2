from django.shortcuts import render
from django.views.generic import CreateView, View
from . import models, forms


class ProfileView(CreateView):
    template_name = "main/profile-view.html"
    queryset = models.UserProfile.objects.all()
    form_class = forms.ProfileForm
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form=form)


class ProductView(CreateView):
    template_name = "main/product-view.html"
    form_class = forms.ProductForm
    success_url = "/"
    queryset = models.Product.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)


class NotificationView(View):
    def get(self, request):
        return render(request, 'notification.html')