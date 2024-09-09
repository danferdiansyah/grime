from django.shortcuts import render

def show_main(request):
    context = {
        'tagline': 'Anytime, anywhere.',
        'name' : 'Daniel Ferdiansyah',
        'class' : 'PBP F'
    }

    return render(request, "main.html", context)