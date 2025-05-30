def solution(polynomial):
    answer = ""
    a,b = 0,0
    for i in polynomial.replace(" + "," ").split(" "):
        if "x" in i:
            if i == "x":
                a += 1
            else:
                a += int(i[:len(i)-1])
        else:
            b += int(i)
    if a and b :
        return ("x" if a == 1 else str(a) + "x") + " + " + str(b)
    elif a:
        return ("x" if a == 1 else str(a) + "x")
    else:
        return str(b)