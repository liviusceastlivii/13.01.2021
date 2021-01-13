with open ("input.txt","r") as f:
    c=f.readline()    
    a=int(c)-2
    b=int(c)-1
    d=int(c)+1
    e=int(c)+2
with open ("output.txt","w") as f:
    f.write(str(a))
    f.write(" ")
    f.write(str(b))
    f.write(" ")
    f.write(str(c))
    f.write(" ")
    f.write(str(d))
    f.write(" ")
    f.write(str(e))