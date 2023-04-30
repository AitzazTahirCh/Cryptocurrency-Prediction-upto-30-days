#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[1]:


import numpy as np
import pandas as pd
import datetime as dt

import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras.layers import Dense, LSTM, Dropout,Flatten
from tensorflow.keras import Sequential
#from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


# 

# In[2]:


df = pd.read_csv('BTC-CoinS.csv')


# In[3]:


train_dates = pd.to_datetime(df['Date'])


# 

# In[4]:


df3 = pd.read_csv("predictionn.csv")
df3


# In[5]:


#df1=df.reset_index()['priceUSD']
df4=df3.reset_index()['BTC price ']


# In[6]:


cols = list(df)[1]
#Date column are not used in training. 
print(cols) #['BTC priceUSD', 'GOLD price', 'sliver price', 'Close price Nasdq']


# In[7]:


cols


# In[8]:


df1=df[cols].astype(float)


# In[9]:


df1.head()


# In[10]:


from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
df1=scaler.fit_transform(np.array(df1).reshape(-1,1))


# In[11]:


##splitting dataset into train and test split
training_size=int(len(df1)*0.75)
test_size=len(df1)-training_size
train_data,test_data=df1[0:training_size,:],df1[training_size:len(df1),:1]


# In[12]:


import numpy
# convert an array of values into a dataset matrix
def create_dataset(dataset, time_step=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-time_step-1):
		a = dataset[i:(i+time_step), 0]   ###i=0, 0,1,2,3-----99   100 
		dataX.append(a)
		dataY.append(dataset[i + time_step, 0])
	return numpy.array(dataX), numpy.array(dataY)


# In[13]:


# reshape into X=t,t+1,t+2,t+3 and Y=t+4
time_step = 10
X_train, y_train = create_dataset(train_data, time_step)
X_test, ytest = create_dataset(test_data, time_step)


# In[14]:


# reshape input to be [samples, time steps, features] which is required for LSTM
X_train =X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1] , 1)


# In[15]:


model=Sequential()
model.add(LSTM(50,return_sequences=True,input_shape=(time_step,1)))
model.add(LSTM(50,return_sequences=True))
model.add(LSTM(50))
model.add(Dropout(0.2))

model.add(Dense(5))

model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='adam')


# In[16]:


#model.fit(X_train,y_train,validation_data=(X_test,ytest),epochs=100,batch_size=64,verbose=1)

history=model.fit(X_train,y_train,validation_split=0.2,epochs=100,batch_size=64,verbose=1)


# In[17]:


### Lets Do the prediction and check performance metrics
train_predict=model.predict(X_train)
test_predict=model.predict(X_test)


# In[18]:


# Estimate model performance
trainScore = model.evaluate(X_train, y_train, verbose=0)
print('Train Score: %f MSE (%f RMSE)' % (trainScore, math.sqrt(trainScore)))
testScore = model.evaluate(X_test, ytest, verbose=0)
print('Test Score: %f MSE (%f RMSE)' % (testScore, math.sqrt(testScore)))


# In[19]:


##Transformback to original form
train_predict=scaler.inverse_transform(train_predict)
test_predict=scaler.inverse_transform(test_predict)


# In[20]:


### Calculate RMSE performance metrics
import math
from sklearn.metrics import mean_squared_error
math.sqrt(mean_squared_error(y_train,train_predict))


# In[21]:


### Calculate RMSE performance metrics

math.sqrt(mean_squared_error(ytest,test_predict))


# In[22]:


### Plotting 
# shift train predictions for plotting
look_back=10
trainPredictPlot = numpy.empty_like(df1)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict


# In[23]:


# shift test predictions for plotting
testPredictPlot = numpy.empty_like(df1)
testPredictPlot[:, :] = numpy.nan
#testPredictPlot[len(train_predict)+(look_back*2)+1:len(df1)-1, :] = test_predict
testPredictPlot[len(train_predict)+(look_back*2)+1:len(df1)-1, :] = test_predict


# In[24]:


# plot baseline and predictions
plt.plot(scaler.inverse_transform(df1))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.savefig('foo.png')
#plt.show() 


# In[25]:


len(test_data)


# In[26]:


x_input=test_data[477:].reshape(1,-1)
x_input.shape


