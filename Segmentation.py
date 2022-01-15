import cv2
import os
import shutil
import pathlib
import json
import base64

def get_images_from_video(video_name, time_F):
    video_images = []
    vc = cv2.VideoCapture(video_name)
    c = 1
    
    if vc.isOpened(): #判斷是否開啟影片
        rval, video_frame = vc.read()
    else:
        rval = False

    while rval:   #擷取視頻至結束
        rval, video_frame = vc.read()
        
        if(c % time_F == 0): #每隔幾幀進行擷取
            video_images.append(video_frame)     
        c = c + 1
    vc.release()
    
    return video_images


time_F = 2 #time_F越小，取樣張數越多
video_name = 'test01.avi' #影片名稱
video_images = get_images_from_video(video_name, time_F) #讀取影片並轉成圖片

list=os.listdir()
if("video_cut" not in list):
    os.mkdir("video_cut")
else:
    shutil.rmtree("video_cut")
    os.mkdir("video_cut")

filename = 'C:\AppServ\www\TFjs\\video_cut'  #video_cut的絕對路徑(記得加上跳脫字元避免\v)
for i in range(0, len(video_images)-1): #顯示出所有擷取之圖片
    print(video_images[i].shape)
    cv2.imwrite(filename+'\\test0'+str(i)+'.png', video_images[i]) #(記得加上跳脫字元避免\v)

count=len(os.listdir(filename))
print(count)

#通過opencv轉base64
img_im= cv2.imread("C:\AppServ\www\TFjs\\video_cut\\test00.png")
aa=base64.b64encode(cv2.imencode('.png',img_im)[1]).decode()
print(len(aa))  



    