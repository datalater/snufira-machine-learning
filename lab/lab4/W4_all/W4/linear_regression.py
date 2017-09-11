#################
### Perceptron for linear regression
#################
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import tensorflow as tf
import math

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# diabetes has two attributes: data, target
print(diabetes.data.shape)
print(diabetes.target.shape)

# diabetes consists of 442 samples 
#with 10 attributes and 1 real target value.

# Use only one feature
diabetes_X = diabetes.data[:, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# define graph
x = tf.placeholder(tf.float32, shape=None, name = 'x-input')
y = tf.placeholder(tf.float32, shape=None, name = 'y-input')

v_weight = tf.Variable(
  0,
  dtype=tf.float32, 
  name = "W")
v_bias = tf.Variable(
  0,
  dtype=tf.float32, 
  name = "w0")

y_h = tf.add( tf.multiply(x, v_weight), v_bias )

n_samples = tf.cast(tf.size(x), tf.float32)
loss = tf.reduce_sum(tf.pow(y_h-y, 2))/(n_samples * 2)

# define optimization function
learning_rate = 0.1
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)



### Starting sessions
with tf.Session() as sess:
  ## initialize variables
  init = tf.global_variables_initializer()
  sess.run(init)

  max_iter = 10000

  for i in range(max_iter):
    _, v_w_val, v_b_val, y_h_val, loss_val = sess.run(
      [train_step, v_weight, v_bias, y_h, loss], 
      feed_dict={x: diabetes_X_train, y: diabetes_y_train})
    
    if i % 1000 == 0:
      print('Epoch ', i)
      print('Loss', loss_val)

    if math.isnan(loss_val):
      print('LOSS is NAN!')
      break

  # The coefficients
  print('Coefficients: \n', v_w_val)
  # The mean squared error
  print("Mean squared error: %.2f" % loss_val )


  # Plot outputs
  plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
  test_pred = sess.run(y_h, 
    feed_dict={x: diabetes_X_test, y: []})
  plt.plot(diabetes_X_test, test_pred, 
          color='blue', linewidth=3)

  plt.xticks(())
  plt.yticks(())

  plt.show()