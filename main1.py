# pj avl
# tozih kol proj 
# byad tedadi khargosh v tdadi sang v havij ra dar jadval 10 da 10 bgozarim be tori ke be jay yek
# digar nkhoran.vakolshon namaysh dade besh
#start
import random
#1 farakhni ktabkhane random
# 2 skht arye 101 tayy bekhter ziba namysh dadn 101 shod
a=[' ' for x in range(101)] 
# 3 sakht halgh for 11tayy  barya in ke goft shode 11 ta az harkodom
for i in range(11):
    # 4 sakht add random 1 ta 100 
            r2=random.randint(1,100)
# 5 ta vagh barabar nabod ' ' dar jayy halgh  
            while a[r2]!=' ':
                r2=random.randint(1,100)
# 6 agr bod s ro bezar
            a[r2]="s"
# 7 ta vagh barabar nabod ' ' dar jayy halgh  
            while a[r2]!=' ':
# 8 sakht add random 1 ta 100 
                r2=random.randint(1,100)
# 9 agr bod c ro bezar
            a[r2]="c"
# 10 ta vagh barabar nabod ' ' dar jayy halgh  
            while a[r2]!=' ':
# 11 sakht add random 1 ta 100 
                r2=random.randint(1,100)
# 12 agr bod R ro bezar
            a[r2]="R"
#13 sakht skht string bary rekhtan arrye vorodi braye namayesh
ss=""
#14 sakht halgh bar mortb rikhtn arrey be string
for s in range(1,101):
#15 bary in ke 10 dar 10 besh age halge be s%10==0 rsid ber khat bad ba ezaf kardn \n
            if s%10==0:
                ss+="\t"+a[s]
                ss+="\n"
#16 dar gher in sorat ba \t ezafe kone 
            else: 
                ss+="\t"+a[s]
#17 dar akharm nmaysh
print(ss)
#18sakht method save file 
with open("test.bat","w") as f:
                f.write(ss)

























# #1.2 frstadn arrye a be class pro
# d=pro(a)
# #1.3 farkhani method mohasbe 
# d.mohasbe()
###############################################################hazf shode
#2 sakht class pro1 
# class pro1():         
# #2.1 grftn vrodi 
#     def __init__(self,lis):
#         self.lis=lis
# #2.2 sakht method show
#     def show(self):
# #2.3 sakht skht string bary rekhtan arrye vorodi braye namayesh
#         ss=""
# #2.4 sakht halgh bar mortb rikhtn arrey be string
#         for s in range(1,101):
# #2.5 bary in ke 10 dar 10 besh age halge be s%10==0 rsid ber khat bad ba ezaf kardn \n
#             if s%10==0:
#                 ss+="\t"+self.lis[s]
#                 ss+="\n"
# #2.6 dar gher in sorat ba \t ezafe kone 
#             else: 
#                 ss+="\t"+self.lis[s]
# #2.7 dar akharm nmaysh
#         print(ss)
# #2.8sakht method save file 
#         with open("test.bat","w") as f:
#                 f.write(ss)
# # 3 sakht class pro
# class pro(pro1):
# # 4 da ebtada vrodi haro moshkas mikonim
#     def __init__(self,a):
#         self.a=a    
# # 5 method jaygozari khargosh va sang va havig ro misazim
#     def mohasbe(self):          

      
# #16 bro barye nmaysh class pro1 seda kon
#         n=pro1(self.a)
# #17 az method show barye namysh estfade kon
#         print(n.show())       
###############################################################hazf shode



#end
