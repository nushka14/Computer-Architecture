f=open("trace.txt","r")
apt=0
n=0
for i in f:
    s=i.split( )
    if s[1]=='T':
        apt=apt+1
    n+=1
rm_at=(n-apt)*100/n
print('misprediction when always taken =',rm_at)
rm_nt=100-rm_at
print('misprediction when always not taken =',rm_nt)
