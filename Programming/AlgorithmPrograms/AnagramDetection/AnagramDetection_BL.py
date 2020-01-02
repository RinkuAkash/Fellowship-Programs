def FindAnagram(s1,s2):
    if len(s1)==len(s2):
        s1=set(s1)
        s2=set(s2)
        if s1==s2:
            return True
        else:
            return False
    else:
        return False
