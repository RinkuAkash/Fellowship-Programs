import sys

def singleInt():
    return int(input())

def singleString():
    return str(input())

def singleFloat():
    return float(input())

def multiInt():
    return list(map(int,input().split()))

def multiString():
    return list(map(str,input().split()))

def multiFloat():
    return list(map(float,input().split()))

def commandLine():
    return sys.argv