# In[27]:


temp_input=list(x_input)
temp_input=temp_input[0].tolist()


# In[28]:


# demonstrate prediction for next 10 days
from numpy import array

lst_output=[]
n_steps= 10
i=0
while(i<30):
    
    if(len(temp_input)>10):
        #print(temp_input)
        x_input=np.array(temp_input[1:])
        print("{} day input {}".format(i,x_input))
        x_input=x_input.reshape(1,-1)
        x_input = x_input.reshape((1, n_steps, 1))
        #print(x_input)
        yhat = model.predict(x_input, verbose=0)
        print("{} day output {}".format(i,yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input=temp_input[1:]
        #print(temp_input)
        lst_output.extend(yhat.tolist())
        i=i+1
    else:
        x_input = x_input.reshape((1, n_steps,1))
        yhat = model.predict(x_input, verbose=0)
        print(yhat[0])
        temp_input.extend(yhat[0].tolist())
        print(len(temp_input))
        lst_output.extend(yhat.tolist())
        i=i+1
    
lst_output=scaler.inverse_transform(lst_output)

x0 = str(lst_output[0])
print("x0 : ",x0)
x1 = str(lst_output[1])
print("x1 : ",x1)
x2 = str(lst_output[2])
print("x2 : ",x2)
x3 = str(lst_output[3])
print("x3 : ",x3)
x4 = str(lst_output[4])
print("x4 : ",x4)
x5 = str(lst_output[5])
print("x5 : ",x5)
x6 = str(lst_output[6])
print("x6 : ",x6)
x7 = str(lst_output[7])
print("x7 : ",x7)
x8 = str(lst_output[8])
print("x8 : ",x8)
x9 = str(lst_output[9])
print("x9 : ",x9)
x10 = str(lst_output[10])
print("x10 : ",x10)
x11 = str(lst_output[11])
print("x11 : ",x11)
x12 = str(lst_output[12])
print("x12 : ",x12)
x13 = str(lst_output[13])
print("x13 : ",x13)
x14 = str(lst_output[14])
print("x15 : ",x14)
x15 = str(lst_output[15])
print("x15 : ",x15)
x16 = str(lst_output[16])
print("x16 : ",x16)
x17 = str(lst_output[17])
print("x17 : ",x17)
x18 = str(lst_output[18])
print("x18 : ",x18)
x19 = str(lst_output[19])
print("x19 : ",x19)
x20 = str(lst_output[20])
print("x20 : ",x20)
x21 = str(lst_output[21])
print("x21 : ",x21)
x22 = str(lst_output[22])
print("x22 : ",x22)
x23 = str(lst_output[23])
print("x23 : ",x23)
x24 = str(lst_output[24])
print("x24 : ",x24)
x25 = str(lst_output[25])
print("x25 : ",x25)
x26 = str(lst_output[26])
print("x26 : ",x26)
x27 = str(lst_output[27])
print("x27 : ",x27)
x28 = str(lst_output[28])
print("x28 : ",x28)
x29 = str(lst_output[29])
print("x29 : ",x29)
lines = [x0,x1, x2, x3, x4, x5, x6, x7 ,x8 ,x9 ,x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22 , x23, x24, x25, x26, x27, x28, x29]
with open('readme.txt', 'w') as f:
    f.writelines('\n'.join(lines))


import urllib
mydata=[('one',lst_output)]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path='http://localhost/lstm/test.php'    #the url you want to POST to
req=urllib.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib.urlopen(req).read()
print(lst_output) #output


# In[29]:


day_new=np.arange(1,101)
day_pred=np.arange(101,134)


# In[30]:


len(df1)


# In[31]:


#lst_output=scaler.inverse_transform(lst_output)


# In[32]:


### Calculate RMSE performance metrics
import math
from sklearn.metrics import mean_squared_error
math.sqrt(mean_squared_error(lst_output,df4))


# In[33]:


df4


# In[34]:


math.sqrt(mean_squared_error(lst_output,df4))


# In[35]:


# plot baseline and predictions
plt.plot(df4)
plt.plot(lst_output)
plt.show() #output


# In[36]:


from sklearn.metrics import mean_squared_error

rms = mean_squared_error(lst_output, df4, squared=False)


# In[37]:


rms


# In[ ]:




