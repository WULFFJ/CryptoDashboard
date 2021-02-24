#Simple Crypto API call to establish metrics for 100 coins
#Six specific coins have history for 30 days.  You can go up to 100 days.
#See cryptocompare.com for documentation on their API
#YOURAPIKEYHERE IS WHERE YOU PUT YOUR API

import requests
import pandas as pd
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:80% !important; }</style>"))
pd.set_option('display.max_colwidth',-1) ######Sets the Jupyter Notebook wider to see mor of what you are typing (script creation purpose)
pd.set_option('display.expand_frame_repr', False)

coins='BTC,BNB,ETH,ADA,XRP,DOT,LTC,BUSD,BCH,HT,EOS,LINK,TRX,DASH,DOGE,OKB,XLM,RVN,ETC,UNI,NEO,USDT,ZEC,BSV,REN,SXP,ATOM,BTT,SUSHI,CAKE,AAVE,XEM,MIOTA,IOST,XTZ,USDC,XMR,ONT,VET,FIL,MATIC,FTT,OMG,ICX,ALGO,XVS,YFI,QTUM,BAKE,CRV,SOL,AVAX,BNT,CRO,ZIL,GLM,KSM,LUNA,EGLD,SRM,SNX,THETA,JST,BAND,CHZ,TMTG,TFUEL,ZRX,CVC,WAVES,GRT,MANA,BAT,HBAR,FTM,GT,ELF,COMP,WBTC,CELO,NPXS,DGB,YFII,PAY,ALPHA,FRONT,DVP,RUNE,OXT,RSR,KNC,LSK,MX,NANO,REP,COTI,ENJ,LOOM,LRC,KAVA'

def GetCoinList(lst):
    global coins,CoinTable
    CoinTable={}
    multi='https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR'
    api='YOURAPIKEYHERE'
    extraParams='dogedash'
    params=(
        f'extraParams={extraParams}&'
        f'fsyms={coins}&'
        f'api_key={api}')
    url=multi+params
    r=requests.get(url).json()
    df=pd.DataFrame(r)
    c1=pd.json_normalize(df['DISPLAY'])
    c2=pd.json_normalize(df['RAW'])
    CoinTable=pd.concat([c1,c2],axis=1)
    col=CoinTable.columns
    for c in col:
        c2=c[4:]
        CoinTable=CoinTable.rename(columns={c:c2})
    
    return (CoinTable)

GetCoinList(coins)

CoinTable.head()



coins2=['BTC','BNB','ETC','ETH','DOGE','LTC']
def GetCoin(name):
    global coins2, coinmap
    coinmap={}
    hist='https://min-api.cryptocompare.com/data/v2/histoday?'
    api='YOURAPIKEYHERE'
    for coin in coins2:
        params=(
            'extraParams=DogeDash&'
            f'fsym={coin}&'
            'tsym=USD&'
            f'api_key={api}&'
            'limit=30')
        r2url=hist+params
        r=requests.get(r2url).json()
        r=pd.json_normalize(r)
        coindf=pd.DataFrame(r['Data.Data'])
        coindf=coindf.explode('Data.Data').reset_index(drop=True)
        coindf=pd.json_normalize(coindf['Data.Data'])
        coindf['symbol']=coin
        coinmap[coin]=coindf

    return (coinmap)
    
GetCoin(coins2)       

coinmap.keys()

CoinHistory=pd.concat(coinmap)
CoinHistory.head()