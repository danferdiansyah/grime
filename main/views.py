from django.shortcuts import render

def show_main(request):
    context = {
        'tagline': 'Anytime, anywhere.'
    }

    return render(request, "main.html", context)