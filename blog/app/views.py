from django.shortcuts import render,redirect
from app.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def create(request):
    if request.method == "POST":
        title1=request.POST['title']

        body_user=request.POST['message']

        try:    
            if  title1:
                 new=Post( tittile=title1,body=body_user)
                 new.save()
                 return redirect('/') 
            else:
                return render(request,'create.html')
        except:
            return render(request,'create.html')
    else:          
      return render(request,'create.html')
def update(request):
    try:
      if request.method == "POST":
        title1=request.POST['title']
        body_user=request.POST['message']
        a=Post.objects.get(tittile=title1)
        a.tittile=title1
        a.body=body_user
        a.save()
        return redirect('index')        
      return render(request,'update.html')
    except:
      return render(request,'update.html')

def delete(request):
    try:
      if request.method == "POST":
        title1=request.POST['title']
        a=Post.objects.get(tittile=title1)
        a.delete()
        return redirect('index')        
      return render(request,'delete.html')
    except:
        return render(request,'delete.html')
        

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})