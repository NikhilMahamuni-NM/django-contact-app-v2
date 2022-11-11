from django.shortcuts import render, get_object_or_404, redirect
from django.forms import formset_factory, modelformset_factory

from .models import Contact, Card
from .forms import CardForm, ContactForm
# Create your views here.
def home(request):

    context = {

    }

    return render(request, 'cards/home.html', context)

def contactList(request):

    context = {
        'cards' : Card.objects.filter(user=request.user)
    }

    return render(request, 'cards/contactList.html', context)

def contactDetail(request, id):

    card = get_object_or_404(Card, id=id)
    context = {
        'card' : card,
        'contacts' : Contact.objects.filter(user=request.user, card=card),
        # 'workInfo' : get_object_or_404(additionalWorkInfo, user=request.user, card=card)
    }

    return render(request, 'cards/contactDetail.html', context)


def createCard(request):
    contactFormset = formset_factory(ContactForm, max_num=0)
    formset = contactFormset()
    form = CardForm()
    if request.method == "POST":
        print(request.POST)
        form = CardForm(request.POST,request.FILES)
        formset = contactFormset(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            
            for contactForm in formset:
                temp = contactForm.save(commit=False)
                temp.user = request.user
                temp.card = card
                temp.save()
            
            
            return redirect('cards:contactList')
        else:
            print("Form invalid", formset.errors)
    context = {
        'cardForm' : form,
        'formset' : formset
    }

    return render(request, 'cards/createCard.html', context)

def editCard(request, id):

    card = get_object_or_404(Card, id=id)
    form = CardForm(instance = card)
    q = Contact.objects.filter(user=request.user, card=card)
    contactFormset = modelformset_factory(Contact, form=ContactForm, extra=0, can_delete=True)
    formset = contactFormset(queryset=q)

    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance = card)
        formset = contactFormset(request.POST, queryset=q)

        if all([form.is_valid(), formset.is_valid()]):
            form = form.save(commit=False)
            form.save()
            for cForm in formset:
                print(cForm.cleaned_data)
                temp = cForm.save(commit=False)
                temp.user = request.user
                temp.card = card
                temp.save()
            for dform in formset.deleted_forms:
                id = dform.cleaned_data['id']
                contact = Contact.objects.get(id=id.id)
                contact.delete()
            return redirect('cards:contactDetail', card.id)

    context = {
        'card' : card,
        'form' : form,
        'formset' : formset
    }

    return render(request, 'cards/editCard.html', context)

def deleteCard(request, id):
    card = get_object_or_404(Card, id=id)
    card.delete()
    return redirect('cards:contactList')


    