from django.shortcuts import render, redirect
from .forms import ContactForm

# View for the homepage
def index(request):
    return render(request, 'main/index.html')

# View for the contact page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Temporary: show data in terminal (or handle/save/send)
            print(form.cleaned_data)
            return render(request, 'main/contact.html', {
                'form': ContactForm(),  # reset form
                'success': True
            })
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})
