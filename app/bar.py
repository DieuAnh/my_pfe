import sys
import numpy
from scipy import signal
from matplotlib import pyplot
import math
import cmath

sys.path.append("numpy_path")
from threading import Lock
lock = Lock()

# matplotlib.use('Agg')

def callback():
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

    # Dimenssion du Barreau
    L = 16e-3;
    a = 2e-3;
    b = 2e-3;

    vb = math.sqrt(1/(rho*s33D));
    print(vb)

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
        # else:
        #   Z.append(math.log10(-res))
    # print(Z)
    with lock:
        fig_barreau = pyplot.figure()
        pyplot.plot(f_new,Z)
        pyplot.title("Evolution, en echelle logarithmique, du module de l''impedence du barreau")
        pyplot.xlabel("Frequence (kHz)")
        pyplot.ylabel("Impedance")
        # pyplot.show()
        fig_barreau.savefig('./barreau_bode.png')

    return fig_barreau
