%matplotlib inline
from matplotlib import pyplot as plt

import torch
import torch.nn as nn
from torch.autograd import Variable

def plot_both(x, y, pred_x=None, pred_y=None, label=""):
    fig = plt.figure(figsize=(8, 4))
    fig.suptitle(label)
    
    plt.subplot(1, 2, 1)
    plt.plot(x.numpy(), y.numpy(), '.', label='Data X -> Y')
    if pred_x is not None:
        plt.plot(x.numpy(), pred_x.numpy(), '.', label='Pred X -> Y')
    plt.legend()
        
    plt.subplot(1, 2, 2)
    plt.plot(y.numpy(), x.numpy(), '.', label='Data Y -> X')
    if pred_y is not None:
        plt.plot(y.numpy(), pred_y.numpy(), '.', label='Pred Y -> X')
    plt.legend()
    
    plt.show()
    return None
  
  test
"hello world"