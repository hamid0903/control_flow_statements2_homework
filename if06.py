def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1=n%10
    n//=10
    n2=n%10
    n//=10
    n3=n%10
    n//=10
    n4=n%10
    n5=n//10
    mx=n1
    inx=1
    if n2>mx:
        mx=n2
        inx=2
    if n3>mx:
        mx=n3
        inx=3
    if n4>mx:
        mx=n4
        inx=4
    if n5>mx:
        mx=n5
        inx=5

    return inx
x=main(98765)
print(x)