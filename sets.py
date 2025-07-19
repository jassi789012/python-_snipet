# set is a collection of well-defined objects
# it does not repeat any same elements in it
# sets are unchangable
# it does not maintain order

s = {1,2,3,4,4,5,5,6,6,7,7,7,7}
print(s)




# empty set would show dictionary type

j = {}
print(type(j))




# to create empty set

k = set()
print(type(k))

#union of two sets

s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.union(s2))

print(s1)
print(s2)

#union_update s1

s1.update(s2)
print(s1)

#intesection

city1 = {"berlin", "tokio", "denver"}
city2 = {"tokio", "dagan"}
print(city1.intersection(city2))
print(f"City1 : {city1}")
print(f"city2 : {city2}")

#intersection_update

city1.intersection_update(city2)
print(city1)


# Symmetric Diffrence
# values which are not common


city1 = {"berlin", "tokio", "denver"}
city2 = {"tokio", "dagan"}
print(f"symmertric_diffrence : {city1.symmetric_difference(city2)}")


# isdisjoint return if sets have anything in common or not
city1 = {"berlin", "tokio", "denver"}
city2 = {"tokio", "dagan"}

print(city1.isdisjoint(city2))

#to add one value to set

city1.add("Helsinki")
print(city1)


#to remove element from set

city1.remove("Helsinki")
print(city1)

#discard is simillar to remove but it does not through error 


# pop oppration remove random element from a set

rev = city1.pop()
print(city1)
print(rev)


# del is used to delete the entire set
# syntax :- del(name_of_set)


#clear is used to empty a set


city1.clear()
print(city1)