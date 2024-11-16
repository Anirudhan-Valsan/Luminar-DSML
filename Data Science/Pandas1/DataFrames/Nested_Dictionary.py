import pandas as pd

dic = {"ID": [1, 2, 3, 4, 5], "F_NAME": ["Anirudhan", "Amal", "Aswin", "Sreerag", "Athul"], "AGE": [25, 26, 22, 33, 22], "PROFESSION": ["ML Engineer", "VFX", "Aalyst", "Signal Engineer", "Developer"]}


df = pd.DataFrame(dic,index=range(1,len(dic)+2))
print(df)
