from PIL import Image
import numpy as np
import os

data_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../full_data/train/'))

def read_assembly_image(assembly_id):
    im = Image.open(f"{data_root}/{assembly_id}/assembly.jpg") 
    return np.array(im)
