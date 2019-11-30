list1=[5,9,12,16,18,22,17,45,84,134,234,146,275,246,232,123,304,307,301,312,305,308,328,322]
list1=list(dict.fromkeys(list1))
f=open("st.jpg","r")
encrypt=f.readline()
len1=str(f.readline())
msg=""
k=0
for i in list1:
    msg=msg+encrypt[i]
    k=k+1
    if(k==int(len1)):
        break
print(msg)

f.close()