import board;
import tensorFlow as tf
class TwentyFourtyEightEnv():
	def __init__(self, num_states, num_actions, batch_size):
        	self._num_states = num_states
        	self._num_actions = num_actions
        	self._batch_size = batch_size
        	# define the placeholders
        	self._states = None
        	self._actions = None
        	# the output operations
        	self._logits = None
        	self._optimizer = None
        	self._var_init = None
        	# now setup the model
        	self._define_model()

	def _define_model(self):
        	self._states = tf.placeholder(shape=[None, self._num_states], dtype=tf.float32)
        	self._q_s_a = tf.placeholder(shape=[None, self._num_actions], dtype=tf.float32)
        	# create a couple of fully connected hidden layers
        	fc1 = tf.layers.dense(self._states, 50, activation=tf.nn.relu)
        	fc2 = tf.layers.dense(fc1, 50, activation=tf.nn.relu)
        	self._logits = tf.layers.dense(fc2, self._num_actions)
        	loss = tf.losses.mean_squared_error(self._q_s_a, self._logits)
        	self._optimizer = tf.train.AdamOptimizer().minimize(loss)
        	self._var_init = tf.global_variables_initializer()i


