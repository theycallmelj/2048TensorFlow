import tensorflow as tf
import board as b
import numpy as np
from numpy import array
def NeuralNet(inpu):
     
        
 
        
        hiddenweights = []
        hiddenweights.append(tf.Variable(initial_value=tf.random_normal(shape=[16, 20],stddev = 0.4), dtype = 'float',  name="Hidden"))
        for i in range(199):
                HiddenLayer(hiddenweights, i + 1)
        
        outputweights = tf.Variable(initial_value=tf.random_normal(shape=[20, 4],stddev = 0.4),dtype = 'float', name="Output")
        hiddenLayers = tf.matmul(inpu, hiddenweights[0])
        for i in range(199):
               hiddenLayers = tf.sigmoid(tf.matmul(hiddenLayers, hiddenweights[i+1]))
        #have to add some bias neurons
        output=tf.sigmoid(tf.matmul(hiddenLayers, outputweights))
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
     
        y = tf.placeholder(tf.float32, shape=[None,4],name="y" )
    
        learningRate = .01
  
        #left is  [1, 0, 0, 0]
        #right is [0, 1, 0, 0]
        #down is  [0, 0, 1, 0]
        #up is    [0, 0, 0, 1] 
        
        l = tf.squared_difference(nnin*b.maxTile(boar), y)
        l = tf.reduce_mean(l)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=learningRate).minimize(l)
        #l is the distance between maxQ and expected Q
        
        #I in theory want the diffenerce in rates to be minized due to convergence
       
        #train_op = optimizer.minimize(l)
        

        
 
        with tf.Session() as session:
                tf.global_variables_initializer().run()
                print("Aloha")
                i = 0
                while( i < 5):
                        qMax = b.add(b.qMultiply(b.qMax(boar), discountRate), b.reward(boar))
                        p = session.run([l], feed_dict={inputs : [boardSliced], y : [qMax]})
                        b.doDown(boar)
                        i +=1
                        print(p)
                
inputs = tf.placeholder(tf.float32, shape=[None, 16],name="Input" )        
bor = b.newBoard()
b.addNewValue(bor)
nnin = NeuralNet(inputs)
train(inputs, bor, nnin)





print("ran")


