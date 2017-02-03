import numpy as np
import pandas as pd

def getData(ticker="XAUUSD", period="", isMac=False):
    if (isMac):
        foldername = '/Users/hnickau/HistoricData/'
    else:
        foldername = '/users/nickau/HistoricData/'
            
            
    fname = foldername + ticker + \
            '/DAT_ASCII_'+ticker+'_M1_'+period+'.csv'
    #names = ["Date","Time","Open","High","Low","Close","Volume"]
    #data = pd.read_csv(fname,sep=';', header=None, names = names)
    data = np.array(pd.read_csv(fname,sep=';', header=None))
    N = data.shape[0]
    date = data[:,0].reshape((N,1))
    year = np.trunc(date/10000)
    month = np.trunc((date-10000*year)/100)
    day = date -10000*year-100*month
    time = data[:,1].reshape((N,1))
    hour = np.trunc(time/10000)
    minute = np.trunc((time-10000*hour)/100)
    return np.concatenate((year,month,day,hour,minute,\
                        data[:,2:-1]*100),axis=1).astype(np.int32)
    
def makeTarget(data, reward=100, risk=50, horizon=10000, isBuy=True):
    N = data.shape[0]-horizon
    price = data[:-horizon,-1].reshape((N,1))
    result = np.zeros((N,1))
    for i in range(horizon):
        pass
    return result
    
def main():
    data = getData(period="201601",isMac=True)
    print data[:5]
    print data.shape

if __name__ == '__main__':
    main()
    