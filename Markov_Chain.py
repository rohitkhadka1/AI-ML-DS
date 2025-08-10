# define the state transition probabilities for a Markov chain
# where states A, B, and C have the following probabilities
Prob_A = 0.5 
Prob_B = 0.2
Prob_C = 0.3 
Prob_AB = 0.2
Prob_AC = 0.3
Prob_BA = 0.7
Prob_BC = 0.1
Prob_CA = 0.1   
Prob_CB = 0.6

# define the transition matrix
transition_matrix = [[0.5, 0.2, 0.3],  # from A to A, B, C
                     [0.7, 0.0, 0.1],  # from B to A, B, C
                     [0.1, 0.6, 0.3]]  # from  C to A, B, C
# define the initial state distribution
initial_state = [1.0, 0.0, 0.0]
# function to perform one step of the Markov chain
def markov_step(current_state, transition_matrix):
    next_state = [0.0,0.0,0.0]
    for i in range(len(current_state)):
        for j in range(len(transition_matrix[i])):
            next_state[j] += current_state[i] * transition_matrix[i][j]
    return next_state
# function to run the Markov chain for a given number of steps
def run_markov_chain(initial_state, transition_matrix, steps):
    current_state = initial_state
    for _ in range(steps):
        current_state = markov_step(current_state, transition_matrix)
    return current_state
# Example usage
#Steps = 10
steps = 10  # number of steps to run the Markov chain
final_state = run_markov_chain(initial_state, transition_matrix, steps)
print("Final state distribution after", steps, "steps:", final_state)

#Step = 10000
steps = 100000  # number of steps to run the Markov chain
final_state = run_markov_chain(initial_state, transition_matrix, steps)
print("Final state distribution after", steps, "steps:", final_state)

#Step = 10000000
steps = 10000000  # number of steps to run the Markov chain
final_state = run_markov_chain(initial_state, transition_matrix, steps)
print("Final state distribution after", steps, "steps:", final_state)

# Final state distribution after 10 steps: [0.29256299519999995, 0.16379668479999998, 0.16098728959999997]
# Final state distribution after 100000 steps: [5.4e-323, 3e-323, 3e-323]
# Final state distribution after 10000000 steps: [5.4e-323, 3e-323, 3e-323]
# Note: The final state distribution converges to a steady state as the number of steps increases.
# The results show that the Markov chain reaches a steady state distribution after a large number of steps.