def solution(n_str):
    l = list(n_str)
    while l[0] == "0":
        l = l[1:]
    return "".join(l)