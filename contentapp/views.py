from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    re = None
    if request.method == "POST":
        r = requests.post("https://api.deepai.org/api/text-generator", 
        data={'text': request.POST["newtext"],}, 
        headers={'api-key': 'XXX'})
        result = r.json()['output']
        re = result.replace("\n", " ")
       
    
  
    
    context = {"re": re}
    return render(request, "index.html", context)


def about(request):

    return render(request, "about.html")



def privacy(request):

    return render(request, "privacy.html")