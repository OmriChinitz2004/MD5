def Generator():
    lst=["a","a","a","a","a","a"]
    while(lst[0]!="z" or lst[1]!="z" or lst[2]!="z" or lst[3]!="z" or lst[4]!="z" or lst[5]!="z"):
        index=4
        while(lst[5]!="z"):
            PrintLst(lst)
            lst[5]=chr(ord(lst[5])+1)
        PrintLst(lst)
        index=4
        while(index!=-1):
            if(lst[index]!="z"):
                lst[index]=chr(ord(lst[index])+1)
                ResetAfterIndex(index,lst)
                break
            index-=1


    


def ResetAfterIndex(index,lst):
    for i in range(index+1,len(lst)):
        lst[i]="a"
def PrintLst(lst):
   my_str=""
   for i in lst:
       my_str+=i
   print(my_str) 

Generator()