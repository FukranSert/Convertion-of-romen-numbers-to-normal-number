Romen_numeral=input("Enter your romen number=").upper()
list1=["I","V","X","L","C","D","M"]
result=0
list2=["IV","IX","XL","XC","CD","CM","MV"]
list3=[]
for x in Romen_numeral:
    list3.append(x)


def Converter():
    global result
    if all(x in list1 for x in list3):



        for x in Romen_numeral:
            if x=="I":
                result=result+1
            elif x=="V":
                result=result+5
            elif x=="X":
                result=result+10
            elif x=="L":
                result=result+50
            elif x=="C":
                result=result+100
            elif x=="D":
                result=result+500
            elif x=="M":
                result=result+1000





        for ü in list2:
            if ü in Romen_numeral:
                if ü=="IV" or ü=="IX":
                    result=result-2
                elif ü=="XL" or ü=="XC":
                    result=result-20
                elif ü=="CD" or ü=="CM":
                    result=result-200
                if list3.count("M")==1:
                    if ü=="MV":
                        result=result+2995
        print(f"Arabic Number={result}")
    else:
        print("You entered wrong character")




Converter()



