
import torch
from colorama import Fore, Back

def device_config():

    if torch.cuda.is_available():
        device = 'cuda'
        print(Fore.GREEN+"CUDA is running")
    elif torch.backends.mps.is_available():
        device = 'mps'
        print(Fore.GREEN+"MPS is running")
    else: 
        device = 'cpu'
        print('device is CPU')

    return torch.device(device)
    pass


"""

from colorama import Fore, Back
r = Fore.RED
print(r + "hello world")
"""