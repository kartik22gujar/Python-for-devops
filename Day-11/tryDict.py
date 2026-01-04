#create dictionary using curly breces

sports_player = {
    "name" : "Sachin", 
    "age" : 48,
    "sport" : "cricket"
}
print("print Dictionary using cury breces",sports_player)

#creat a dictionry using dict() function
student_info = dict( stud_name ="akash" , stud_age = 22 ,stud_sub ="English" )
print("print Dictionary using dict()",student_info)

#accessing value using [] bracke 
print("********************accessing value using [] square brackets**********************")
name = sports_player["name"]
print("Sprots Player Name: ",name)
print("Student name:",student_info["stud_name"])

print("********************accessing value using get() method**********************")
stud_age=student_info.get("stud_age")
print("Student age: ",stud_age)
print("player age: ",sports_player.get("age"))
print("********************modify value of existing key**********************")
print("player age befor modify: ",sports_player["age"])
sports_player["age"] = 22
print("player age after modify: ",sports_player["age"])

print("********************adding new key-value player in existing Dictionary**********************")
print("dictionay befor added key-value",sports_player)
sports_player["type"]= "batting"
print("dictionay after added key-value",sports_player)

# Iterating in dictioary
print("***********Itratinon through keys***********")
for key in sports_player:
    print("key:",key)
print("***********Itratinon through value***********")
for value in sports_player:
    print("value:",sports_player[value])
print("***********Itratinon through key-value pair***********")
for key ,value in sports_player.items():
    print("key: ",key," value:",value)

