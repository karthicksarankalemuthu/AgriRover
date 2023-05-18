from flask import Flask, render_template, request,redirect,Response
import numpy as np
from tensorflow import keras
from cv2 import  VideoCapture,imshow,waitKey,resize,imencode
from io import BytesIO
import webcam
from PIL import Image
import moter
import arm
import msg

app = Flask(__name__)
camera =VideoCapture(1)
def getframe():
        while True:
            success, frame = camera.read()  # read the camera frame
            if not success:
                break
            else:
              ret, buffer =imencode('.jpg', frame)
              frame = buffer.tobytes()
              yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/streaming')
def streaming():
    return Response(getframe(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<string:option>')
def move(option):
    if option=="forword":
        moter.forword()
        return render_template("home.html")
    elif option=="backword":
        moter.backword()
        return render_template("home.html")
    elif option=="right":
        moter.right()
        return render_template("home.html")
    elif option=="left":
        moter.left()
        return render_template("home.html")
    elif option=="stop":
        moter.stop()
        return render_template("home.html")
    return render_template("home.html")

@app.route('/moter1',methods=['GET'])
def moter1():
      angle=request.args.get('angle1')   
      arm.moter1(angle)
      return render_template("home.html")

@app.route('/moter2',methods=['GET'])
def moter2():
      angle=request.args.get('angle2')   
      arm.moter2(angle)
      return render_template("home.html")

@app.route('/predict',methods=['GET'])
def predict():
          model = keras.models.load_model('./leafdiseasesclassifier.h5')
          #testimg="./img/healthy.jpg"
          testimg="./img/late.jpg"
          #testimg="./img/early1.jpg"
          #testimg="./img/mold.jpg"
          #testimg="./img/target.jpg"
          
       #result, image = camera.read()
       #if result:
          #im = Image.fromarray(image, 'RGB')
          #img =testimg.resize((256, 256))
          #img_array=np.array(Image.open(BytesIO(img))) 
          img=keras.preprocessing.image.load_img(testimg)
          img1 =img.resize((256, 256))
          img_array=keras.preprocessing.image.img_to_array(img1) 
          #print(img_array.shape)
          div=img_array/255
          img_array1=np.expand_dims(div,0)
          #img2=np.array(img_array1)
       #print(img_array1.shape)
          pre=model.predict(img_array1)
          #print(pre)
          ans=np.argmax(pre[0])
          acc=round(100*np.max(pre[0]),2)
          #print(acc)
          class_names=['Tomato_Bacterial_spot',
                   'Tomato_Early_blight',
                    'Tomato_Late_blight',
                   'Tomato_Leaf_Mold',
                   'Tomato_Septoria_leaf_spot',
                   'Tomato_Spider_mites',
                   'Tomato_Target_Spot',
                   'Tomato_Tomato_Yellow_Leaf_Curl_Virus',
                  'Tomato_Tomato_mosaic_virus',
                 'Tomato_healthy']
          label=class_names[ans]
          msg.sendmsg(ans)
          return render_template("home.html",prediction=label,accrency=acc)
 

if __name__ == '__main__':
    app.run(debug=True)
