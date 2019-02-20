import tensorflow as tf



def NeuralNet():
	input  = tf.placeholder(tf.int32, shape=[None, 16],name="Input" )
	hiddenweights = []
	hiddenweights=(tf.Variable(initial_value=tf.random_normal(shape=[16, 20],stddev = 0.4),  name="Hidden"))
	for i in range(200):
		HiddenLayer(i)	
	outputwieghts = tf.Variable(initial_value=tf.random_normal(shape=[20, 4],stddev = 0.4),  name="Output")


def HiddenLayer(i):
	 callMe = "Hidden" + str(i)
	 hiddenweights=(tf.Variable(initial_value=tf.random_normal(shape=[20, 20],stddev = 0.4),  name=callMe))
def initNeuralNet(weights):
	net  = []
	for i in range(len(weights)):
		net.append(tf.Variable([weights[i]], tf.float32))
	init = tf.global_variables_initializer()

	sess = tf.Session()
	print(sess.run(init))

NeuralNet()	


