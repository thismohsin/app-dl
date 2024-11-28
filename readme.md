- https://poloclub.github.io/transformer-explainer/
- https://bbycroft.net/llm

```
Attention Scores (Raw):

the attention to other tokens:
  the: 0.6964
  sky: 1.4965
  is: 2.2966
  blue: 3.0967

sky attention to other tokens:
  the: 1.4932
  sky: 3.2581
  is: 5.0230
  blue: 6.7879

is attention to other tokens:
  the: 2.2900
  sky: 5.0197
  is: 7.7494
  blue: 10.4791

blue attention to other tokens:
  the: 3.0868
  sky: 6.7813
  is: 10.4758
  blue: 14.1703

Attention Probabilities:

the attention distribution:
  the: 0.0521
  sky: 0.1159
  is: 0.2579
  blue: 0.5741

sky attention distribution:
  the: 0.0042
  sky: 0.0243
  is: 0.1420
  blue: 0.8295

is attention distribution:
  the: 0.0003
  sky: 0.0040
  is: 0.0610
  blue: 0.9348

blue attention distribution:
  the: 0.0000
  sky: 0.0006
  is: 0.0242
  blue: 0.9751

Weighted Values:

the weighted representation:
  Raw values: [1.56120781 1.70120781 1.75120781 1.76058516]
  Meaning context: How the gets influenced by other tokens

sky weighted representation:
  Raw values: [1.80030983 1.94030983 1.99030983 1.98640372]
  Meaning context: How sky gets influenced by other tokens

is weighted representation:
  Raw values: [1.87235144 2.01235144 2.06235144 2.05444303]
  Meaning context: How is gets influenced by other tokens

blue weighted representation:
  Raw values: [1.89623425 2.03623425 2.08623425 2.07699902]
  Meaning context: How blue gets influenced by other tokens

Semantic Relationship Interpretation:

the (article referring to a specific noun):
  Strongly influenced by blue (color representing clear atmosphere): 0.5741
  Strongly influenced by is (state of being verb): 0.2579
  Strongly influenced by sky (celestial dome above earth): 0.1159

sky (celestial dome above earth):
  Strongly influenced by blue (color representing clear atmosphere): 0.8295
  Strongly influenced by is (state of being verb): 0.1420

is (state of being verb):
  Strongly influenced by blue (color representing clear atmosphere): 0.9348

blue (color representing clear atmosphere):
  Strongly influenced by is (state of being verb): 0.0242
```
