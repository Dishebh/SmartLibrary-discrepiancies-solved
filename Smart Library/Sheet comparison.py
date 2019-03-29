import pandas as pd

'''dict1 = { "Entry ID": ["Dishebh", "Raghav", "Hemant"],
         "Exit ID": ["Dishebh", "Raghav", "Hemant"] }
table1 = pd.DataFrame(dict1)'''

data1 = pd.read_csv("Vibhav entry.csv")
print(data1)

data2 = pd.read_csv("Vibhav locker.csv")

print(data2)

data = pd.DataFrame()
data.insert(0, "Time IN", data1["Time IN"])
data.insert(1, "Time OUT", data1["Time OUT"])
data.insert(2, "TIME", data2["TIME"])
data.insert(3, "Card ID", data1["Card ID"])
print(data)


    

data["TIME greater than Time OUT"] = data["TIME"] > data["Time OUT"]
print(data)


data2["USER_ID"] = "184077"

'''dict2 = { "Locker ID": ["Dishebh", "Raghav", "Ronak", "Prateek"] }
table2 = pd.DataFrame(dict2)'''

entry = []

for entry2 in data2["USER_ID"]:
    k = 0
    for entry1 in data1["Card ID"]:
        if entry1 != entry2:
            k += 1
        if k >=  len(data1["Card ID"]):
            entry.append(entry2)
            
            
newEntry = []  
for i in entry:
    if i not in newEntry:
        newEntry.append(i)

for i in newEntry:
    print(i, "entry is invalid!")
        
    

 