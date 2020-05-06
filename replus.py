def replus(a,b):
    Ans = 0
    tempa = 1/a
    #print(tempa)
    tempb=1/b
    #print(tempb)
    Ans = tempa+tempb
    #print(Ans)
    Ans = 1/Ans
    Ans = round(Ans,5)
    return Ans

def main():
    print(replus(20,35))

if __name__ == "__main__":
    main()
