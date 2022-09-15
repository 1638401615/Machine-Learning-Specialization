import tensorflow as tf
import numpy as np

with tf.Session() as sess:
    with tf.device('/cpu:0'):
        a = tf.placeholder(tf.int32)
        b = tf.placeholder(tf.int32)
        add = tf.add(a, b)
        sum = sess.run(add, feed_dict={a: 3, b: 4})
        print(sum)