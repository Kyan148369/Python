
# Pseudocode will prolly help to transfer it in code
# basically u1 = v1
# u2 = v2 - <v2,u1>/u1^2 * u1(make dot product function for this probably)
# u3 = v3 - <v3,u1>/u1^2* u1 - <v3,u2>/u^2
# taken test matrix will add input matrix soon


def gram_schmidt(matrix):
    Gram_schmidt_matrix = []
    # this loop iterates through each indiviual vector
    for v in matrix:
        w = v[:]  # Create a copy of the current vector
        # this loop basically makes that vector orthogonal to the ones present in the GSP matrix
        for b in Gram_schmidt_matrix:
            proj = 0  # initialize projection
            for i in range(len(v)):
                proj += v[i] * b[i]  # Projection of v onto b
            proj /= sum(b[i] * b[i] for i in range(len(b)))

            for i in range(len(v)):
                w[i] -= proj * b[i]  # Subtract the projection of v onto b from v
        # Calculate the norm of the vector
        norm = sum(i ** 2 for i in w) ** 0.5
        # computer arithmetic isnt perfect so due to that floating point errors can add up
        # leading to us getting another vector which is in fact a zero vector
        if norm > 1e-10:
            for i in range(len(w)):
                w[i] /= norm  # Normalize the vector
            # Append the normalized vector to the Gram_schmidt_matrix
            Gram_schmidt_matrix.append(w)
        # appending zero vector to the remaining rows which werent linearly independent
        else:
            for i in range(len(w)):
                w[i] = 0
            Gram_schmidt_matrix.append(w)

    return Gram_schmidt_matrix


matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
orthonormal_basis = gram_schmidt(matrix)
print(orthonormal_basis)
