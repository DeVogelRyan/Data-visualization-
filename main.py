import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))

labels=[]

for x in range(1, 6):
    user_input = input(f"Give me a name for label {x} pls: ")
    labels.append(user_input)
    

values=[]

for x in range(1, 6):
    user_input = input(f"Give me a value for label {x} pls: ")
    values.append(user_input)

plt.pie(values, labels=labels, autopct="%.1f%%")
plt.show()