stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

# stops.append("Edinburgh Waverly")

# print(stops)

# stops.insert(0,'Glasgow Queen St')

# print(stops)

# stops.insert(3,'Polmont')

# print(stops)

# print(stops.index('Linlithgow'))

# stops.remove('Livingston')

# print(stops)

# stops.pop(1)

# print(stops)

# print(len(stops))

# sorted_stops = sorted(stops)
# print(sorted_stops)

# stops.reverse()

# print(stops)


for stop in stops:
    print(f"the next stop is {stop}")