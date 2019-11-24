import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = './data/'
data = pd.read_csv(path + 'copy1.csv')
regions = data.groupby('Region of Incident').size()
sum_by_year = pd.pivot_table(data, index = ['Region of Incident'], values = ['Total Dead and Missing'], columns = ['Reported Year'], aggfunc = [np.sum],fill_value = 0)
# , fill_value = 'None'

print(sum_by_year.columns)
print(sum_by_year.index)
print(sum_by_year.head(2))

sum_by_year.columns.names=['Sum','Total Dead and Missing','Reported Year']
x = sum_by_year.columns.get_level_values('Reported Year')
y = sum_by_year.values


fig = plt.figure(figsize=(20,30))
fig.subplots_adjust(hspace=0.5, wspace=0.4)
# distance between plots

n = 1
i = 0
for region in regions.index:
    ax = fig.add_subplot(5,3,n) 
    # 5rows, 3columns, No.n
    ax.scatter(x,y[i])
    ax.set_xlabel('Year',fontsize = 12)
    ax.set_ylabel('Dead and Missing',fontsize = 12)
    ax.legend([region],loc = 'upper right')
    n += 1
    i += 1

plt.show()