import time 
from veri import *

from tkinter.tix import Tree

def bekle(sn):
    time.sleep(sn)

def yukariKes(a, b):
    oncekiKisa=a[len(a)-3]
    kisa=a[len(a)-2]
    simdikiKisa=a[len(a)-1]

    oncekiUzun=b[len(b)-3]
    uzun=b[len(b)-2]
    simdikiUzun=b[len(b)-1]


    if oncekiKisa<oncekiUzun and kisa>uzun and simdikiKisa>simdikiUzun:
        return True

    else:
        return False    


def dipMi(a):
    ikiOnce=(a[len(a)-3])
    birOnce=(a[len(a)-2])
    once=(a[len(a)-1])
    if ikiOnce> birOnce and once> birOnce:
        return True
    else:
        return False

def tepeMi(a):
    ikiOnce= a[len(a)-3]
    birOnce= a[len(a)-2]
    once= a[len(a)-1]
    if ikiOnce< birOnce and once < birOnce:
        return True
    else:
        return False


def asagiKes(a, b):
    oncekiKisa=a[len(a)-3]
    kisa= a[len(a)-2]
    simdiKisa=a [len(a)-1]
    oncekiUzun=b [len(b)-3]
    uzun=b[len(b)-2]
    simdikiUzun=b [len(b)-1]
    if oncekiKisa > oncekiUzun and kisa < uzun and simdiKisa < simdikiUzun:
        return True
    else:
        return False     


def enYuksek(a, barSayisi):
    return max(a.tail(barSayisi))


def mesafe(l, el):
    for i in l.index:
        if l[i] == el:
            return len(l) - i - 1
    return None

def enDusuk(a, barSayisi):
    return min(a.tail(barSayisi))

