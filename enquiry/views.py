from django.shortcuts import render, redirect
from enquiry.forms import EnquiryForm
from enquiry.models import Enquiry
# Create your views here.


def index(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EnquiryForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    enquiries = Enquiry.objects.all()
    return render(request, "show.html", {'enquiries': enquiries})


def edit(request, id):
    enquiry = Enquiry.objects.get(id=id)
    return render(request, 'edit.html', {'enquiry': enquiry})


def update(request, id):
    enquiry = Enquiry.objects.get(id=id)
    form = EnquiryForm(request.POST, instance=enquiry)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'enquiry': enquiry})


def destroy(request, id):
    enquiry = Enquiry.objects.get(id=id)
    enquiry.delete()
    return redirect("/show")
