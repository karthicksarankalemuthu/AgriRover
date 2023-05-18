from cv2 import  VideoCapture,imread,imshow,imwrite,waitKey,destroyWindow,resize,imencode
from io import BytesIO

cam_port = 0

def getimg():
     cam = VideoCapture(cam_port)
     result, image = cam.read()
     if result:
        #imshow("img", image)
        img =resize(image, (256, 256))
        #return img
        imshow("img", img)
       # imwrite("GeeksForGeeks.png", image)
        waitKey(0)
       # destroyWindow("GeeksForGeeks")
        #im_buf_arr =imencode(".jpg", img)
        #byte_im =BytesIO(img)
     else:
      print("error")
     #return image
    # img =resize(image, (256, 256))
     return img
    #imshow("img", img)
#getimg()
#+14155238886
#AC0b7a6c73a5a4790379e9c8313c90e5e1
#dcfbf615c2d83955a699400ce84e8096
#AC0c228c92c51a2ec0f68388287e69e4e4
#b4104194a0dc91e0580a66526ee0001b
#+1 270 713 5220