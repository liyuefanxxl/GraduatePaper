# coding: utf-8
from WindPy import *
from datetime import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

w.start()



#
def get_sector_list(sectorID, date):
    sector_list=w.wset("SectorConstituent", "date= %s; setorId=%s; field=wind_code"%(date,sectorID))
    return sector_list.Data[0]

Industry_list=['6210000000000000','6215000000000000','6220000000000000','6225000000000000','6230000000000000','6235000000000000','6240000000000000','6245000000000000','6250000000000000','6255000000000000']

for item in Industry_list:
    item_count=1
    print 'The number of industry:', item_count, '\r',
    stock_count=0
    data_frame=pd.DataFrame()
    each_list=get_sector_list(item,'20160305')
    for stock in each_list:

        print 'stock',np.float(100*stock_count/len(each_list)),'\r',
        data=w.wsd(stock, "industry_gicscode,pct_chg,ev,val_pe_deducted_ttm,pb_lf,ps_ttm,pcf_ocf_ttm,dividendyield", "2008-01-01", "2016-03-05", "industryType=1;rptYear=2014;Fill=Previous")
        data_frame=data_frame.append(pd.DataFrame(data.Data).T)
        stock_count+=1
    data_frame.to_csv('%s.csv'%item,header=True)
    item_count+=1