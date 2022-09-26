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



# year = int(input())
#
# next_year = year
# final_year = 0
#
# stop = False
# string_of_final_year = str(final_year)
# set_of_final_year = set(string_of_final_year)
#
# while stop == False:
#     final_year += 1
#     lenght_of_next_year = len(set_of_final_year)
#     lenght_of_year = len(str(year))
#     if lenght_of_next_year == lenght_of_year:
#         stop = True
#         print(final_year)


# year = 9013
# lenght_of_year = len(set(str(year)))
# print(lenght_of_year)

# year1 = len(set(str(year)))
# print(year1)
# print(year1)
#
# # year = 1998
# years = 2000
