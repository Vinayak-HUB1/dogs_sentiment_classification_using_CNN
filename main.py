from fastapi import FastAPI,UploadFile,File
import uvicorn
from keras.models import  load_model
import tensorflow as tf
import cv2
import shutil
import numpy as np
import os
from fastapi.responses import FileResponse
import logging


LOG_DIR = "Logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(filename=os.path.join(LOG_DIR, "running_logs.log"),    level=logging.INFO,
                    filemode='a',
                    format='[%(asctime)s: %(levelname)s: %(module)s]: >>>>>>>>>  %(message)s')

app = FastAPI(title="dog mood detection")

model = load_model("model.h5")



@app.post("/pred")
async def prediction(image:UploadFile = File(...)):
    file_dir = "Test"
    img_name = "input.jpg"
    os.makedirs(file_dir,exist_ok=True)
    with open(os.path.join(file_dir,img_name),"wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
        image = cv2.imread(os.path.join(file_dir,img_name))
        resized_image = tf.image.resize(image,(256,256))
        yhat = model.predict(np.expand_dims(resized_image/255,0))
    if yhat < 0.5:
        result =  "puppy is feeling happy"
    else:
        result =  "puppy is in sad mood"
    return result




@app.get("/image")
def image_filter():
    return FileResponse("Test\input.jpg")



if  __name__ == '__main__':
    uvicorn.run(app)