from typing import Any

from django.db.models.query import QuerySet
from reviews.models import Review
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    # form_class = ReviewForm
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    # def get(self, request):
    #    form = ReviewForm()

    #    return render(request, "reviews/review.html", {
    #        "form" : form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid(): 
    #         form.save() 
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form" : form
    #     })

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = "/"
    template_name = "reviews/delete.html"
        
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]="You review was submitted successfully!"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    