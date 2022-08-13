from PIL import Image
import numpy as np
import os
from src.util.features import extract_features
import glob
import matplotlib.pyplot as plt
import pandas as pd
import json

data_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../full_data/train/'))
json_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../fingerprints/json/'))
csv_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../fingerprints/csv/'))

font_size = 4

def read_assembly_image(assembly_id):
    return np.array(Image.open(f"{data_root}/{assembly_id}/assembly.jpg"))


def read_body_images_from_assembly(assembly_id,body_id=None):
    if body_id:
        return np.array(Image.open(f"{data_root}/{assembly_id}/{body_id}.jpg"))
    else:
        body_img_dict = {}
        image_names = glob.glob(f"{data_root}/{assembly_id}/*.jpg")
        for image_name in image_names:
            body_name = image_name.split("/")[-1][:-4]
            body_img_dict[body_name] =  np.array(Image.open(image_name))
        return body_img_dict



def plot_assembly_images(assembly_id_list):
    N = len(assembly_id_list)
    nrow = int(np.ceil(np.sqrt(N)))
    ncol = int(np.ceil(N/nrow))
    fig,axarr = plt.subplots(nrows=nrow,ncols=ncol)
    axarr = axarr.flatten()
    for assembly_id, ax in zip(assembly_id_list,axarr):
        ax.imshow(read_assembly_image(assembly_id))
        ax.set_title(f"assembly_id = {assembly_id}",fontdict={'fontsize': font_size})
    plt.show()
    return 


def plot_body_images_from_assembly(assembly_id,body_id=None):

    body_img_dict = read_body_images_from_assembly(assembly_id,body_id=body_id)
    if body_id:
        plt.imshow(body_img_dict)
        plt.title(f"body_id = {body_id}")
    else:
        N = len(body_img_dict)
        nrow = int(np.ceil(np.sqrt(N)))
        ncol = int(np.ceil(N/nrow))
        fig,axarr = plt.subplots(nrows=nrow,ncols=ncol)
        axarr = axarr.flatten()
        axarr[0].imshow(body_img_dict["assembly"])
        axarr[0].set_title(f"assembly_id = {assembly_id}",fontdict={'fontsize': font_size})
        axarr[0].get_xaxis().set_visible(False)
        axarr[0].get_yaxis().set_visible(False)
        
        offset = 1
        for idx,bodyid in enumerate(body_img_dict):
            if bodyid == "assembly":
                offset=0
                continue
            ax = axarr[idx+offset]
            ax.imshow(body_img_dict[bodyid])
            ax.set_title(f"body_id = {bodyid}",fontdict={'fontsize': font_size})
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()
    return 

def read_fingerprint(assembly_id):
    return pd.read_csv(f"{csv_root}/{assembly_id}.csv",index_col=0).T

def read_assembly_fingerprint(assembly_id):
    fp = pd.read_csv(f"{csv_root}/{assembly_id}.csv",index_col=0).T
    return fp["assembly.jpg"].to_numpy()

def read_json(assembly_id):
    f = open (f"{json_root}/{assembly_id}.json", "r")
    assembly_data = json.loads(f.read())
    f.close()
    return assembly_data