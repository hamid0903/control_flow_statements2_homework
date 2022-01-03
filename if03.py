def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    m=a
    if b>m and b<c:
        m=b
    else:
        m=c
    return m
x=main(10,30,20)
print(x)