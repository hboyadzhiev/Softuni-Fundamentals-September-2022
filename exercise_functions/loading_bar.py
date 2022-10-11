def loading_bar(number):
    percent_signs = "%" * (number // 10)
    dots_count = "." * ((100 - number) // 10)
    if number < 100:
        return f"{number}% [{percent_signs}{dots_count}] \nStill loading..."
    return "100% Complete! \n[%%%%%%%%%%]"

current_number = int(input())
print(loading_bar(current_number))