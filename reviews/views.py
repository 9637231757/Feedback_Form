from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
#from django.views.generic.edit import FormView 
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review
# using class
# update this by using class
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
         
        
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html" 
    model = Review
   
class AddFavouriteView(View):
    def post(self, requests):   
        review_id = request.POSTS['review_id']
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = fav_review
        return HttpResponseRedirect("/reviews/" + review_id)
 
       
        
         

