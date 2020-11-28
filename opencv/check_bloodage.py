import cv2
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

frame=0
dataR=[]
dataG=[]
dataB=[]
vidcap=cv2.VideoCapture("2.mp4")
success,img=vidcap.read()
#(1080,1920,3)
while success:
    dataB.append(np.average(img[400:461,400:461,0]))
    dataG.append(np.average(img[400:461,400:461,1]))
    dataR.append(np.average(img[400:461,400:461,2]))
    frame+=1
    success,img=vidcap.read()

"""
x=np.arange(0,1/30*frame,1/30)
plt.plot(x,dataB,color='blue')
plt.plot(x,dataG,color="green")
#plt.plot(x,dataR,color="red")
plt.show()

"""

x=np.arange(0,1/30*frame,1/30)
avedata=np.convolve(dataG,np.ones(1)/1,mode="same")
fit=np.poly1d(np.polyfit(x,avedata,10))
data=-(avedata-fit(x))
plt.plot(x,data)
from peakdetect import peakdetect
peaks=np.array(peakdetect(data,lookahead=10)[0])
plt.plot(1/30*peaks[:,0:1],peaks[:,1:2],"ro")
plt.show()

peak_count=peaks[:,0:1].shape[0]
print(peak_count)
myakuhaku_1min=60*peak_count/(peaks[:,0:1][peak_count-1]/30)
print("脈拍は"+str(myakuhaku_1min)+"回/分です")

data=np.convolve(data,np.ones(1)/1,mode="same")
data1stD=np.gradient(data)
plt.plot(np.arange(0,len(data1stD),1),data1stD)
plt.show()

data1stD=np.convolve(data1stD,np.ones(1)/1,mode="same")
data2ndD=np.gradient(data1stD[100:1900])
plt.plot(np.arange(0,len(data2ndD),1),data2ndD)
plt.show()