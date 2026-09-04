number  = [4, 2, 4, 3, 2, 4, 2, 5]

frequency = {}
def most_frequent(number) :
    for num in number:
        count = number.count(num)
        frequency[num]  = count
    highest = max(frequency.values())
    nu =[]
    for key,values in frequency.items():
        if  values == highest :
            nu.append(key)
    return min(nu)
print(most_frequent(number))
