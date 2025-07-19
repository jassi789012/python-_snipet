letter = "Hello my name is {} and my country is {}"
name = "jassi"
country = "india"

print(letter.format(name, country))





letter = "Hello my name is {0} and my country is {1}"
name = "jassi"
country = "india"

print(letter.format(name, country))





letter = "Hello my name is {1} and my country is {0}"
name = "jassi"
country = "india"

print(letter.format(country, name))


txt = f"hello guys my name is {name} and my country name is {country}"
print(txt)

totalPrice = 100.234434
print(f"total price is {totalPrice:.2f}")

txt = f"hello guys my name is {{name}} and my country name is {{country}}"
print(txt)


