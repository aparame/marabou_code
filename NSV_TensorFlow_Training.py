import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2
from keras import regularizers
import os, argparse

##Numerical ML

model = keras.Sequential([
    keras.layers.Dense(units=1,activation = "linear",input_shape=[1]),
    keras.layers.Dense(units = 64, activation = "relu",kernel_regularizer=regularizers.l2(0.001)),
    keras.layers.Dense(units = 64, activation = "relu",kernel_regularizer=regularizers.l2(0.001)),
    keras.layers.Dense(units = 64, activation = "relu",kernel_regularizer=regularizers.l2(0.001)),
    keras.layers.Dense(units = 1, activation = "linear")
    ])
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01), loss= 'mean_squared_error')

xs = np.linspace(-np.pi,np.pi,num=10001,dtype=float)
y = np.cos(xs)
#print(y)
model.fit(xs,y,epochs=300,verbose=1)
#%%
print(model.predict([np.pi/2]))


#%% Save model to SavedModel format
tf.saved_model.save(model, "./models/simple_model")

 # load the saved_model using low-level API
model_path = "models/simple_model"
m = tf.saved_model.load(model_path)

from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2

tfm = tf.function(lambda x: m(x))  # full model                                                  
tfm = tfm.get_concrete_function(tf.TensorSpec(m.signatures['serving_default'].inputs[0].shape.as_list(), m.signatures['serving_default'].inputs[0].dtype.name))   
frozen_func = convert_variables_to_constants_v2(tfm)                                                                                                                              
tf.io.write_graph(graph_or_graph_def=frozen_func.graph, logdir="./", name="NSV_2.pb", as_text=False)
