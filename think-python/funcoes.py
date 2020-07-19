import math

hours = 1
degrees = int(input('Insert degrees: '))
x = math.sin(degrees / 360.0 * 2 * math.pi)

# Chamadas de função

x = math.exp(math.log(x+1))

minutes = hours * 60

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print(print_lyrics())
