
def test(a,b,c,*d,**e):
    print("A : ",a,"B : ",b,"c : ",c,"d : ",d,"E : ",e)

test(1,2,3,4,5,6,7,8,9,X=10,Y=20,Z=30)

