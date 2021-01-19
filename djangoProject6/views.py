from django.http import HttpResponse
from django.shortcuts import render
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.datasets import make_classification


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
    fig = px.line(df, x="reg", y="dis1", title="Regional dental clinic distribution in Turkey")
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

    city_list = [
        {"name": "Adana", "region": "Mediterranean", "population": "2,237,940", "Hospital": "74598", "Bed": "31.4", "Exclusive Bed per Person": "18.4",
         "Ambulance": "38"},
        {"name": "Adıyaman", "region": "Southeast Anatolia", "population": "626,465", "Hospital": "52205", "Bed": "20.8", "Exclusive Bed per Person": "14.5",
         "Ambulance": "70.2"},
        {"name": "Afyonkarahisar", "region": "Aegean", "population": "729,483", "Hospital": "34737", "Bed": "30", "Exclusive Bed per Person": "22",
         "Ambulance": "82.3"},
        {"name": "Ağrı", "region": "East Anatolia", "population": "536,199", "Hospital": "53620", "Bed": "16.4", "Exclusive Bed per Person": "13.3",
         "Ambulance": "83.9"},
        {"name": "Aksaray", "region": "Central Anatolia", "population": "416,367", "Hospital": "41637", "Bed": "19.1", "Exclusive Bed per Person": "12.8",
         "Ambulance": "91.3"},
        {"name": "Amasya", "region": "Black Sea", "population": "337,800", "Hospital": "42225", "Bed": "24.7", "Exclusive Bed per Person": "16.4",
         "Ambulance": "94.7"},
        {"name": "Ankara", "region": "Central Anatolia", "population": "5,639,076", "Hospital": "72296", "Bed": "32.4", "Exclusive Bed per Person": "15.7",
         "Ambulance": "40.1"},
        {"name": "Antalya", "region": "Mediterranean", "population": "2,511,700", "Hospital": "55816", "Bed": "28.6", "Exclusive Bed per Person": "19.7",
         "Ambulance": "34.2"},
        {"name": "Ardahan", "region": "East Anatolia", "population": "97,319", "Hospital": "32440", "Bed": "20.6", "Exclusive Bed per Person": "18.6",
         "Ambulance": "359.6"},
        {"name": "Artvin", "region": "Black Sea", "population": "170,875", "Hospital": "21359", "Bed": "20.2", "Exclusive Bed per Person": "15.9",
         "Ambulance": "251.6"},
        {"name": "Aydın", "region": "Aegean", "population": "1,110,972", "Hospital": "50499", "Bed": "28.3", "Exclusive Bed per Person": "16.4",
         "Ambulance": "57.6"},
        {"name": "Balıkesir", "region": " Marmara", "population": "1,228,620", "Hospital": "51193", "Bed": "27.1", "Exclusive Bed per Person": "19.1",
         "Ambulance": "57.8"},
        {"name": "Bartın", "region": "Black Sea", "population": "198,249", "Hospital": "66083", "Bed": "21.8", "Exclusive Bed per Person": "7.5",
         "Ambulance": "136.2"},
        {"name": "Batman", "region": "Southeastern Anatolia", "population": "608,659", "Hospital": "55333", "Bed": "21.4", "Exclusive Bed per Person": "12",
         "Ambulance": "60.8"},
        {"name": "Bayburt", "region": "Black Sea", "population": "84,843", "Hospital": "84843", "Bed": "23.6", "Exclusive Bed per Person": "15.8",
         "Ambulance": "294.7"},
        {"name": "Bilecik", "region": "Marmara", "population": "219,427", "Hospital": "27428", "Bed": "15.3", "Exclusive Bed per Person": "4.9",
         "Ambulance": "150.4"},
        {"name": "Bingöl", "region": "East Anatolia", "population": "279,812", "Hospital": "34977", "Bed": "24.7", "Exclusive Bed per Person": "16.8",
         "Ambulance": "128.7"},
        {"name": "Bitlis", "region": "Southeastern Anatolia", "population": "348,115", "Hospital": "43514", "Bed": "27.5", "Exclusive Bed per Person": "16.5",
         "Ambulance": "103.4"},
        {"name": "Bolu", "region": "Black Sea", "population": "316,126", "Hospital": "28739", "Bed": "45.8", "Exclusive Bed per Person": "31.6",
         "Ambulance": "136"},
        {"name": "Burdur", "region": "Mediterranean", "population": "270,796", "Hospital": "33850", "Bed": "28", "Exclusive Bed per Person": "19.8",
         "Ambulance": "125.6"},
        {"name": "Bursa", "region": "Marmara", "population": "3,056,120", "Hospital": "76403", "Bed": "24.1", "Exclusive Bed per Person": "14.8",
         "Ambulance": "34"},
        {"name": "Çanakkale", "region": "Marmara", "population": "542,157", "Hospital": "41704", "Bed": "30.6", "Exclusive Bed per Person": "23.6",
         "Ambulance": "84.8"},
        {"name": "Çankırı", "region": "Central Anatolia", "population": "195,789", "Hospital": "21754", "Bed": "23.8", "Exclusive Bed per Person": "18.3",
         "Ambulance": "204.3"},
        {"name": "Çorum", "region": "Black Sea", "population": "530,864", "Hospital": "33179", "Bed": "31.3", "Exclusive Bed per Person": "23.2",
         "Ambulance": "105.5"},
        {"name": "Denizli", "region": "Aegean", "population": "1,037,208", "Hospital": "45096", "Bed": "31.1", "Exclusive Bed per Person": "17.5",
         "Ambulance": "59.8"},
        {"name": "Diyarbakır", "region": "Southeastern Anatolia", "population": "1,756,353", "Hospital": "67552", "Bed": "26.4", "Exclusive Bed per Person": "11.5",
         "Ambulance": "56.4"},
        {"name": "Düzce", "region": "Black Sea", "population": "392,166", "Hospital": "56024", "Bed": "20.2", "Exclusive Bed per Person": "13.8",
         "Ambulance": "79"},
        {"name": "Edirne", "region": "Marmara", "population": "413,903", "Hospital": "41390", "Bed": "46.8", "Exclusive Bed per Person": "25.1",
         "Ambulance": "116"},
        {"name": "Elâzığ", "region": "East Anatolia", "population": "591,098", "Hospital": "59110", "Bed": "50.6", "Exclusive Bed per Person": "30.4",
         "Ambulance": "89.7"},
        {"name": "Erzincan", "region": "East Anatolia", "population": "234,747", "Hospital": "23475", "Bed": "23", "Exclusive Bed per Person": "13.5",
         "Ambulance": "230"},
        {"name": "Erzurum", "region": "East Anatolia", "population": "762,062", "Hospital": "34639", "Bed": "47.5", "Exclusive Bed per Person": "30.1",
         "Ambulance": "101"},
        {"name": "Eskişehir", "region": "Central Anatolia", "population": "887,475", "Hospital": "63391", "Bed": "40", "Exclusive Bed per Person": "29.9",
         "Ambulance": "55.2"},
        {"name": "Gaziantep", "region": "Southeastern Anatolia", "population": "2,069,364", "Hospital": "73906", "Bed": "29.1", "Exclusive Bed per Person": "13.7",
         "Ambulance": "36.2"},
        {"name": "Giresun", "region": "Black Sea", "population": "448,400", "Hospital": "26376", "Bed": "35.1", "Exclusive Bed per Person": "23.4",
         "Ambulance": "116"},
        {"name": "Gümüşhane", "region": "Black Sea", "population": "164,521", "Hospital": "27420", "Bed": "19.9", "Exclusive Bed per Person": "10.6",
         "Ambulance": "218.8"},
        {"name": "Hakkâri", "region": "East Anatolia", "population": "280,991", "Hospital": "70248", "Bed": "14", "Exclusive Bed per Person": "11.9",
         "Ambulance": "142.4"},
        {"name": "Hatay", "region": "Mediterranean", "population": "1,628,894", "Hospital": "67871", "Bed": "25.7", "Exclusive Bed per Person": "16.1",
         "Ambulance": "54.6"},
        {"name": "Iğdır", "region": "East Anatolia", "population": "199,442", "Hospital": "66481", "Bed": "15.7", "Exclusive Bed per Person": "12.5",
         "Ambulance": "155.4"},
        {"name": "Isparta", "region": "Mediterranean", "population": "444,914", "Hospital": "31780", "Bed": "45.4", "Exclusive Bed per Person": "30.1",
         "Ambulance": "105.6"},
        {"name": "İstanbul", "region": "Marmara", "population": "15,519,267", "Hospital": "70542", "Bed": "25.3", "Exclusive Bed per Person": "14.4",
         "Ambulance": "30"},
        {"name": "İzmir", "region": "Aegean", "population": "4,367,251", "Hospital": "80875", "Bed": "27.4", "Exclusive Bed per Person": "13.9",
         "Ambulance": "33.2"},
        {"name": "Kahramanmaraş", "region": "Mediterranean", "population": "1,154,102", "Hospital": "64117", "Bed": "25.5", "Exclusive Bed per Person": "15.3",
         "Ambulance": "63.3"},
        {"name": "Karabük", "region": "Black Sea", "population": "248,458", "Hospital": "49692", "Bed": "28.8", "Exclusive Bed per Person": "22.5",
         "Ambulance": "132.8"},
        {"name": "Karaman", "region": "Central Anatolia", "population": "253,279", "Hospital": "42213", "Bed": "23.6", "Exclusive Bed per Person": "20.2",
         "Ambulance": "134.2"},
        {"name": "Kars", "region": "East Anatolia", "population": "285,410", "Hospital": "40773", "Bed": "25.9", "Exclusive Bed per Person": "18.7",
         "Ambulance": "129.6"},
        {"name": "Kastamonu", "region": "Black Sea", "population": "379,405", "Hospital": "21078", "Bed": "29", "Exclusive Bed per Person": "17.3",
         "Ambulance": "139.7"},
        {"name": "Kayseri", "region": "Central Anatolia", "population": "1,407,409", "Hospital": "54131", "Bed": "32.5", "Exclusive Bed per Person": "20.2",
         "Ambulance": "52.6"},
        {"name": "Kilis", "region": "Southeastern Anatolia", "population": "142,490", "Hospital": "47497", "Bed": "22.5", "Exclusive Bed per Person": "18.2",
         "Ambulance": "379"},
        {"name": "Kırıkkale", "region": "Central Anatolia", "population": "283,017", "Hospital": "47170", "Bed": "44.3", "Exclusive Bed per Person": "24.1",
         "Ambulance": "137.8"},
        {"name": "Kırklareli", "region": "Marmara", "population": "361,836", "Hospital": "40204", "Bed": "25.1", "Exclusive Bed per Person": "16.1",
         "Ambulance": "110.5"},
        {"name": "Kırşehir", "region": "Central Anatolia", "population": "242,938", "Hospital": "48588", "Bed": "19.4", "Exclusive Bed per Person": "16.7",
         "Ambulance": "127.6"},
        {"name": "Kocaeli", "region": "Marmara", "population": "1,953,035", "Hospital": "72335", "Bed": "22.2", "Exclusive Bed per Person": "14.2",
         "Ambulance": "35.3"},
        {"name": "Konya", "region": "Central Anatolia", "population": "2,232,374", "Hospital": "53152", "Bed": "33.7", "Exclusive Bed per Person": "20",
         "Ambulance": "43.9"},
        {"name": "Kütahya", "region": "Aegean", "population": "579,257", "Hospital": "48271", "Bed": "32.6", "Exclusive Bed per Person": "20.8",
         "Ambulance": "74.2"},
        {"name": "Malatya", "region": "East Anatolia", "population": "800,165", "Hospital": "50010", "Bed": "37", "Exclusive Bed per Person": "21.8",
         "Ambulance": "90"},
        {"name": "Manisa", "region": "Aegean", "population": "1,440,611", "Hospital": "53356", "Bed": "31.8", "Exclusive Bed per Person": "21.4",
         "Ambulance": "49.3"},
        {"name": "Mardin", "region": "Southeastern Anatolia", "population": "838,778", "Hospital": "69898", "Bed": "17.2", "Exclusive Bed per Person": "11.3",
         "Ambulance": "48.9"},
        {"name": "Mersin", "region": "Mediterranean", "population": "1,840,425", "Hospital": "70786", "Bed": "25.9", "Exclusive Bed per Person": "18",
         "Ambulance": "46.7"},
        {"name": "Muğla", "region": "Aegean", "population": "983,142", "Hospital": "44688", "Bed": "20.7", "Exclusive Bed per Person": "14.1",
         "Ambulance": "77.3"},
        {"name": "Muş", "region": "East Anatolia", "population": "408,809", "Hospital": "58401", "Bed": "18", "Exclusive Bed per Person": "14.2",
         "Ambulance": "93"},
        {"name": "Nevşehir", "region": "Central Anatolia", "population": "303,010", "Hospital": "30301", "Bed": "23", "Exclusive Bed per Person": "19.7",
         "Ambulance": "105.6"},
        {"name": "Niğde", "region": "Central Anatolia", "population": "362,861", "Hospital": "45358", "Bed": "24.5", "Exclusive Bed per Person": "16.4",
         "Ambulance": "113"},
        {"name": "Ordu", "region": "Black Sea", "population": "754,198", "Hospital": "44365", "Bed": "28.4", "Exclusive Bed per Person": "16.5",
         "Ambulance": "76.9"},
        {"name": "Osmaniye", "region": "Southeastern Anatolia", "population": "538,759", "Hospital": "53876", "Bed": "24", "Exclusive Bed per Person": "12.9",
         "Ambulance": "79.8"},
        {"name": "Rize", "region": "Black Sea", "population": "343,212", "Hospital": "31201", "Bed": "32.3", "Exclusive Bed per Person": "25.1",
         "Ambulance": "128.2"},
        {"name": "Sakarya", "region": "Marmara", "population": "1,028,500", "Hospital": "54132", "Bed": "18.8", "Exclusive Bed per Person": "14.4",
         "Ambulance": "48.6"},
        {"name": "Samsun", "region": "Black Sea", "population": "1,348,542", "Hospital": "53942", "Bed": "34.3", "Exclusive Bed per Person": "20.8",
         "Ambulance": "47.5"},
        {"name": "Şanlıurfa", "region": "Southeastern Anatolia", "population": "2,073,614", "Hospital": "109138", "Bed": "19.5", "Exclusive Bed per Person": "10.1",
         "Ambulance": "43.4"},
        {"name": "Siirt", "region": "Southeastern Anatolia", "population": "330,280", "Hospital": "36698", "Bed": "26", "Exclusive Bed per Person": "20.4",
         "Ambulance": "121.1"},
        {"name": "Sinop", "region": "Black Sea", "population": "218,243", "Hospital": "31178", "Bed": "24.5", "Exclusive Bed per Person": "15.4",
         "Ambulance": "160.4"},
        {"name": "Şırnak", "region": "Southeastern Anatolia", "population": "529,615", "Hospital": "75659", "Bed": "11.9", "Exclusive Bed per Person": "8.6",
         "Ambulance": "94.4"},
        {"name": "Sivas", "region": "Central Anatolia", "population": "638,956", "Hospital": "33629", "Bed": "40.9", "Exclusive Bed per Person": "19.3",
         "Ambulance": "112.7"},
        {"name": "Tekirdağ", "region": "Marmara", "population": "1,055,412", "Hospital": "62083", "Bed": "25.3", "Exclusive Bed per Person": "15.9",
         "Ambulance": "50.2"},
        {"name": "Tokat", "region": "Black Sea", "population": "612,747", "Hospital": "43768", "Bed": "35.9", "Exclusive Bed per Person": "27.1",
         "Ambulance": "94.7"},
        {"name": "Trabzon", "region": "Black Sea", "population": "808,974", "Hospital": "40449", "Bed": "40.1", "Exclusive Bed per Person": "23.6",
         "Ambulance": "69.2"},
        {"name": "Tunceli", "region": "East Anatolia", "population": "84,660", "Hospital": "14110", "Bed": "17.7", "Exclusive Bed per Person": "15.6",
         "Ambulance": "366.2"},
        {"name": "Uşak", "region": "Aegean ", "population": "370,509", "Hospital": "46314", "Bed": "33.3", "Exclusive Bed per Person": "22.1",
         "Ambulance": "113.4"},
        {"name": "Van", "region": "East Anatolia", "population": "1,136,757", "Hospital": "94730", "Bed": "25.4", "Exclusive Bed per Person": "18.3",
         "Ambulance": "64.2"},
        {"name": "Yalova", "region": "Marmara", "population": "270,976", "Hospital": "30108", "Bed": "21", "Exclusive Bed per Person": "12.1",
         "Ambulance": "81.2"},
        {"name": "Yozgat", "region": "Central Anatolia", "population": "421,200", "Hospital": "28080", "Bed": "30.5", "Exclusive Bed per Person": "25.4",
         "Ambulance": "133"},
        {"name": "Zonguldak", "region": "Black Sea", "population": "596,053", "Hospital": "54187", "Bed": "36.8", "Exclusive Bed per Person": "16.5",
         "Ambulance": "65.4"}
    ]

    flag = True
    return render(request, "display.html", {"city_list": city_list,
                                            "flag": flag
                                            })
