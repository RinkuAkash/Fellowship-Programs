import AnagramDetection_BL as AD

if __name__=="__main__":
    s1=str(input())
    s2=str(input())
    res=AD.FindAnagram(s1,s2)
    if res==True:
        print("The two strings are Anagrams")
    else:
        print("Not Anagrams")
