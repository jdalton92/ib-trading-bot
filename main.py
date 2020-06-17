import os
import sys
import ib_api
import env_config
from datetime import datetime, timedelta


def main():
    ip_address = os.getenv("IP_ADDRESS")
    port = int(os.getenv("PORT"))

    app = ib_api.main(ip_address, port)

    end_date = datetime.today()
    start_date = end_date - timedelta(days=15)
    symbols = ["MSFT"]

    bars = app.get_price_history(
        symbols=symbols, rth=False, start_date=start_date, end_date=end_date)

    print(bars.head(10))


if __name__ == "__main__":
    main()
