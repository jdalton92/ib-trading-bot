import os
import sys
import env_config
import ib_insync
import numpy as np
import pandas as pd
from datetime import datetime, timedelta, date


def main(ip_address, port, clientId, ticker=None):
    """
    Connect through ib_sync
    """
    ib = ib_insync.IB()
    ib.connect(ip_address, port, clientId, readonly=True)

    contract = ib_insync.Stock(ticker, 'SMART', 'USD')

    bars = ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='5 D',
        barSizeSetting='1 day',
        whatToShow='MIDPOINT',
        useRTH=True
    )

    df = ib_insync.util.df(bars)
    print(df)

if __name__ == "__main__":
    ip_address = os.getenv("IP_ADDRESS")
    port = int(os.getenv("PORT"))
    clientId = int(os.getenv("CLIENTID"))
    ticker = sys.argv[1]

    main(ip_address, port, clientId, ticker)
