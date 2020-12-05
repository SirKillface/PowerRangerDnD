from django.shortcuts import render

# Create your views here.
def dashboard(request):
    """dashboard renders a view for the homepage.

    Args:
        request (HttpRequest): web request

    Returns:
        HttpResponse: text/html response
    """


    return render(request, 'dashboard/index.html', context={

    })
