def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    if len(signature) == n:
        return signature
    signature.append(signature[-1] + signature[-2] + signature[-3])
    return tribonacci(signature,n)
