# pj avl
# tozih kol proj 
# byad tedadi khargosh v tdadi sang v havij ra dar jadval 10 da 10 bgozarim be tori ke be jay yek
# digar nkhoran.vakolshon namaysh dade besh
#start
import random
#1 farakhni ktabkhane random
#2 sakht class pro1 
class pro1():         
#2.1 grftn vrodi 
    def __init__(self,lis):
        self.lis=lis
#2.2 sakht method show
    def show(self):
#2.3 sakht skht string bary rekhtan arrye vorodi braye namayesh
        ss=""
#2.4 sakht halgh bar mortb rikhtn arrey be string
        for s in range(1,101):
#2.5 bary in ke 10 dar 10 besh age halge be s%10==0 rsid ber khat bad ba ezaf kardn \n
            if s%10==0:
                ss+="\t"+self.lis[s]
                ss+="\n"
#2.6 dar gher in sorat ba \t ezafe kone 
            else: 
                ss+="\t"+self.lis[s]
#2.7 dar akharm nmaysh
        print(ss)
# 3 sakht class pro
class pro(pro1):
# 4 da ebtada vrodi haro moshkas mikonim
    def __init__(self,a):
        self.a=a    
# 5 method jaygozari khargosh va sang va havig ro misazim
    def mohasbe(self):          
# 6 sakht halgh for 11tayy  barya in ke goft shode 11 ta az harkodom
        for i in range(11):
# 7 sakht add random 1 ta 100 
            r2=random.randint(1,100)
# 8 ta vagh barabar nabod ' ' dar jayy halgh  
            while self.a[r2]!=' ':
                r2=random.randint(1,100)
# 9 agr bod s ro bezar
            self.a[r2]="s"
# 10 ta vagh barabar nabod ' ' dar jayy halgh  
            while self.a[r2]!=' ':
# 11 sakht add random 1 ta 100 
                r2=random.randint(1,100)
# 12 agr bod c ro bezar
            self.a[r2]="c"
# 13 ta vagh barabar nabod ' ' dar jayy halgh  
            while self.a[r2]!=' ':
# 14 sakht add random 1 ta 100 
                r2=random.randint(1,100)
# 15 agr bod R ro bezar
            self.a[r2]="R"
#16 bro barye nmaysh class pro1 seda kon
        n=pro1(self.a)
#17 az method show barye namysh estfade kon
        print(n.show())       

# 1.1 skht arye 101 tayy bekhter ziba namysh dadn 101 shod
a=[' ' for x in range(101)] 
#1.2 frstadn arrye a be class pro
d=pro(a)
#1.3 farkhani method mohasbe 
d.mohasbe()


#end
