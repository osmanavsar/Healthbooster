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
    fig = px.bar(df, x="reg", y="mr", title="Regional MR device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_ul(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="reg", y="ul", title="Regional ultrasound device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_mam(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="reg", y="mam", title="Regional mammography device distribution in Turkey")
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})

def plot_her(request):
    df = pd.read_csv("static/regionaldata.csv", header = 0)
    df.info(verbose=True)
    fig = px.bar(df, x="reg", y="her", title="Regional hemodialysis device distribution in Turkey")
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
    df = pd.read_csv("static/citydata.csv", header = 0)

    print(df)


    books_list = [
        {"title": "Tesla Inventor of the Modern", "publisher": "Norton", "year": "2018"},
        {"title": "Kubeflow for Machine Learning", "publisher": "OReilly", "year": "2020"},
        {"title": "Africa Diaries", "publisher": "Adventure Press", "year": "2006"},
        {"title": "How to Be Rich", "publisher": "Penguin Books", "year": "2011"}
    ]

    flag = True
    return render(request, "display.html", {"books_list": books_list,
                                            "flag": flag
                                            })
