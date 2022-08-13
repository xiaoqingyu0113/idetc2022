from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import src.util.feature_extract as fe_util
from src.util.features import extract_features
import time

assembly_id_list = ['7778_3a9748b3','148051_ad8f6d60','148105_610e3d11','148137_f6cfb712']
assembly_id = assembly_id_list[1]

assembly_data = fe_util.read_json(assembly_id)
print(assembly_data.keys())
# print(assembly_data["contacts"])



