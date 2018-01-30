# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division

import tensorflow as tf

flags = tf.app.flags
FLAGS = flags.FLAGS

_float_feature = lambda v: tf.train.Feature(float_list=tf.train.FloatList(value=v))
_int_feature = lambda v: tf.train.Feature(int64_list=tf.train.Int64List(value=v))


# libsvm to tfrecord

def main(argv):
    input = "  " #file path
    output = "  " #file path
    writer = tf.python_io.TFRecordWriter(output)
    f = open(input)
    for line in f:
        l = line.rstrip().split()
        label = int(l[0])
        indexes = []
        values = []
        for item in l[1:]:
            index, value = item.split(':')
            indexes.append(int(index))
            values.append(float(value))

        example = tf.train.Example(features=tf.train.Feature(features={
                'l': _int_feature([label]),
                'i': _int_feature(indexes),
                'v': _float_feature(values)}))

        writer.write(example.SerializeToString())

    writer.close()

if __name__ == '__main__':
    tf.app.run()


