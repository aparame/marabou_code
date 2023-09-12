'''
Tensorflow Example
====================

Top contributors (to current version):
  - Christopher Lazarus
  - Kyle Julian
  
This file is part of the Marabou project.
Copyright (c) 2017-2019 by the authors listed in the file AUTHORS
in the top-level source directory) and their institutional affiliations.
All rights reserved. See the file COPYING in the top-level source
directory for licensing information.
'''
import sys

sys.path.append("/home/aparame/NeuroSymbolic/Marabou")
from maraboupy import Marabou
import numpy as np
import tensorflow as tf
print(tf.__version__)



#%%
# This network has inputs x0, x1, and was trained to create outputs that approximate
# y0 = abs(x0) + abs(x1), y1 = x0^2 + x1^2
filename ="NSV_2.pb"
network = Marabou.read_tf(filename)

# %%
# Or, you can specify the operation names of the input and output operations.
# The default chooses the placeholder operations as input and the last operation as output
#inputNames = ['Placeholder']
#outputName = 'y_out'
#network = Marabou.read_tf(filename = filename, inputNames = inputNames, outputNames = outputName)

# %%
# Get the input and output variable numbers; [0] since first dimension is batch size
inputVars = network.inputVars[0][0]
outputVars = network.outputVars[0][0]


# %%
# #Set input bounds on both input variable
delta = 0.03
network.setLowerBound(inputVars[0],0.0)	# 0 < x < pi/2
network.setUpperBound(inputVars[0], np.pi/2)	

# Set output bounds on the output variable
network.setLowerBound(outputVars[0], -1.0)	# -1.0 < y1 < 0.0
network.setUpperBound(outputVars[0], 0.0)

## Call to C++ Marabou solver
exitCode, vals, stats = network.solve("marabou.log")
print(delta)
#%%
# op = network.evaluateWithMarabou([np.pi/2])

#%% Check actual outputs vs expected outputs
#inputs = np.array([np.pi/2, np.pi])
#output_expected = np.array([ 0.0, -1.0])


#output_Marabou = network.evaluateWithMarabou([inputs[0]])
#print(output_Marabou)

#for i,input in enumerate(inputs):
    #output_Marabou = network.evaluateWithMarabou([input])
    #print(output_Marabou)
    #assert max(abs(output_Marabou-output_expected[i])) < 1e-2

