# -*- coding:utf-8 -*-

from WindPy import *
from datetime import *
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

w.start()

All_stock=w.wset("SectorConstituent","date=20150305;sectorId=a001010200000000;field=wind_code")

def get_ipo_date(ticker):
    ipo_date=w.wss(str(ticker),"ipo_date")
    return str(ipo_date.Data[0])

def data_on_ipo_date(ticker):
    da_ipo_date=w.wsd(str(ticker),"industry_gicscode,pct_chg,ev,val_pe_deducted_ttm,pb_lf,ps_ttm,pcf_ocf_ttm,dividendyield", get_ipo_date(ticker),get_ipo_date(ticker),"Fill=Previous")
    return da_ipo_date.Data[0]

for i in range(len(All_stock.Data[0])):
    ipo_data=pd.DataFrame()
    print i*100./len(All_stock.Data[0]),'\r',
    print get_ipo_date('000001.sz')
    ipo_data=ipo_data.append(pd.DataFrame(data_on_ipo_date(All_stock.Data[0][i])).T)

ipo_data.to_csv('trial.csv',header=True)
w.stop()