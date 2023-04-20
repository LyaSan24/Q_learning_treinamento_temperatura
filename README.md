# Q_learning_treinamento_temperatura
Construir modelo de aprendizado de reforço para ajustar a temperatura automaticamente para obtê-lo na faixa ideal

Este é um exemplo de implementação do algoritmo Q-Learning para um ambiente de controle de temperatura. O objetivo é treinar um agente para escolher ações que permitam manter a temperatura dentro do intervalo desejado de 37 a 39 graus Celsius.

O código começa definindo os hiperparâmetros do modelo, incluindo a taxa de aprendizagem, o fator de desconto, a probabilidade de escolha aleatória de ação e o número de episódios de treinamento. Em seguida, são definidos o range de temperaturas e as ações possíveis, que neste caso são diminuir em um grau Celsius, manter a temperatura ou aumentar em um grau Celsius.

A Q-table é inicializada como uma matriz de zeros, com dimensões baseadas no range de temperatura e no número de ações possíveis. A função discretize_temp é usada para discretizar a temperatura em um número inteiro que pode ser usado como um índice na Q-table.

A função choose_action escolhe a ação que o agente deve tomar com base na política epsilon-greedy, que explora uma ação aleatória com probabilidade epsilon e escolhe a ação com maior valor Q com probabilidade 1 - epsilon.

O loop de treinamento é executado n_episodes vezes, inicializando a temperatura aleatoriamente dentro do intervalo permitido e atualizando a Q-table com base nas ações tomadas e nas recompensas recebidas. A recompensa é calculada como 1 se a temperatura estiver dentro do intervalo desejado e -1 caso contrário.

O loop de teste é usado para verificar se o agente aprendeu a controlar a temperatura. A temperatura é inicializada aleatoriamente e o agente escolhe a ação apropriada a cada etapa de tempo. As leituras de temperatura e as ações escolhidas são impressas na tela.