# Write your code here
print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")

print("Write how many cups of coffee you will need:")
coffee_cups = int(input())

# amounts for the needed coffee_cups

water = int(coffee_cups * 200)
milk = int(coffee_cups * 50)
coffee_beans = int(coffee_cups * 15)

print(f"""For {coffee_cups} cups of coffee you will need:
{water} ml of water
{milk} ml of milk
{coffee_beans} g of coffee beans""")
