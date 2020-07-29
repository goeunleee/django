from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def main (request):
    blog=Blog.objects.all().order_by('-id')
    return render(request,'main.html', {'blog':blog}  )

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    bIndex = Blog.objects.all().order_by('-id')
    p= Paginator(bIndex,1)
    page= p.page(blog_id)
    
    return render(request,'detail.html',{'blog_detail':blog,'p':p,'id':blog_id,'page':page,'nkey':blog.pk+1,'pkey':blog.pk-1})       


def google_move(request):
    return redirect('https://www.naver.com/')


def new(request):
    if request.method == 'POST' :
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pk = len(Blog.objects.all())+1
        #blog.index = len(Blog.objects.all)+1
        blog.pub_date = timezone.datetime.now()
        blog.save()

        #return redirect('/myapp/detail/'+str(blog.id))
        return redirect('/myapp')
    else :    
        return render(request,'new.html')

def renew(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog,pk = blog_id)
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect("/myapp/detail/"+str(blog_id))
    else :    
        blog = get_object_or_404(Blog,pk = blog_id)
        return render(request,'renew.html',{'renew_blog':blog})        

def remove(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    

    return redirect('/myapp/')


def return_main(request):
   
    blog = Blog.objects.all().order_by('-id')
    return render(request, 'main.html', {'blog': blog})

    
