import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision.utils import make_grid

def show_images(images:torch.Tensor,mean=(0.5,),std=(0.5,)):
  """
  Shows a grid of images.

  Args:
    images: A tensor of size (batch_size, height, width)
    mean: A tuple of mean values for each channel
    std: A tuple of standard deviation values for each channel
  """

  mean,std=torch.tensor(mean),torch.tensor(std)
  images=images*std+mean

  nrows=images.shape[0]//8
  grid=make_grid(images,nrows=nrows)
  grid=grid.permute(1,2,0)
  plt.imshow(grid)
  plt.show()


