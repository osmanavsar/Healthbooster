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
from djangoProject6.views import plot_bed, plot_int, plot_spe
from healthbooster.views import add_investor, all_authors, author_search
from healthbooster.views import search_form, search

urlpatterns = [
    path('', home),
    path('plot_dis/', plot_dis),
    path('plot_poph/', plot_poph),
    path('plot_amb/', plot_amb),
    path('plot_mr/',plot_mr),
    path('plot_her/',plot_her),
    path('plot_mam/',plot_mam),
    path('plot_ul/',plot_ul),
    path('plot_bed/',plot_bed),
    path('plot_spe/',plot_spe),
    path('plot_int/',plot_int),
    path('admin/', admin.site.urls),
    path('display/', display),
    path('add_investor/', add_investor),
    path('authors/', all_authors),
    path('author_search/', author_search),
    path('search_form/', search_form),
    path('search/', search)
]
