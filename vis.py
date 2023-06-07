import csv
from datetime import datetime
import matplotlib.pyplot as pyplot

file = 'csv.txt'

with open(file) as f:
    reader = csv.reader(f)

    prices, times = [], []
    for col in reader:
        time = datetime.strptime(col[1], '%H:%M:%S')
        price = float(col[0])
        times.append(time)
        prices.append(price)

pyplot.style.use('ggplot')
fig, ax = pyplot.subplots()
ax.plot(times, prices, c='red')
fig.autofmt_xdate()
fig.canvas.manager.set_window_title(file)
ax.set_title('Price Movement', fontsize=20)
ax.set_xlabel('Hour:Minute:Second', fontsize=13)
ax.set_ylabel('Price', fontsize=13)

pyplot.show()
