def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    m=a
    if b<m:
        m=b
    if c<m:
        m=c
    return m
x=main(1,2,3)
print(x)