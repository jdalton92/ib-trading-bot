import os
import sys
import ib_api
import env_config
from datetime import datetime, timedelta, date


def main():
    ip_address = os.getenv("IP_ADDRESS")
    port = int(os.getenv("PORT"))
    clientId = int(os.getenv("CLIENTID"))

    app = ib_api.main(ip_address, port, clientId)

    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=15)
    symbols = ["MSFT"]

    bars = app.get_price_history(
        symbols=symbols, rth=False, start_date=start_date, end_date=end_date)

    quote = (app.get_quotes(["MSFT"]))
    print(quote)

    # print(bars.head(10))


if __name__ == "__main__":
    main()
