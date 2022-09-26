year = int(input())
stop = False
while stop == False:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])
    if len(str(year)) == len(set_year):
        stop = True
print(year)


