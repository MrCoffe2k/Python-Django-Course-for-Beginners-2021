from django.shortcuts import render

# Create your views here.


def index(request):
    app = [
        {
            'title': 'Ejemplo app',
            'location': 'Saltillo',
            'slug': 'Primer-ejemplo'
        },
        {
            'title': 'Ejemplo app2',
            'location': 'Monterrey',
            'slug': 'Segundo-ejemplo'
        }
    ]
    return render(request, 'app/index.html', {
        'show_app': True,
        'app': app
    })
