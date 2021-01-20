"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoProject6.views import display, home, plot_dis, plot_amb, plot_mr, plot_her, plot_mam, plot_ul, plot_poph
from djangoProject6.views import plot_bed, plot_int, plot_spe, plot_eko ,plot_expu , plot_pub
from healthbooster.views import add_person, all_people, people_search, add_city, all_cities
from healthbooster.views import search_form, search
from django.conf import settings
from django.conf.urls.static import static
from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', home),
    path('plot_dis/', plot_dis),
    path('plot_poph/', plot_poph),
    path('plot_pub/', plot_pub),
    path('plot_expu/', plot_expu),
    path('plot_amb/', plot_amb),
    path('plot_mr/',plot_mr),
    path('plot_her/',plot_her),
    path('plot_eko/',plot_eko),
    path('plot_mam/',plot_mam),
    path('plot_ul/',plot_ul),
    path('plot_bed/',plot_bed),
    path('plot_spe/',plot_spe),
    path('plot_int/',plot_int),
    path('admin/', admin.site.urls),
    path('display/', display),
    path('add_person/', add_person),
    path('add_city/', add_city),
    path('cities/', all_cities),
    path('people/', all_people),
    path('people_search/', people_search),
    path('search_form/', search_form),
    path('search/', search)
]
