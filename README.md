# Interactive Brokers Trading Bot

Simple open source tool for trading shares on ASX with [Interactive Brokers Gateway API](https://interactivebrokers.github.io/tws-api/introduction.html)

## Authors

**[James Dalton](https://jamesdalton.io)**

## Credits

- **[brentjm](https://github.com/brentjm/Interactive-Brokers-API)** starter python class for working with Interactive Brokers API

## Built with

- [Python](https://www.python.org/) - Scripting Language
- [Interactive Brokers Gateway](https://www.interactivebrokers.com.au/en/index.php?f=16457) - Enabling API connection to Interactive Brokers API
- [Interactive Brokers Python API](http://interactivebrokers.github.io/) - Interactive Brokers API
- [Visual Studio Code](https://code.visualstudio.com/) - IDE

## Instructions

**1. Download and install [Interactive Brokers Python API](http://interactivebrokers.github.io/) and [Interactive Brokers Gateway](https://www.interactivebrokers.com.au/en/index.php?f=16457)**

**Note:** [Interactive Brokers Gateway](https://www.interactivebrokers.com.au/en/index.php?f=16457), and [Trader Work Station (TWS)](https://www.interactivebrokers.com/en/index.php?f=16040), have the same API (for the purposes of this tool) and can be used interchangeably

**2. Clone repo**

```sh
git clone https://github.com/jdalton92/ib-trading-bot.git
```

**3. Create python virtual environment in root directory**

```sh
ib-trading-bot$ python -m venv venv
```

**4. Activate virtual environment**

windows:

```sh
ib-trading-bot$ venv\Scripts\activate
```

unix/mac:

```sh
ib-trading-bot$ source venv/bin/activate
```

**5. Create a wheel of the Interactive Brokers API from the directory of the TWS API installed in Step 1**

```sh
TWS API$ python setup.py bdist_wheel
```

**Note:** you will likely have to install wheel package to your Python virtual environment before being able to make a wheel, with the following command

```sh
TWS API$ python -m pip install wheel
```

**6. Install Interactive Brokers API wheel**

```sh
ib-trading-bot$ python3 -m pip install --user --upgrade "C:/location/to/TWS API/dist/ibapi-9.75.1-py3-none-any.whl"
```

**Note:** the file name version will have to match your downloaded version of the Interactive Brokers API, so change _ibapi-9.75.1_ to your installed version

**7. Start IB Gateway, or TWS, and login**

**Note:** ensure in your IB Gateway/TWS configuration to [enable API connections](https://interactivebrokers.github.io/tws-api/initial_setup.html#enable_api), and ensure the port is matching the below;

IB Gateway

> Paper Trading: PORT 7497
> Live Trading: PORT 7496

IB TWS

> Paper Trading: PORT 4002
> Live Trading: PORT 4001

**8. Create a _env_config.py_ file in your project root directory**

Store the following your IP address, and your port number (from above) as strings as follows:

```sh
import os

os.environ["IP_ADDRESS"] = "your.IP.address"
os.environ["PORT"] = "portnumber"
```

**Note:** ensure your TWS, or Gateway, allows connections from your IP address listed in the above file

**9. Ensure you have access to [market data subscriptions](https://interactivebrokers.github.io/tws-api/market_data.html) to avoid getting "no market data permissions" error**. To access the American stock exchanges, login to Interactive Brokers dashboard, and scroll to _Market Data Subscriptions_ in the footer. Click the configure button on _Current GFIS Subscriptions_ and under the _North American_ header and _Level 1 (NBBO)_ card select the **NASDAQ (Network C/UTP)** (USD 1.50 / month), or **NYSE (Network A/CTA)** (USD 1.50 / month) to get access to live data for either of these markets. Click _continue_ and confirm the request. I chose **NASDAQ (Network C/UTP)** to access stock information like AAPL, MSFT, AMZN, FB, GOOG, and NFLX.

**10. Navigate to root directory, and start main.py**

```sh
ib-trading-bot$ python main.py
```

**11. TBC**

**12. TBC**
