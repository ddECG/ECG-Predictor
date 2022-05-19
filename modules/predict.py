# -----------------------------------------------------------------------------
# Module: User interface
#
# What: User interface logic and definitions.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules 
import os
import torch
import h5py
import json
import numpy as np
import pandas as pd
from pathlib import Path

# Local resources 
from modules.resnet import ResNet1d
from modules.functions import resource_path

# Constants
N_LEADS = 12
SEED = 2
TRACES = "tracings"
ID = "exam_id"
AGE = "true_age"

# ------------------------------------------------------------------------------
# 2 - Functions
# ------------------------------------------------------------------------------
def predict(model_folder, hdf_path, exam_id):
    """ Predict age using predefined model. """
    
    # Set random seed
    torch.manual_seed(SEED)

    # Get path
    model_path = os.path.join(model_folder, 'model.pth')
    model_path = resource_path(model_path)

    # Set device
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # Define model parameters
    config_path = os.path.join(model_folder, 'config.json')
    config_path = resource_path(config_path)

    # Load config info
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Load model
    checkpoints = torch.load(model_path, map_location=lambda storage, loc: storage)
    model = ResNet1d(input_dim=(N_LEADS, config['seq_length']),
                    blocks_dim=list(zip(config['net_filter_size'], config['net_seq_length'])),
                    n_classes=1,
                    kernel_size=config['kernel_size'],
                    dropout_rate=config['dropout_rate'])
    model.load_state_dict(checkpoints["model"])
    model = model.to(device)

    # Load data
    data = h5py.File(hdf_path, 'r')
    traces = data[TRACES]
    ids = data[ID]
    age = data[AGE]

    # Prepare data for mo model
    model.eval() # Turn on prediction mode

    # Find index
    index = np.array(ids)
    index = np.where(index == exam_id)
    index = int(index[0])

    # Get true age
    true_age = int(age[index])

    # Make prediction
    with torch.no_grad():

        # Make tensor
        x = torch.tensor(traces[index:(index+1), :, :]).transpose(-1, -2)
        
        # Send to GPU/CPU
        x = x.to(device, dtype=torch.float32)

        # Predict
        predicted_age = model(x)
        predicted_age = int(predicted_age.detach().cpu().numpy().flatten())

    # Return
    return(predicted_age, true_age)