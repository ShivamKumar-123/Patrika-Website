from django.shortcuts import render,redirect
from .models import AllCards,Members,NewArrival,FeedBack
from .forms import CustomSignUpForm,FeedbackForm
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def allCards(request):
    allCards = AllCards.objects.all()

    return render(request,'component/all_card.html',{'allCards': allCards})



def home(request):
    # return HttpResponse("Hello world. You are at chai aur Django Home page")
    return render(request, 'website/index.html')

@login_required
def about(request):
    members = Members.objects.all()
    return render(request,"component/about_us.html",{"members":members})


@login_required
def newArrival(request):
    books = NewArrival.objects.all()
    return render(request, 'component/newArrival.html',{'books': books})


class FeedBackView(LoginRequiredMixin, View):
    login_url = '/login/'  # Optional: redirect URL if not logged in
    redirect_field_name = 'next'  # Optional: default is 'next'

    def get(self, request):
        form = FeedbackForm()
        return render(request, 'component/feedbackGive.html', {'form': form})

    

def signup_view(request):
    if request.method == "POST":
        form = CustomSignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')

    else:
        form = CustomSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def feedBackShow(request):
    feedbacks = FeedBack.objects.all()
    return render(request, 'component/feedbackShow.html', {'feedbacks': feedbacks})
