def solution(s):
    # TODO: Implement me!
    if len(s) % 2 == 1:
        return False
    else:
        for i in range(0, len(s)//2):
            mir = len(s)-i-1
            if s[i] == ")" or s[i] == "}" or s[i] == "]":
                return False
            elif s[i] == "(":
                if s[mir] != ")":
                    return False
            elif s[i] == "{":
                if s[mir] != "}":
                    return False
            elif s[i] == "[":
                if s[mir] != "]":
                    return False
    
    return True

ans = solution("}{")

print(ans)