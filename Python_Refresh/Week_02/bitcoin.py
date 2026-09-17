import requests

def main():
    n = float(input("Number of bitcoin you want to purchase: "))
    amount = bitcoin(n)
    print(f"you need to pay {amount} USD to purchase {n} bitcoin")

def bitcoin(n):
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    
    data_bitcoin = response.json()
    print(f"{data_bitcoin}")

    Per_Unit = float(data_bitcoin["data"]["amount"])
    return n * Per_Unit

main()