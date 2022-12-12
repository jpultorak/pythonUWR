import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan']
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ys = [4, 3.91, 3.99, 4.05, 4.30, 4.10, 3.50, 3.60, 3.90, 4.08, 4, 4.4]

locator = mdates.MonthLocator()
fmt = mdates.DateFormatter('b')


plt.plot(xs, ys)
plt.show()
 # print(np.linspace(0, 365, 13))
