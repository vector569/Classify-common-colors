import numpy as np
import tensorflow as tf
import pandas as pd
from create_csv import *


list_ = ["black","white","blue"]
N = 10
height = 5
width = 5
create_csv(list_,N,"medium",height,width,"data.csv")

data = pd.read_csv('data.csv')
print(data.head())
