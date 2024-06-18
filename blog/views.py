from django.shortcuts import render,redirect
from django.views import View
from .models import RcentBlog
class BlogListView(View):
    def get(self,request):
        search = request.GET.get("search")
        if not search:
            recent_blog = RcentBlog.objects.all()
            context = {
                'recent_blog':recent_blog,
                'result':search
            }
            return render(request, "main/blog.html", context)
        else:
            recent_blog = RcentBlog.objects.filter(owner__icontains= search)
            if recent_blog:
                context = {
                    'recent_blog':recent_blog,
                    'result':search
            }
                return render(request, "main/blog.html", context)
            else: 
                context = {
                    'recent_blog':recent_blog,
                    'result':search
            }
            return render(request, "main/blog.html", context)   

class BlogDetailView(View):
    def get (self, request, id):
        recent_blog = RcentBlog.objects.get(id = id)
        return render(request, template_name="main/blogdetail.html",context={'recent_blog':recent_blog})
    
    
    
    
class BlogUpdateView(View):
    def get (self, request,id):
        recent_blog = RcentBlog.objects.get(id = id)
        return render(request,template_name="main/blog_update_view.html",context={'recent_blog':recent_blog}) 
    
    def post(self, request, id):
        new_title = request.POST.get('title')
        new_owner = request.POST.get('owner')
        
        
        recent_blog = RcentBlog.objects.get(id=id)
        recent_blog.title = new_title
        recent_blog.owner = new_owner
        recent_blog.save()
        
        return redirect('blogs') 


class BlogDeleteView(View):
    def get(self, request, id):
        recent_blog = RcentBlog.objects.get(id = id)
        recent_blog.delete()
        return redirect('blogs   ')       