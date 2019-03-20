import tensorflow as tf
import board as b


def NeuralNet():
     
        
        inputs  = tf.placeholder(tf.float32, shape=[None, 16],name="Input" )
        hiddenweights = []
        hiddenweights.append(tf.Variable(initial_value=tf.random_normal(shape=[16, 20],stddev = 0.4), dtype = 'float',  name="Hidden"))
        for i in range(199):
        	HiddenLayer(hiddenweights, i + 1)
        
        outputweights = tf.Variable(initial_value=tf.random_normal(shape=[20, 4],stddev = 0.4),dtype = 'float', name="Output")
        hiddenLayers = tf.matmul(inputs, hiddenweights[0])
        for i in range(199):
        	hiddenLayers = tf.matmul(hiddenLayers, hiddenweights[i+1])

        output=tf.matmul(hiddenLayers, outputweights)
        

def HiddenLayer(hiddenweights, i):
	 callMe = "Hidden" + str(i)
	 hiddenweights.append(tf.Variable(initial_value=tf.random_normal(shape=[20, 20],stddev = 0.4), dtype = 'float',  name=callMe))

def train(board, W):
	discountRate = .7
	qMax = discountRate*b.qMax(board) + b.reward(board)
	learningRate = .00001

	#l is the distance between maxQ and expected Q
	#W is all the weigths
	#I in theory want the diffenerce in rates to be minized due to convergence
	gradW = tf.gradients(l,W)

NeuralNet()
print("ran")


