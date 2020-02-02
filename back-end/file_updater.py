import pprint

f = open("allergens.txt", "r")
allergens = eval(f.read())
f.close()

print(str(allergens))


command = input("Input a command: (N=new Key Value, E=Edit Key Value, Q=Quit)")
while(command.lower() != 'q'):
    if(command.lower() == 'n'):
        key = input("Input the key")
        value = input("Input next value: (QUIT to quit)")
        allergens[key] = {value}
        value = input("Input next value: (QUIT to quit)")
        while(value != "QUIT"):
            allergens[key].add(value)
            value = input("Input next value: (QUIT to quit)")
    elif(command.lower() == 'e'):
        key = input("Input the existing key")
        value = input("Input next value to add: (QUIT to quit)")
        while(value != "QUIT"):
            allergens[key].add(value)
            value = input("Input next value to add: (QUIT to quit)")
    command = input("Input a command: (N=new Key Value, E=Edit Key Value, Q=Quit)")

f = open("allergens.txt","w")

# f.write('{\n')
# for key,value in allergens.items():
#     f.write(key + ":")
#     for ing in sorted(value):
#         print(key, "->", ing)
f.write( pprint.pformat(allergens) )
f.close()
