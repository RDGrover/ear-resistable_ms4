from django.shortcuts import render

# Create your views here.


def view_bag(request):
# A view to render bag's contents
    return render(request, 'bag/bag.html')
