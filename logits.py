import numpy as np

# -----------------------------------------
# 1. Let's start with some logits (raw scores)
# -----------------------------------------
# Logits can be any real numbers. They are *unnormalized log-probabilities*.
logits = np.array([2.0, 1.0, 0.1])
print("Raw logits:", logits)


# -----------------------------------------
# 2. Implementing softmax by hand
# -----------------------------------------
def softmax(z):
    # Trick: subtract max for numerical stability (prevents overflow)
    z_stable = z - np.max(z)
    
    # Exponentiate each number
    exp_z = np.exp(z_stable)
    
    # Normalize to get probabilities that sum to 1
    return exp_z / np.sum(exp_z)

probs = softmax(logits)
print("Softmax Output (probabilities):", probs)
print("Sum of probabilities:", np.sum(probs))


# -----------------------------------------
# 3. What does softmax output REPRESENT?
# -----------------------------------------
# Answer: It is a PROBABILITY VECTOR.
# These probabilities parameterize a *categorical distribution*.
# They do NOT form a Gaussian/Bernoulli/etc., but they DEFINE the chance
# of selecting one discrete class.

# For example:
# probs = [0.659, 0.242, 0.098]
# This means:
#   Class 0 -> 65.9% chance
#   Class 1 -> 24.2% chance
#   Class 2 ->  9.8% chance


# -----------------------------------------
# 4. Let's SAMPLE from the categorical distribution
# -----------------------------------------
# This makes the idea more concrete.
sample = np.random.choice([0, 1, 2], p=probs)
print("Sampled class:", sample)


# -----------------------------------------
# 5. What is 'parameterizing the distribution'?
# -----------------------------------------
# The softmax probabilities *define* how sampling works.
# We are NOT creating a "softmax distribution".
# We are creating a *categorical distribution*.
#
# Example: If you repeatedly sample many times:
samples = [np.random.choice([0, 1, 2], p=probs) for _ in  range(10000)]
samples = np.array(samples)

# Empirical frequency of each class (should match softmax over many trials)
freqs = np.bincount(samples, minlength=3) / len(samples)
print("Empirical frequencies after sampling:", freqs)


# -----------------------------------------
# 6. Softmax, logits, and cross-entropy connection
# -----------------------------------------
# Neural networks output logits.
# Softmax converts logits → probability vector.
# Cross-entropy assumes these probabilities define a categorical distribution.
#
# Let's compute a simple cross-entropy loss manually:
true_class = 0  # Suppose the correct class is 0

cross_entropy_loss = -np.log(probs[true_class])
print("Cross-entropy loss for true class 0:", cross_entropy_loss)
