##TGV feed rate trial 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


##get feedrate data, name df
df=pd.read_csv(r'.\tgv_feedrate.csv')
df.head()

##drop columns which do not have data yet
##drop blanks
df.drop(columns=['feeddayeight','feeddaysixteen'], inplace=True)
df.dropna(axis=0,inplace=True)
df.tail()

#split data into treatments. X=animals with exposed moms. Y=animals with unexposed moms
X=df[df['TX']=='Comp']
Y=df[df['TX']=='Uncomp']

##histogram for size, d1
sizemin=min(X['d1_size'].min(),Y['d1_size'].min())
sizemax=max(X['d1_size'].max(),Y['d1_size'].max())
sizebins = np.linspace(sizemin, sizemax, 10)
plt.hist(X['d1_size'], sizebins, alpha=0.5, label='Comp')
plt.hist(Y['d1_size'], sizebins, alpha=0.5, label='Uncomp')
plt.legend(loc='upper left')
plt.xticks(sizebins)
plt.show()

##histogram for amount eaten. d1
eatenmax=max(X['d1_eaten'].max(),Y['d1_eaten'].max())
eatenmin=min(X['d1_eaten'].min(),Y['d1_eaten'].min())
eatenbins = np.linspace(eatenmin, eatenmax, 10)
plt.hist(X['d1_eaten'], eatenbins, alpha=0.5, label='Comp')
plt.hist(Y['d1_eaten'], eatenbins, alpha=0.5, label='Uncomp')
plt.legend(loc='upper right')
plt.xticks(eatenbins)
plt.show()


##histogram for amount eaten per unit size, day 1
sizepermin=min(X['d1_eatenpersize'].min(),Y['d1_eatenpersize'].min())
sizepermax=max(X['d1_eatenpersize'].max(),Y['d1_eatenpersize'].max())
eatenpersizebins = np.linspace(sizepermin, sizepermax, 10)
plt.hist(X['d1_eatenpersize'], eatenpersizebins, alpha=0.5, label='Comp')
plt.hist(Y['d1_eatenpersize'], eatenpersizebins, alpha=0.5, label='Uncomp')
plt.legend(loc='upper right')
plt.xticks(eatenpersizebins, rotation=90)
plt.show()


###loop to create the above histograms more quickly
for column in ['d1_size','d1_eaten','d1_eatenpersize']:
    columnmin=min(X[column].min(),Y[column].min())
    columnmax=max(X[column].max(),Y[column].max())
    bins = np.linspace(columnmin, columnmax, 10)
    plt.hist(X[column], bins, alpha=0.5, label='Comp')
    plt.hist(Y[column], bins, alpha=0.5, label='Uncomp')
    plt.legend(loc='upper right')
    plt.title(column)
    plt.xticks(bins, rotation=90)
    plt.show()



##loop to create the ttests for all 3 variables
for column in ['d1_size','d1_eaten','d1_eatenpersize']:
    #perform Welch's t-test, no assumption of equal variance
    result=ttest_ind(X[column], Y[column], equal_var=False)
    print(column, result)
    #indicates sig difference in amount eaten and amount eaten per unit size


##boxplot for amount eaten per unit size
df[['TX','d1_eatenpersize']].boxplot(by='TX', grid=False)    
##indicates lesser consumption per unit size in comp animals