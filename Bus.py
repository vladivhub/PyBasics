passengers = int(input())
stops = int(input())

# its done by slave

for i in range(1, stops + 1):
    passengers_off = int(input())
    passengers_on = int(input())
    if i % 2 != 0:
        passengers = passengers - passengers_off + passengers_on + 2
    elif i % 2 == 0:
        passengers = passengers - passengers_off + passengers_on - 2

print(f"The final number of passengers is : {passengers}")
