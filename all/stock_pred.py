import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
yearsFmt = mdates.DateFormatter('%Y')

market_train_df = pd.read_csv('marketdata_sample.csv')
news_train_df = pd.read_csv('news_sample.csv')
print (market_train_df.columns)
print (news_train_df.columns)

'''
news_train_df['time']= pd.to_datetime(news_train_df['time']).dt.date
apple_news_sent = news_train_df.groupby(['time','sentimentClass']).count()['sourceTimestamp'].unstack()
print (apple_news_sent[1])

fig,ax = plt.subplots()
ax.bar(apple_news_sent.index,apple_news_sent[-1],label='-1',color='red',bottom=None)
ax.bar(apple_news_sent.index,apple_news_sent[0],label='0',color='blue',bottom=apple_news_sent[-1])
ax.bar(apple_news_sent.index,apple_news_sent[1],label='1',color='green',bottom=apple_news_sent[0])
ax.xaxis.set_major_formatter(yearsFmt)
ax.legend(loc='best')
plt.show()
'''