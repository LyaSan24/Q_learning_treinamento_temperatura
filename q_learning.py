import numpy as np

# Definindo hiperparâmetros do modelo
alpha = 0.1  # taxa de aprendizagem
gamma = 0.9  # fator de desconto
epsilon = 0.1  # probabilidade de escolha aleatória de ação
n_episodes = 5000  # número de episódios de treinamento

# Definindo o range de temperaturas e as ações possíveis
temp_range = 5.0
actions = [-1, 0, 1]

# Inicializando a Q-table
Q = np.zeros((int(temp_range * 10), len(actions)))


# Definindo a função de discretização da temperatura
def discretize_temp(temp):
    return int((temp - 37) * 10)


# Definindo a função de escolha da ação
def choose_action(state):
    if np.random.uniform() < epsilon:
        action = np.random.choice(actions)
    else:
        max_actions = np.where(Q[state] == np.max(Q[state]))[0]
        action = actions[np.random.choice(max_actions)]
    return action


# Loop de treinamento
rewards = []
for episode in range(n_episodes):
    # Inicializando a temperatura e a recompensa acumulada
    temp = np.random.uniform(low=36, high=40)
    state = discretize_temp(temp)
    total_reward = 0

    for i in range(60):
        # Escolhendo a ação e atualizando a temperatura
        action = choose_action(state)
        temp = np.clip(temp + action, 36, 40)
        temp = max(temp, 36)
        temp = min(temp, 40)

        # Calculando a recompensa
        if temp >= 37 and temp <= 39:
            reward = 1
        else:
            reward = -1

        # Atualizando a Q-table
        next_state = discretize_temp(temp)
        Q[state, actions.index(action)] += alpha * (
                    reward + gamma * np.max(Q[next_state, :]) - Q[state, actions.index(action)])

        # Atualizando o estado e a recompensa acumulada
        state = next_state
        total_reward += reward

    # Armazenando a recompensa acumulada do episódio
    rewards.append(total_reward)

# Loop de teste
for i in range(10):
    # Inicializando a temperatura
    temp = np.random.uniform(low=36, high=40)
    state = discretize_temp(temp)

    for j in range(60):
        # Escolhendo a ação e atualizando a temperatura
        max_actions = np.where(Q[state] == np.max(Q[state]))[0]
        action = actions[np.random.choice(max_actions)]
        temp = np.clip(temp + action, 36, 40)
        temp = max(temp, 36)
        temp = min(temp, 40)

        # Imprimindo a temperatura e a ação escolhida
        print(f'Temperatura: {temp:.1f} - Ação: {action}')

        # Atualizando o estado
        state = discretize_temp(temp)
