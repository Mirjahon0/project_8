from django.shortcuts import render, redirect
from django.views import View
from .models import Chairs,Team
from django.contrib.auth.forms import UserCreationForm

class ShopListView(View):
    def get(self,request):
        search = request.GET.get("search")
        if not search:
            chairs = Chairs.objects.all()
            context = {
                'chairs':chairs,
                'result':search
            }
            return render(request, "main/shop.html", context)
        else:
            chairs = Chairs.objects.filter(name__icontains= search)
            if chairs:
                context = {
                    'chairs':chairs,
                    'result':search
            }
                return render(request, "main/shop.html", context)
            else: 
                context = {
                    'chairs':chairs,
                    'result':search
            }
            return render(request, "main/shop.html", context)   
            
         
            
            
class AboutListView(View):
    def get(self,request):
        teams = Team.objects.all()
        context = {
            'teams':teams
        }
        return render(request, "main/about.html", context)

class ServicesListView(View):
    def get(self,request):
        chairs = Chairs.objects.all()
        context = {
            'chairs':chairs
        }
        return render(request, "main/services.html", context)

class ChairdetailView(View):
    def get (self, request, id):
        chairs = Chairs.objects.get(id = id)
        return render(request, template_name="main/chairdetail.html",context={'chairs':chairs})

class ChairUpdateView(View):
    def get (self, request,id):
        chairs = Chairs.objects.get(id = id)
        return render(request,template_name="main/chair_update_view.html",context={'chairs':chairs} ) 
    
    def post(self, request, id):
        new_name = request.POST.get('name')
        new_price = request.POST.get('price')
        new_prices = request.POST.get('prices')
        
        chairs = Chairs.objects.get(id=id)
        chairs.name = new_name
        chairs.price = new_price
        chairs.prices = new_prices
        chairs.save()
        
        return redirect('shops')
    
    
class ChairDeleteView(View):
    def get(self, request, id):
        chairs = Chairs.objects.get(id = id)
        chairs.delete()
        return redirect('shops')
    
    
    