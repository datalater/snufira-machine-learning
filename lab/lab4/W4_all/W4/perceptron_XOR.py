#################
### Perceptron for XOR function
#################
import tensorflow as tf
import math


### define graph
x = tf.placeholder(tf.float32, shape=(None, 2), name = 'x-input')
y = tf.placeholder(tf.float32, shape=(None, 1), name = 'y-input')

v_weight1 = tf.Variable(
  tf.random_uniform(shape=(2, 2), minval=-1, maxval=1), 
  dtype=tf.float32, 
  name = "W1")
v_bias1 = tf.Variable(
  tf.zeros(shape=(1)), 
  dtype=tf.float32, 
  name = "B1")

v_weight2 = tf.Variable(
  tf.random_uniform(shape=(2, 1), minval=-1, maxval=1), 
  dtype=tf.float32, 
  name = "W2")
v_bias2 = tf.Variable(
  tf.zeros(shape=(1)), 
  dtype=tf.float32, 
  name = "B2")

a_h = tf.sigmoid( tf.matmul(x, v_weight1) + v_bias1 )
y_h = tf.sigmoid( tf.matmul(a_h, v_weight2) + v_bias2 )


### define loss function
# # prevent nan loss
# epsilon = 1e-10 
# loss = tf.reduce_mean( 
#   -1 * y * tf.log(y_h + epsilon) - 
#   (1 - y) * tf.log(1 - y_h + epsilon) )

loss = tf.reduce_mean( 
  -1 * y * tf.log(y_h) - 
  (1 - y) * tf.log(1 - y_h) )

### define optimization function
learning_rate = 0.1
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)



### define input data
DATA = {
  'X': [[0,0],[0,1],[1,0],[1,1]],
  'Y': [[0],[1],[1],[0]]
}


### Starting sessions
with tf.Session() as sess:
  ## initialize variables
  init = tf.global_variables_initializer()
  sess.run(init)

  max_iter = 100000

  for i in range(max_iter):
    _, v_w1_val, v_b1_val, v_w2_val, v_b2_val, y_h_val, loss_val = sess.run(
      [train_step, v_weight1, v_bias1, v_weight2, v_bias2, y_h, loss], 
      feed_dict={x: DATA['X'], y: DATA['Y']})

    if i % 1000 == 0:
      print('Epoch ', i)
      print('Y_prediction ', y_h_val)
      print('True', DATA['Y'])
      print('Loss', loss_val)
      print('Weight1', v_w1_val)
      print('Bias1', v_b1_val)
      print('Weight2', v_w2_val)
      print('Bias2', v_b2_val)

    if math.isnan(loss_val):
      print('LOSS is NAN!')
      break