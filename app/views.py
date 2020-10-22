from django.shortcuts import redirect, render
from app.forms import TutoForm
from app.models import Tuto
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.





@login_required(login_url="/login/")
def listTutos(request):
    user = request.user
    tutos = Tuto.objects.filter(created_by=user)
    return render(request,"list.html",{"tutos":tutos})

@login_required(login_url="/login/")
def addTuto(request):
    form = TutoForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        cle_tuto = form.cleaned_data.get("cle_tuto")
        typeTuto = "Youtube"
        idTutoVideo = form.cleaned_data.get("idTutoVideo")
        if(idTutoVideo.find("https://www.youtube.com/watch?v=")==0):
            idTutoVideo = idTutoVideo.replace("https://www.youtube.com/watch?v=","",1)
        if(idTutoVideo.find("https://youtu.be/")==0):
            idTutoVideo = idTutoVideo.replace("https://youtu.be/","",1)
        if(idTutoVideo.find("https://www.youtube.com/embed/")==0):
            idTutoVideo = idTutoVideo.replace("https://www.youtube.com/embed/","",1)
        
        deb = idTutoVideo.find("/")
        if(deb>0):
            idTutoVideo = idTutoVideo[:deb]
            
        deb = idTutoVideo.find("&")
        if(deb>0):
            idTutoVideo = idTutoVideo[:deb]

        deb = idTutoVideo.find("?")
        if(deb>0):
            idTutoVideo = idTutoVideo[:deb]
        
        client_url = form.cleaned_data.get("client_url")
        if(client_url.find("https://") == 0):
            client_url = client_url.replace("https://", "",1)
        elif (client_url.find("http://") == 0):
            client_url = client_url.replace("http://", "",1)
        clientName = form.cleaned_data.get("clientName")
        created_by = request.user
        
        tuto = Tuto.objects.create(
            cle_tuto = cle_tuto,
            typeTuto = typeTuto,
            idTutoVideo = idTutoVideo,
            client_url = client_url,
            clientName = clientName,
            created_by = created_by
        )
        tuto.save()
        return redirect("/list")
        
    return render(request,"add.html",{"form":form})

@login_required(login_url="/login/")
def updateTuto(request, idTuto):
    try:
        tuto = Tuto.objects.get(pk=idTuto)
    except:
        return redirect("/list")
    user = request.user
    tutos = Tuto.objects.filter(created_by=user)
    if(tuto not in tutos):
        return redirect("/list")
    dico = tuto.__dict__
    if request.method == "POST":
        cle_tuto = request.POST.get("cle_tuto")
        idTutoVideo = request.POST.get("idTutoVideo")
        if(idTutoVideo.find("https://www.youtube.com/watch?v=")==0):
            idTutoVideo = idTutoVideo.replace("https://www.youtube.com/watch?v=","")
        if(idTutoVideo.find("https://youtu.be/")==0):
            idTutoVideo = idTutoVideo.replace("https://youtu.be/","")
        if(idTutoVideo.find("https://www.youtube.com/embed/")==0):
            idTutoVideo = idTutoVideo.replace("https://www.youtube.com/embed/","")
        
        deb = idTutoVideo.find("/")
        if(deb>0):
            idTutoVideo = idTutoVideo[:deb]
            
        deb = idTutoVideo.find("&")
        if(deb>0):
            idTutoVideo = idTutoVideo[:deb]

        deb = idTutoVideo.find("?")
        if(deb>0):
            idTutoVideo = idTutoVideo[:deb]
        
        
        client_url = request.POST.get("client_url")
        if(client_url.find("https://") == 0):
            client_url = client_url.replace("https://", "",1)
        elif (client_url.find("http://") == 0):
            client_url = client_url.replace("http://", "",1)
        clientName = request.POST.get("clientName")
        Tuto.objects.filter(pk = idTuto).update(
            cle_tuto = cle_tuto,
            client_url = client_url,
            idTutoVideo = idTutoVideo,
            clientName = clientName,
        )
        return redirect("/list")
    return render(request, "update.html", {"dico":dico})

@login_required(login_url="/login/")
def upd_del_tuto(request, idTuto):
    try:
        tuto = Tuto.objects.get(pk=idTuto)
    except:
        return redirect("/list")
    user = request.user
    tutos = Tuto.objects.filter(created_by=user)
    if(tuto not in tutos):
        return redirect("/list")
    if request.method == "POST":
        tuto.delete()
        return redirect("/list")
    return render(request, "upd_del.html",{"tuto":tuto})


def connexion(request):
    if request.method == "POST":
        cle_tuto = request.POST.get("cle_tuto")
        try:
            tuto = Tuto.objects.get(pk=cle_tuto)
        except:
            return redirect("/")
        return redirect("/tuto/"+cle_tuto)
    return render(request, "connexion.html")

def tutoPage(request, idTuto):
    try:
        tuto = Tuto.objects.get(pk=idTuto)
    except:
        return redirect("/")
    return render(request,"tuto.html",{"tuto":tuto})

def pour1404(request, param1):
    return render(request, "pour404.html")

def pour2404(request, param1, param2):
    return render(request, "pour404.html")
