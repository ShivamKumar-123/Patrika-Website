from django.shortcuts import render,redirect,get_object_or_404
from .models import AllCards,Members,NewArrival,FeedBack
from .forms import CustomSignUpForm,FeedbackForm,UpdateCardsAndDelete,MemberDetail
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages



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
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        form = FeedbackForm()
        return render(request, 'component/feedbackGive.html', {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Saves data to the FeedBack model
            messages.success(request, "Thank you for your feedback!")
            return redirect('feedback_thankyou')  # Redirect to a success/thank you page (define in urls/views)
        return render(request, 'component/feedbackGive.html', {'form': form})

def feedback_thankyou(request):
    return render(request, 'component/feedback_thankyou.html')

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



# app password----
# mrms quzm ziou nbvl


def updateCard(request, card_id):
    card = get_object_or_404(AllCards, pk=card_id)

    if request.method == "POST":
        form = UpdateCardsAndDelete(request.POST, request.FILES)
        if form.is_valid():
            # Update fields manually
            card.name = form.cleaned_data['name']
            card.description = form.cleaned_data['description']
            card.urls = form.cleaned_data['urls']
            card.type = form.cleaned_data['type']

            # Only update image if a new one was uploaded
            if form.cleaned_data.get('image'):
                card.image = form.cleaned_data['image']

            card.save()
            return redirect('allcard')

    else:
        # Pre-fill non-file fields only
        form = UpdateCardsAndDelete(initial={
            'name': card.name,
            'description': card.description,
            'urls': card.urls,
            'type': card.type
            # Do not include 'image' in initial
        })

    # Pass card to template to show current image
    return render(request, 'component/updation.html', {'form': form, 'card': card})


def deleteCard(request, card_id):
    card = get_object_or_404(AllCards, pk=card_id)

    if request.method == "POST":
        card.delete()
        return redirect('allcard')  # Make sure 'allcard' is the correct URL name

    # Optionally, you can show a confirmation page before deleting:
    return render(request, 'component/delete_confirmation.html', {'card': card})


def updateCardNewArrival(request, card_id):
    card = get_object_or_404(NewArrival, pk=card_id)  # assuming your model is named NewArrival

    if request.method == "POST":
        form = UpdateCardsAndDelete(request.POST, request.FILES)
        if form.is_valid():
            card.name = form.cleaned_data['name']
            card.description = form.cleaned_data['description']
            card.urls = form.cleaned_data['urls']
            card.type = form.cleaned_data['type']

            if form.cleaned_data.get('image'):
                card.image = form.cleaned_data['image']

            card.save()
            return redirect('newArrival')  # change to the correct redirect view name
    else:
        form = UpdateCardsAndDelete(initial={
            'name': card.name,
            'description': card.description,
            'urls': card.urls,
            'type': card.type
        })

    return render(request, 'component/updateNewArrival.html', {'form': form, 'card': card})

def deleteCardNewArrival(request, card_id):
    card = get_object_or_404(NewArrival, pk=card_id)

    if request.method == "POST":
        card.delete()
        return redirect('newArrival')  # Make sure 'newarrival' is the correct URL name

    return render(request, 'component/delete_confirmation_newarrival.html', {'card': card})




# Update Feedback
def updateFeedback(request, feedback_id):
    feedback = get_object_or_404(FeedBack, id=feedback_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Feedback updated successfully.")
            return redirect('feedback_show')  # Change to your feedback list page
    else:
        form = FeedbackForm(instance=feedback)

    return render(request, 'component/update_feedback.html', {'form': form})

# Delete Feedback
def deleteFeedback(request, feedback_id):
    feedback = get_object_or_404(FeedBack, id=feedback_id)

    if request.method == 'POST':
        feedback.delete()
        messages.success(request, "Feedback deleted successfully.")
        return redirect('feedbackShow')

    return render(request, 'component/confirm_delete_feedback.html', {'feedback': feedback})




# Update Member
def updateMember(request, member_id):
    member = get_object_or_404(Members, id=member_id)

    if request.method == 'POST':
        form = MemberDetail(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, "Member updated successfully.")
            return redirect('member_list')  # adjust this to your actual member list view name
    else:
        form = MemberDetail(instance=member)

    return render(request, 'component/update_member.html', {'form': form})


# Delete Member
def deleteMember(request, member_id):
    member = get_object_or_404(Members, id=member_id)

    if request.method == 'POST':
        member.delete()
        messages.success(request, "Member deleted successfully.")
        return redirect('aboutUs')

    return render(request, 'component/confirm_delete_member.html', {'member': member})
