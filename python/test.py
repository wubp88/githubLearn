# import tensorflow as tf
# from numpy.random import RandomState
#
#
# ## 1. 定义神经网络的相关参数和变量。
# batchsize= 8
# x = tf.placeholder(tf.float32, shape=(None,2),name="x-input")
# y_ = tf.placeholder(tf.float32, shape=(None,1),name="y-input")
# w1 = tf.Variable(tf.random_normal([2,1],stddev=1, seed=1))
# y =  tf.matmul(x, w1)
#
#
# ##2. 设置自定义的损失函数。
#
# loss_less = 10
# loss_more = 1
# loss = tf.reduce_sum(tf.where(tf.greater(y, y_), (y-y_)*loss_more, (y_ - y) * loss_less))
#
#
#
# rdm =  RandomState(1)
# X = rdm.rand(128,2)
# Y = [[x1+x2+(rdm.rand()/10.0-0.05)] for (x1, x2) in X]
#
#
# with tf.Sesssion() as sess:
#     init_op = tf.global_variables_initializer()
#     sess.run(init_op)











