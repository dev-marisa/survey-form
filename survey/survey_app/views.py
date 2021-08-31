from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    elif request.method == 'POST':
        print(request.POST)
        context = {
            "form_data": request.POST
        }
        return render(request, "results.html", context)
