from django.shortcuts import render
from django.views import View
from product.models import Chairs, Speciality,Testominal,Links,Team
from blog.models import RcentBlog


class BasicViewPage(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        chairs = Chairs.objects.all()
        recent_blog = RcentBlog.objects.all()
        testominal = Testominal.objects.all()
        teams = Team.objects.all()
        link = Links.objects.all()
        context = {
            "specialities":specialities,
            "chairs":chairs,
            "recent_blog":recent_blog,
            "testominal":testominal,
            "link":link,
            'teams':teams
        }
        return render(request, "main/index.html", context)

