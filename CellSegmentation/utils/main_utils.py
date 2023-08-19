import os.path
import sys
import yaml
import base64


from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging

def read_yaml_file(file_path:str) -> dict:
    try:
        with oopen(file_path,"rb") as yaml_file:
            logging.info("read yaml file sucessfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e
def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        with open(file_path,"w") as file:
            yaml.dump(cntenet,file)
            logging.info("Sucessfully write_yaml_file")
    except Exception as e:
        raise AppException(e,sys)
def decodeImage(imgstring,fileName):
    imgdata=base64.b64decode(imgstring)
    with open("./data/" + fileName,"wb") as f:
        f.write(imgdata)
        f.close()
    def encodeImageIntoBase64(croppedImagePath):
        with open(croppedImagePath,"rb") as f:
            return base64.b64encode(f.read())
