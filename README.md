
# Maraboupy examples

This folder contains a collection of example files showing how Maraboupy can be used.
These files can be run after Marabou and Maraboupy have been built. Make sure that
the Marabou root directory has been added to PYTHONPATH. These examples use networks
stored in the root directory's resources folder.

## Adding new example files
New example files can be added to this folder, and they will automatically be included
in the documentation created in the maraboupy/docs folder. To make the derived documentation
look correct, follow these basic rules:
1. A comment block should be at the top and contain the title followed by a line of "="
2. The remaining lines of the comment block can give information or documentation about the file
3. Begin comment lines with a preceding "# %%" to denote the beginning of a text block
4. Subsections can be created in a comment line by writing the subsection title followed 
by a line of "-" characters
5. Append a number prefix to the name of the file to indicate order of files used in documentation

Following these steps will produce documentation with alternating code and text blocks. See
one of the existing files as an example.
=======
# Neural Verification of Deep Convolution Neural Networks

## Features
- Allows formal verification of Deep CNN's using neural network verifiers such as Marabou

 
### *Current Features*
- Currently the ```NSV_training.py``` file enables the user to train and save simple neural network locally on their device.
- The ```NSV_Tensorflow.py``` file allows the user to use Marabou to set bounds on the input and output variables of the network trained and saved using the ```NSV_Training.py``` file.

## How to connect to Palmetto Cluster and Run

1) Connect to ```Palmetto OnDemand``` supercomputer cluster using Clemson credentials and start the Palmetto Desktop version.  In the Desktop version, git clone the Marabou folder from [Marabou github page](https://github.com/NeuralNetworkVerification/Marabou) and follow the steps to install Marabou onto your computer. Be sure that you have the ```anaconda``` and ```gcc``` modules loaded onto your remote computer. (THe installation process can take some time)

2) Once cloned and installed, head into ```Marabou/maraboupy/examples```.

3) Delete all contents of that folder, and git clone this repository into that folder. We do this as some of the examples from maraboupy do not run natively as expected, hence I have made those changes accordingly.

4) Try running the ```1_TensorflowExample.py``` and if it successfull runs, then everything has been succesfully installed.
