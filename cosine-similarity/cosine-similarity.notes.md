Cosine Similarity measures how similar two vectors are in terms of their **direction**, not their magnitude.

- `1` → Same direction
- `0` → Perpendicular vectors
- `-1` → Opposite directions
- We need three things:

1. Dot product of `a` and `b`.
2. Euclidean norm of `a`.
3. Euclidean norm of `b`.

Then divide the dot product by the product of both norms.

**Important edge case:** If either vector has zero norm, return `0.0` to avoid division by zero.

The NumPy function for calculating  the Euclidean norm (vector magnitude) is :-

`np.linalg.norm()`



zero vector handling 

norm_a * norm_b = 0

similarity =dot_product/(norm_a *times norm_b)