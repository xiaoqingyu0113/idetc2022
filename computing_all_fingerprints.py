from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import src.util.feature_extract as fe
from src.util.features import extract_features

data_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'full_data/train/'))

if __name__ == "__main__":
    assembly_paths = glob.glob(data_root+'/*')
    for iter,filepath in enumerate(assembly_paths):
        print(f"\niter = {iter}, assembly_id = filepath")
        extract_features(filepath, model='ResNet50', write_to=filepath+'/fingerprints.csv', recursive=False)