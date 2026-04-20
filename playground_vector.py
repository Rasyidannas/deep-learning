def elementwise_by(operator, vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))

    result = 0
    
    for i in range(len(vec_a)):
        if operator == "MULTIPLICATION":
            result += vec_a[i] * vec_b[i]
        elif operator == "ADDITION":
            result += vector_a[i] + vec_b[i]
        else:
            return "You need input operator"

    return result

vector_a = [1, 2, 3]
vector_b = [3, 2, 1]

vectors_multiplication = elementwise_by("", vector_a, vector_b)
print(vectors_multiplication)
