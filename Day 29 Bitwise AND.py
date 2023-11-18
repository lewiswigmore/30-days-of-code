import os

# Complete the 'bitwiseAnd' function below.
def bitwiseAnd(N, K):
    max_and = 0
    for A in range(1, N):
        for B in range(A+1, N+1):
            current_and = A & B
            if current_and > max_and and current_and < K:
                max_and = current_and
                # Early stopping if found the highest possible result.
                if max_and == K - 1:
                    return max_and
    return max_and

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        N = int(first_multiple_input[0])
        K = int(first_multiple_input[1])

        res = bitwiseAnd(N, K)

        fptr.write(str(res) + '\n')

    fptr.close()
