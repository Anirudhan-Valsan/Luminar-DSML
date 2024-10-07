mobiles={"Apple":{"model":"iphone15","price":120000,"color":"black"},
         "Samsung":{"model":"s23 ultra","price":180000,"color":"white"},
         "Sony":{"model":"xperia ultra","price":130000,"color":"red"},
         "Huawei":{"model":"Pura 70 ultra","price":170000,"color":"black"}}



mobiles["Apple"]["model"]="iphone16"




'''for i in mobiles:
    if mobiles[i]["color"]=="black":
        print(f"{i} : {mobiles[i]}")'''


#filter less than 150000


'''for i in mobiles:
  if (mobiles[i]["price"] <150000):
    print(f"{i} : {mobiles[i]}")  '''

#filter >150000 and white

for i in mobiles:
  if (mobiles[i]["price"] > 150000) and (mobiles[i]["color"]=="white"):
    print(f"{i} : {mobiles[i]}")  