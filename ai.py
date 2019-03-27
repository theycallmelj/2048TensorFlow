import tensorflow as tf
import board as b
import numpy as np
from numpy import array
def NeuralNet():
     
        
 
        
        hiddenweights = []
        hiddenweights.append(tf.Variable(initial_value=tf.random_normal(shape=[16, 20],stddev = 0.4), dtype = 'float',  name="Hidden"))
        for i in range(199):
                HiddenLayer(hiddenweights, i + 1)
        
        outputweights = tf.Variable(initial_value=tf.random_normal(shape=[20, 4],stddev = 0.4),dtype = 'float', name="Output")
        hiddenLayers = tf.matmul(inputs, hiddenweights[0])
        for i in range(199):
                hiddenLayers = tf.matmul(hiddenLayers, hiddenweights[i+1])

        output=tf.matmul(hiddenLayers, outputweights)
        return output

def HiddenLayer(hiddenweights, i):
         callMe = "Hidden" + str(i)
         hiddenweights.append(tf.Variable(initial_value=tf.random_normal(shape=[20, 20],stddev = 0.4), dtype = 'float',  name=callMe))


def train(inputs, boar, nnin):
        boardSliced = []
        topTile = b.maxTile(boar)
        for x in range(4):
                for y in range(4):
                        boardSliced.append(boar[x][y]/topTile)        
        
        discountRate = .25
   
        qMax = b.add(b.qMultiply(b.qMax(boar), discountRate), b.reward(boar))
     
        
        
        learningRate = .001
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=learningRate)
        #left is  [1, 0, 0, 0]
        #right is [0, 1, 0, 0]
        #down is  [0, 0, 1, 0]
        #up is    [0, 0, 0, 1] 
        
        l = tf.square(qMax - nnin)
        #l is the distance between maxQ and expected Q
        
        #I in theory want the diffenerce in rates to be minized due to convergence
       
        train_op = optimizer.minimize(l)
        

        
        model = tf.global_variables_initializer()
        with tf.Session() as session:
                session.run(model, {inputs : array([boardSliced])})
                
inputs = tf.placeholder(tf.float32, shape=[None, 16],name="Input" )        
bor = b.newBoard()
b.addNewValue(bor)
nnin = NeuralNet()
train(inputs, bor, nnin)





print("ran")


