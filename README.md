# Interactive Brokers Trading Bot

Simple open source tool for trading shares on NASDAQ with [Interactive Brokers Gateway API](https://interactivebrokers.github.io/tws-api/introduction.html), and [ib_sync](https://github.com/erdewit/ib_insync) api wrapper

## Authors

**[James Dalton](https://jamesdalton.io)**

## Credits

- **[Ewald de Wit](https://github.com/erdewit)** for [ib_sync](https://github.com/erdewit/ib_insync), the python sync/async framework for Interactive Brokers API

## Built with

- [Python](https://www.python.org/) - Scripting Language
- [Interactive Brokers Gateway](https://www.interactivebrokers.com.au/en/index.php?f=16457) - Enabling API connection to Interactive Brokers API (or alternatively use [Interactive Brokers TWS](https://interactivebrokers.github.io/tws-api/introduction.html) which is essentially the same API with a graphical user interface)
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
ib-trading-bot$ pipenv install
```

**4. Activate virtual environment**

```sh
ib-trading-bot$ pipenv shell
```

**5. Install ib_synx**

```sh
ib-trading-bot$ pip install ib_sync
```

**6. Start IB Gateway, or TWS, and login**

**Note:** ensure in your IB Gateway/TWS configuration to [enable API connections](https://interactivebrokers.github.io/tws-api/initial_setup.html#enable_api), and ensure the following settings in Configure > API > Settings:

ClientId matches what you choose in Step 8, your local host IP Address is listed as a trusted connection, and the Port is matching the below;

IB Gateway

> Paper Trading: PORT 7497

> Live Trading: PORT 7496

IB TWS

> Paper Trading: PORT 4002

> Live Trading: PORT 4001

**7. Create a _env_config.py_ file in your project root directory**

Store the following your IP address, your port number (from above), and clientId number (can choose any number as long as it matches what you input in Step 7.), as strings as follows:

```sh
import os

os.environ["IP_ADDRESS"] = "your.IP.address"
os.environ["PORT"] = "portnumber"
os.environ["CLIENTID"] = "clientIdNumber"
```

**Note:** ensure your TWS, or Gateway, allows connections from your IP address listed in the above file

**8. Ensure you have access to [market data subscriptions](https://interactivebrokers.github.io/tws-api/market_data.html) to avoid getting "no market data permissions" error**. To access the American stock exchanges, login to Interactive Brokers dashboard, and scroll to _Market Data Subscriptions_ in the footer. Click the configure button on _Current GFIS Subscriptions_ and under the _North American_ header and _Level 1 (NBBO)_ card select the **NASDAQ (Network C/UTP)** (USD 1.50 / month), or **NYSE (Network A/CTA)** (USD 1.50 / month) to get access to live data for either of these markets. Click _continue_ and confirm the request. I chose **NASDAQ (Network C/UTP)** to access stock information like AAPL, MSFT, AMZN, FB, GOOG, and NFLX.

**9. Navigate to root directory, and start main.py**

```sh
ib-trading-bot$ python main.py
```

**Note:** ensure you are not logged into the Interactive Brokers online portal via a web browser/mobile at the same time, or you _may_ get errors as saying Interactive Brokers TWS API only allows connections from one IP address at a time

**11. TBC**

**12. TBC**
