# Q_learning_treinamento_temperatura
Build a reinforcement learning model to automatically adjust the temperature to get it in the ideal range

This is an example implementation of the Q-Learning algorithm for a temperature control environment. The goal is to train an agent to choose actions that allow maintaining the temperature within the desired range of 37 to 39 degrees Celsius.

The code starts by defining the model's hyperparameters, including the learning rate, discount factor, probability of randomly choosing an action, and the number of training episodes. Then, the temperature range and possible actions are defined, which in this case are to decrease by one degree Celsius, maintain the temperature, or increase by one degree Celsius.

The Q-table is initialized as a matrix of zeros, with dimensions based on the temperature range and the number of possible actions. The discretize_temp function is used to discretize the temperature into an integer that can be used as an index in the Q-table.

The choose_action function chooses the action that the agent should take based on the epsilon-greedy policy, which explores a random action with probability epsilon and chooses the action with the highest Q-value with probability 1 - epsilon.

The training loop is executed n_episodes times, initializing the temperature randomly within the allowed range and updating the Q-table based on the actions taken and the rewards received. The reward is calculated as 1 if the temperature is within the desired range and -1 otherwise.

The testing loop is used to check if the agent has learned to control the temperature. The temperature is initialized randomly, and the agent chooses the appropriate action at each time step. The temperature readings and chosen actions are printed on the screen.