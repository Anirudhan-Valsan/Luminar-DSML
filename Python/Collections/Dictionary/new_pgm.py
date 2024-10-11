#course_name,language,duration,place,role

course={"course_name":"DSML","Language":"Python","Duration":6,"Place":"Kochi","Role":"Machine Learning Engineer"}

print(course)

if("Duration" in course.keys()):
    course["Duration"]=10

print(course)

course.update({"course_type":"Internship"})
print(course)


