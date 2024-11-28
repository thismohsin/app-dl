import numpy as np

def softmax(x, axis=None):
    if axis is None:
        x = x.flatten()
        axis = 0
    
    max_x = np.max(x, axis=axis, keepdims=True)
    exp_x = np.exp(x - max_x)
    
    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)

# Tokens with their semantic meanings
tokens = ["the", "sky", "is", "blue"]
token_meanings = [
    "article referring to a specific noun",
    "celestial dome above earth",
    "state of being verb",
    "color representing clear atmosphere"
]

# Enhanced embedding to capture more semantic information
embeddings = np.array([
    [0.1, 0.2, 0.3, 0.4],   # "the"
    [0.4, 0.5, 0.6, 0.7],   # "sky"
    [0.7, 0.8, 0.9, 1.0],   # "is"
    [1.0, 1.1, 1.2, 1.3]    # "blue"
])

# Weight matrices with more interesting transformations
W_Q = np.array([
    [1.0, 0.2, 0.3, 0.1],
    [0.2, 1.0, 0.1, 0.3],
    [0.3, 0.1, 1.0, 0.2],
    [0.1, 0.3, 0.2, 1.0]
])
W_K = np.array([
    [1.1, 0.1, 0.2, 0.3],
    [0.2, 1.1, 0.3, 0.1],
    [0.3, 0.2, 1.1, 0.1],
    [0.1, 0.3, 0.1, 1.1]
])
W_V = np.array([
    [1.2, 0.1, 0.2, 0.3],
    [0.2, 1.2, 0.3, 0.1],
    [0.3, 0.2, 1.2, 0.1],
    [0.1, 0.3, 0.1, 1.2]
])

# Compute Q, K, V matrices
Q = np.dot(embeddings, W_Q)  # Query matrix
K = np.dot(embeddings, W_K)  # Key matrix
V = np.dot(embeddings, W_V)  # Value matrix

# Compute Attention Scores
attention_scores = np.dot(Q, K.T)
print("Attention Scores (Raw):")
for i, token_i in enumerate(tokens):
    print(f"\n{token_i} attention to other tokens:")
    for j, token_j in enumerate(tokens):
        print(f"  {token_j}: {attention_scores[i][j]:.4f}")

# Apply Softmax to normalize attention scores
attention_probs = softmax(attention_scores, axis=1)
print("\nAttention Probabilities:")
for i, token_i in enumerate(tokens):
    print(f"\n{token_i} attention distribution:")
    for j, token_j in enumerate(tokens):
        print(f"  {token_j}: {attention_probs[i][j]:.4f}")

# Compute Weighted Values
weighted_values = np.dot(attention_probs, V)
print("\nWeighted Values:")
for i, token_i in enumerate(tokens):
    print(f"\n{token_i} weighted representation:")
    print(f"  Raw values: {weighted_values[i]}")
    print(f"  Meaning context: How {token_i} gets influenced by other tokens")

# Optional: Visualize relationship
print("\nSemantic Relationship Interpretation:")
for i, token_i in enumerate(tokens):
    print(f"\n{token_i} ({token_meanings[i]}):")
    sorted_influences = sorted(enumerate(attention_probs[i]), key=lambda x: x[1], reverse=True)
    for j, prob in sorted_influences:
        if i != j and prob > 0.01:
            print(f"  Strongly influenced by {tokens[j]} ({token_meanings[j]}): {prob:.4f}")
