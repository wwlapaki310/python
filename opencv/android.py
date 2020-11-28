import cv2
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

ip_address='192.168.11.5'
cap = cv2.VideoCapture('http://'+ip_address+':4747/video')
#cap = cv2.VideoCapture('http://192.168.11.5:4747/video')

frame=0
max_frame=50
dataR=[]
dataG=[]
dataB=[]

# 描画領域を取得
#fig, ax = plt.subplots(1, 1)

# y軸方向の描画幅を指定
#ax.set_ylim((0, 255))

x=np.arange(0,1/30*max_frame,1/30)


while frame<max_frame:
    ret,img = cap.read()
    cv2.imshow('img', img)
    #print(img.shape) (480,640,3)
    dataB.append(np.average(img[400:461,400:461,0]))
    dataG.append(np.average(img[400:461,400:461,1]))
    dataR.append(np.average(img[400:461,400:461,2]))
    '''
    plt.plot(x[frame], dataB[frame], color='blue')
    plt.plot(x[frame], dataG[frame], color="green")
    plt.plot(x[frame], dataR[frame], color="red")
    plt.draw()

    line1,=ax.plot(x[frame], dataB[frame], color='blue')
    line2,=ax.plot(x[frame], dataG[frame], color="green")
    line3,=ax.plot(x[frame], dataR[frame], color="red")
    '''

    #plt.draw()
    # 次の描画まで0.01秒待つ

    frame+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

plt.plot(x,dataB,color='blue')
plt.plot(x,dataG,color="green")
#plt.plot(x,dataR,color="red")
plt.show()
cap.release()
cv2.destroyAllWindows()