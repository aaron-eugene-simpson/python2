crap=[0,9,
      13,14,15,16,17,
      22,23,24,25,26,27,28,
      31,32,34,35,37,38,
      41,44,45,47,48,
      52,53,55,56,57, 
      64,65,66,72,76,
      81,84,85,86,88,
      90,99]
green='@ '
def isint(n): #returns True if a string is an integer, otherwise returns false 
    try:
        if float(n)-int(n)==0: 
            f=True
        else:
            f=False
    except ValueError:
        f=False
    return f
def halal(): #checks that the scaling factor is a natural number
    k=False
    while k==False:
        n=input('Enter scaling factor.')
        if n.isdigit() and int(n)>0:
            k=True
        else:
            print('Natural number please.')
        n=int(n)
    return n
def wack(n,l,h,p): #in combination with juno, makes the string for the printout
    grue=''
    for k in range(10):
        for i in range(n): 
            if 10*h+k in crap:
                grue=grue+green[p%2]
            else:
                grue=grue+green[(p+1)%2]
    grue=grue+'\n'
    return grue
def juno(n,l,p): #in combination with wack, makes the string for the printout
    blue=''
    for h in range(10):
        for i in range(n):
            blue=blue+wack(n,l,h,p)
    return blue
def woo(r,s,t): #Takes the input, checks it and prints error messages
    k=True
    while k==True:
        n=input(r)
        if isint(n):
            k=False
        else:
            print(s)
    n=int(n)%t
    return n
def rot(n,x): #rotates the string counterclockwise
    for j in range(n):
        for k in range(len(x)):
            x[k]=10*(9-x[k]%10)+int(x[k]/10)
def flip(n,x): #flips the string horizontally
    for j in range(n):
        for k in range(len(x)):
            x[k]=10*(int(x[k]/10))+9-x[k]%10
def main():
    b='Integer please!'
    n=woo('Enter rotation factor.',b,4 )
    m=woo('Enter flip factor.',b,2 )
    l=woo('Enter color reverse.', b,2)
    rot(n,crap)
    flip(m,crap)
    scale=halal()
    b=juno(scale,crap,l)
    print(b)
main()