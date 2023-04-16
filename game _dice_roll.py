#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


def dice():
    i = np.random.randint(1,7)
    if i == 1:
        print(' =======\n|       |\n|   o   |\n|       |\n =======')
    elif i == 2:
        print(' =======\n|   o   |\n|       |\n|   o   |\n =======')
    elif i == 3:
        print(' =======\n|   o   |\n|   o   |\n|   o   |\n =======')
    elif i == 4:
        print(' =======\n| o   o |\n|       |\n| o   o |\n =======')
    elif i == 5:
        print(' =======\n| o   o |\n|   o   |\n| o   o |\n =======')
    else:
        print(' =======\n| o   o |\n| o   o |\n| o   o |\n =======')


# In[ ]:


x = 'x'
while x == 'x':
    dice()
    x = input('press x to roll : ')

