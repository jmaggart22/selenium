from browse import Browse
import datetime

symbol = input("Ticker symbol: ")

p = Browse(symbol)

file = 'csv.txt'

def get_time():
    now = datetime.datetime.now()
    hms = now.strftime('%H:%M:%S')
    return hms

def csv(price):
    with open(file, 'a') as f:
        time = get_time()
        f.write(price+","+time+"\n")

while True:
    csv(p.get_price())
    print(p.get_price())

