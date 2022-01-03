def main(n):
    """
    Find the largest digit of the five-digit number.
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
    print(n1,n2,n3,n4,n5)
    mx=n1
    if n2>mx:
        mx=n2
    elif n3>mx:
        mx=n3
    elif n4>mx:
        mx=n4
    elif n5>mx:
        mx=n5
    return mx
x=main(12345)
print(x)