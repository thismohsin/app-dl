- https://poloclub.github.io/transformer-explainer/
- https://bbycroft.net/llm

```
Tokens: ['the', 'sky', 'is', 'blue']

Embeddings Matrix:
 [[0.1 0.2 0.3 0.4]
 [0.4 0.5 0.6 0.7]
 [0.7 0.8 0.9 1. ]
 [1.  1.1 1.2 1.3]]

Query (Q) Matrix:
 [[0.27 0.37 0.43 0.53]
 [0.75 0.85 0.91 1.01]
 [1.23 1.33 1.39 1.49]
 [1.71 1.81 1.87 1.97]]

Key (K) Matrix:
 [[0.28 0.41 0.45 0.52]
 [0.79 0.92 0.96 1.  ]
 [1.3  1.43 1.47 1.48]
 [1.81 1.94 1.98 1.96]]

Value (V) Matrix:
 [[0.29 0.43 0.48 0.56]
 [0.83 0.97 1.02 1.07]
 [1.37 1.51 1.56 1.58]
 [1.91 2.05 2.1  2.09]]

Attention Scores (Before Softmax):
 [[ 0.6964  1.4965  2.2966  3.0967]
 [ 1.4932  3.2581  5.023   6.7879]
 [ 2.29    5.0197  7.7494 10.4791]
 [ 3.0868  6.7813 10.4758 14.1703]]

Attention Scores (Raw):

'the' attention to other tokens:
  the: 0.6964
  sky: 1.4965
  is: 2.2966
  blue: 3.0967

'sky' attention to other tokens:
  the: 1.4932
  sky: 3.2581
  is: 5.0230
  blue: 6.7879

'is' attention to other tokens:
  the: 2.2900
  sky: 5.0197
  is: 7.7494
  blue: 10.4791

'blue' attention to other tokens:
  the: 3.0868
  sky: 6.7813
  is: 10.4758
  blue: 14.1703

Attention Scores (After Softmax):
 [[5.20663292e-02 1.15887335e-01 2.57937799e-01 5.74108537e-01]
 [4.16257407e-03 2.43135461e-02 1.42015137e-01 8.29508743e-01]
 [2.59553910e-04 3.97851704e-03 6.09838544e-02 9.34778075e-01]
 [1.49818105e-05 6.02650143e-04 2.42418761e-02 9.75140492e-01]]

Attention Probabilities:

'the' attention distribution:
  the: 0.0521
  sky: 0.1159
  is: 0.2579
  blue: 0.5741

'sky' attention distribution:
  the: 0.0042
  sky: 0.0243
  is: 0.1420
  blue: 0.8295

'is' attention distribution:
  the: 0.0003
  sky: 0.0040
  is: 0.0610
  blue: 0.9348

'blue' attention distribution:
  the: 0.0000
  sky: 0.0006
  is: 0.0242
  blue: 0.9751

Weighted Values:
 [[1.56120781 1.70120781 1.75120781 1.76058516]
 [1.80030983 1.94030983 1.99030983 1.98640372]
 [1.87235144 2.01235144 2.06235144 2.05444303]
 [1.89623425 2.03623425 2.08623425 2.07699902]]

Weighted Values:

'the' weighted representation:
  Raw values: [1.56120781 1.70120781 1.75120781 1.76058516]
  Meaning context: How the gets influenced by other tokens

'sky' weighted representation:
  Raw values: [1.80030983 1.94030983 1.99030983 1.98640372]
  Meaning context: How sky gets influenced by other tokens

'is' weighted representation:
  Raw values: [1.87235144 2.01235144 2.06235144 2.05444303]
  Meaning context: How is gets influenced by other tokens

'blue' weighted representation:
  Raw values: [1.89623425 2.03623425 2.08623425 2.07699902]
  Meaning context: How blue gets influenced by other tokens

Semantic Relationship Interpretation:

'the' (article referring to a specific noun):
Attn sorted influence: [(3, np.float64(0.5741085369204841)), (2, np.float64(0.2579377991156912)), (1, np.float64(0.11588733477039649)), (0, np.float64(0.05206632919342827))]
  Strongly influenced by blue (color representing clear atmosphere): 0.5741
  Strongly influenced by is (state of being verb): 0.2579
  Strongly influenced by sky (celestial dome above earth): 0.1159

'sky' (celestial dome above earth):
Attn sorted influence: [(3, np.float64(0.8295087429201997)), (2, np.float64(0.1420151368653065)), (1, np.float64(0.024313546145241723)), (0, np.float64(0.0041625740692520004))]
  Strongly influenced by blue (color representing clear atmosphere): 0.8295
  Strongly influenced by is (state of being verb): 0.1420

'is' (state of being verb):
Attn sorted influence: [(3, np.float64(0.9347780746105904)), (2, np.float64(0.06098385443577424)), (1, np.float64(0.003978517043623401)), (0, np.float64(0.0002595539100119022))]
  Strongly influenced by blue (color representing clear atmosphere): 0.9348

'blue' (color representing clear atmosphere):
Attn sorted influence: [(3, np.float64(0.9751404919502488)), (2, np.float64(0.024241876096470095)), (1, np.float64(0.0006026501427515234)), (0, np.float64(1.4981810529561968e-05))]
  Strongly influenced by is (state of being verb): 0.0242
(venv) I509335@C02FLET7MD6M dl-fundamentals % 
```
