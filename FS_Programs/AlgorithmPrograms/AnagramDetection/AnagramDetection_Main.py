import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input
import AnagramDetection_BL as AD

if __name__=="__main__":
    s1=Input.singleString()
    s2=Input.singleString()
    res=AD.FindAnagram(s1,s2)
    if res==True:
        print("The two strings are Anagrams")
    else:
        print("Not Anagrams")
