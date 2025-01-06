from setuptools import setup, find_packages

setup(
    name="currency-backend",
    version="1.0.0",
    author="Tvoje Jméno",
    description="Backend aplikace pro kurzy měn, akcií a kryptoměn.",
    install_requires=[
        "sanic==22.9.1",
        "apscheduler==3.10.1",
        "forex-python==1.8",
        "ccxt==3.0.85",
        "matplotlib==3.7.2",
        "redis==5.0.0",
        "pypyodbc==1.3.6",
        "pytest==7.4.0",
        "pytest-asyncio==0.21.0",
        "cryptography==41.0.3"
    ],
    packages=find_packages(),
)
