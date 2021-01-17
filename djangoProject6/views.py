from django.http import HttpResponse
from django.shortcuts import render
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np

def home(request):
    return render(request, "base.html")

def plot_mr(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.scatter(df, x="reg", y="mr", title="Regional MR device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_ul(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.scatter(df, x="reg", y="ul", title="Regional ultrasound device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_mam(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.scatter(df, x="reg", y="mam", title="Regional mammography device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_her(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.scatter(df, x="reg", y="her", title="Regional hemodialysis device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_eko(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.scatter(df, x="reg", y="eko", title="Regional ecocardiography device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_dis(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="reg", y="dis1", title="Regional dental clinic distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_poph(request):
    df = pd.read_csv("static/citydata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="City", y="PopH", title="Number of people per hospital")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_pub(request):
    df = pd.read_csv("static/citydata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="City", y="Pub", title="Number of public hospitals")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_expu(request):
    df = pd.read_csv("static/citydata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="City", y="ExPu", title="Number of total hospitals")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_bed(request):
    df = pd.read_csv("static/citydata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="City", y="BedP", title="Number of bed per 10.000 people")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_spe(request):
    df = pd.read_csv("static/citydata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="City", y="SpeP", title="Number of high quality bed per 10.000 people")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_int(request):
    df = pd.read_csv("static/citydata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="City", y="IntP", title="Number of intensive care bed per 10.000 people")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_amb(request):
    df = pd.read_csv("static/citydata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="City", y="AmbP", title="Number of ambulance per 1.000.000 people")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

#the first parameter is request, i.e., HttpRequest
def display(request):
    df = pd.read_csv("static/citydata.csv", header=0)
    df.info(verbose=True)

    city_list = [
        {"name": "Adana", "region": "Akdeniz", "population": "2,237,940"},
        {"name": "Adıyaman", "region": "Güneydoğu", "population": "626,465"},
        {"name": "Afyonkarahisar", "region": "Ege", "population": "729,483"},
        {"name": "Ağrı", "region": "Doğu", "population": "536,199"}
    ]

    flag = True
    return render(request, "display.html", {"city_list": city_list,
                                            "flag": flag
                                            })
