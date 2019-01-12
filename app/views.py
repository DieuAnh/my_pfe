from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.files import File
import matplotlib
matplotlib.use('Agg')
import os
import csv
import fileinput
from io import BytesIO
import base64
import sys
import numpy
from scipy import signal
from matplotlib import pyplot
import math
import cmath

sys.path.append("numpy_path")
from threading import Lock
lock = Lock()

from django.http import  HttpResponseRedirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from . import barreau
from . import plaque
from .forms import BarreauForm, PlateForm

# Create your views here.
def base(request):
    return render(request, 'app/base.html')

def draw_bode(a, b, l):
    nmin = 80e3;
    nmax = 150e3;
    nb_point = 800;

    pas = (nmax - nmin)/(nb_point - 1);
    f = numpy.arange(nmin, nmax, pas)

    eps33 = 867*8e-12;
    Beta33 = 1/eps33;
    k33 = 0.6269;
    rho = 7700;
    s33D = (103.6*10**9)**-1;
    vb = math.sqrt(1/(rho*s33D));

def bar(request):
    return render(request, 'app/bar.html')

def plate(request):
    return render(request, 'app/plate.html')

def disk(request):
    return render(request, 'app/disk.html')

def ring(request):
    return render(request, 'app/ring.html')


# I need to do a refactor later on this function
def display_form_bar(request):
    form = BarreauForm()
    return render(request, 'app/display_form_bar.html',{'form': form})
# Dimension du Barreau
# L = 16e-3;
# a = 2e-3;
# b = 2e-3;

def display_form_plate(request):
    form = PlateForm()
    return render(request, 'app/display_form_plate.html', {'form': form})

def handle_uploaded_file(f):
    with open('app/media/path_to_csv_file.csv', 'wb+') as destination:
        for line in f:
            destination.write(line)
    destination.close()
    # return 'path_to_csv_file.csv'

def compare_bode_bar(request):
    if request.method == 'POST':
        form = BarreauForm(request.POST, request.FILES)
        if form.is_valid():
            message = "form has been successfully submitted"
            # barreau = form.save(commit=False)
            L = float(request.POST.get('l'))
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            handle_uploaded_file(request.FILES['csvfile'])
            X = []
            Y = []
            with open('app/media/path_to_csv_file.csv') as file:
                csv_reader = csv.reader(file, delimiter=';')
                for i in range(0,17):
                    next(csv_reader)
                data = list(csv_reader)
                for i in data:
                    X.append(float(i[1])*10**-3)
                    Y.append(math.log10(float(i[2])))
            nmin = 80e3;
            nmax = 150e3;
            nb_point = 800;
            pas = (nmax - nmin)/(nb_point - 1);
            f = numpy.arange(nmin, nmax, pas)
            eps33 = 867*8e-12;
            Beta33 = 1/eps33;
            k33 = 0.6269;
            rho = 7700;
            s33D = (103.6*10**9)**-1;
            vb = math.sqrt(1/(rho*s33D));
            Z = []
            f_new = []
            for x in f:
                F1  = (2*math.pi*x*L)/(2*vb)
                # print(f"F1: {F1}, ")
                TF1 = math.tan(F1)/F1
                # print(f"TF1: {TF1}, ")
                C1  = (L*Beta33)/(a*b*2*math.pi*x*(1-k33**2))
                # print(f"C1: {C1}, ")
                res = C1*(1-(k33**2)*TF1)
                f_new.append(x*10**-3)
                Z.append(cmath.log10(res))
            X_f_new = zip(X,f_new)
            print(type(X_f_new))
            resultListX_f_new = list(X_f_new)
            print(resultListX_f_new)


            print('Size of X {}'.format(len(X)))
            print('Size of Y {}'.format(len(Y)))
            print('Size of f_new {}'.format(len(f_new)))
            print('Size of Z {}'.format(len(Z)))
            dif = []
            for i in range(0, len(Z)-1):
            	dif_elmt = abs((Z[i]-Y[i])/Z[i])*100
            	if dif_elmt <= 100:
            		dif.append(dif_elmt)
            	else:
            		dif.append(100)
            X_dif = []
            for i in range(0, len(Z)-1):
            	X_dif.append(X[i])

            with lock:
                fig_compare_bode_barreau = pyplot.figure()
                pyplot.subplot(2,1,1)
                pyplot.plot(X,Y,'r')

                pyplot.plot(f_new,Z,'b')
                pyplot.title("Evolution, in logarithmic scale, of the bar impedance module")
                pyplot.xlabel("Frequence (kHz)")
                pyplot.ylabel("Impedance")
                pyplot.subplot(2,1,2)
                pyplot.plot(X_dif,dif)
                fig_compare_bode_barreau.savefig('app/static/figures/compare_bode_bar.png')
            form.save()
            return render(request, 'app/compare_bode_bar.html')
            # return render(request, 'app/barreau.html')
    else:
        form = BarreauForm()
    return render(request, 'app/display_form_bar.html',{'form': form})


def compare_bode_plate(request):
    if request.method == 'POST':
        form = PlateForm(request.POST, request.FILES)
        if form.is_valid():
            message = "form has been successfully submitted"
            # barreau = form.save(commit=False)
            L = float(request.POST.get('l'))
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            handle_uploaded_file(request.FILES['csvfile'])
            X = []
            Y = []
            with open('app/media/path_to_csv_file.csv') as file:
                csv_reader = csv.reader(file, delimiter=';')
                for i in range(0,17):
                    next(csv_reader)
                data = list(csv_reader)
                for i in data:
                    X.append(float(i[1])*10**-3)
                    Y.append(math.log10(float(i[2])))
            nmin     = 80e3;
            nmax     = 150e3;
            nb_point = 10000;

            pas = (nmax-nmin)/(nb_point-1);
            f = numpy.arange(nmin, nmax, pas)
            rho=7700;
            eps33 = -3.271967632835997e-08;
            k31=0.327;
            s11 = 1.7e-11;
            # L =   75e-3;
            # a = 1.98e-3;
            # b =   20e-3;
            Vd  = math.sqrt(1/(rho*s11));
            eps = 9.14e3;
            C0  = eps*(L*b)/a;
            kt  = 0.469;
            Y1 = []
            Z = []
            f_new = []
            for x in f:
                F1  = ((2*math.pi*x)/(2*Vd))
                TF1 = math.tan(F1)/F1
                Y1_elmt = C0*(1-kt**2*TF1)
                f_new.append(x*10**-3)
                Y1.append(Y1_elmt)
                Z.append(cmath.log10(1/Y1_elmt))
            with lock:
                fig_compare_bode_plate = pyplot.figure()
                pyplot.plot(X,Y,'r')
                pyplot.plot(f_new,Z,'b')
                pyplot.xlabel('Frequence (kHz)')
                pyplot.ylabel('Impédance')
                pyplot.title('Evolution, en echelle logarithmique, du module de l''impédence d''une plaque')
                fig_compare_bode_plate.savefig('app/static/figures/compare_bode_plate.png')
            form.save()
            return render(request, 'app/compare_bode_plate.html')
            # return render(request, 'app/barreau.html')
    else:
        form = PlateForm()
    print("here i am")
    return render(request, 'app/display_form_plate.html',{'form': form})
