# Double Pendulum Neural ODE Solver
## By Marc-Andre Gaudet, Han Fang, Hasnain Syed

This project attempts to model the motion (angles and angular velocities) of a double pendulum using a neural ODE. To evaluate the performance of the neural ODE, it was trained and tested on a dataset gathered from _, and compared with the result of using established theoretical differential equations for double pendulum motion.

This repository contains two Jupyter notebooks (for easier code readability and usability) and several .pth files where neural network weights are stored. 
The notebook titled "Double_Pendulum_Neural_ODE" uses a neural ODE to attempt to model the motion of a double pendulum, and the model weights from the .pth files are saved from and used there.
The notebook titled _ uses the theoretical system of differential equations to do the same.

To clone this repository, use the following terminal command:
```git clone https://github.com/marzg7/doublependulum```

The following are descriptions of the Jupyter notebook files.

## Double_Pendulum_Neural_ODE.ipynb

To install the required packages to run this notebook, run the first code block.

All other code blocks have section headings.

Run code sections 1 and then 2 to import the needed Python libraries and load the data from the double pendulum datasets, respectively.

Next, to quickly see our results from training the neural ODE, run code sections 5, then 7.1.1. 
Inside 7.1.1., the strings within the variables ```train_names``` and ```test_name``` at the top of the code cell can be swapped around to produce the neural ODE results when trained on the trials specified in ```train_names``` and tested on ```test_name```. In addition, ```method_name```, specifying the numerical method used in the neural ODE, can be chosen from any one of "euler", "midpoint", "rk4", "dopri5", and "bosh3". The resulting graphs show two pairs of graphs, each comparing the neural ODE to one of the trials used in training and to the trial used in testing.

Otherwise, to train the model, run code sections 1 through 6, then either run section 7.1 to train the neural ODE with an individual numerical method, or run 7.2 to train the neural ODE on multiple (previously specified) numerical methods and compare their performances. In both code sections 7.1 and 7.2, the trials to test can train can be specified in the same way as in section 7.1.1 (at the top of the code cell), and in section 7.1, the numerical method can also be specified.