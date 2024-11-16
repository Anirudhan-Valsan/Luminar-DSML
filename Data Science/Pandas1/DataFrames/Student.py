import pandas as pd

#id,fname,lname,sub1,sub2,sub3,coll_name

students = [[101,"Anirudhan","Valsan",70,50,60,"M.A College Of Engineering"],[105,"Amal","Das",50,55,60,"St Anns"],[102,"Sreerag","Das",80,60,70,"GPTC"],[107,"Arjun","Krishna",80,70,70,"M.A College Of Engineering"],[109,"Rajshekhar","M.A",80,60,70,"M.A College Of Engineering"]]

df =pd.DataFrame(students,index=range(1,len(students)+1),columns=["Id","F_NAME","L_NAME","PHY","CHEM","MATHS","COLLEGE NAME"])
print(f"Shape {df.shape}, \nData Type : \n{df.dtypes}")
print("*"*100)
print(df)
