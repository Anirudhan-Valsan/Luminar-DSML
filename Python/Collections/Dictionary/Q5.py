mobiles={"Apple":{"model":"iphone15","price":120000,"color":["black","red","golden"]},
         "Samsung":{"model":"s23 ultra","price":180000,"color":["yellow","red","white"]},
         "Sony":{"model":"xperia ultra","price":130000,"color":["black","orange","red"]},
         "Huawei":{"model":"Pura 70 ultra","price":170000,"color":["black","brown","white"]}}


mobiles["Sony"]["color"][1]="white"


#print(mobiles["Sony"])



#filter the element with black colour


'''for i in mobiles:
    if "black" in mobiles[i]["color"]:
        print(f"{i} : {mobiles[i]}")'''


#filter with mobile pricw >150000 , with black or red in color



for i in mobiles:
    if mobiles[i]["price"]>150000 and ("black" or "red " in mobiles[i]["color"]):
            print(f"{i} :  {mobiles[i]}")