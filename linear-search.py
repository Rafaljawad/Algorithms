#Python program to implement linear search
countries=["usa","jordan","tokyou","china","egypt","canda","oman","france"]
country_to_find="france"
def find_country(list,country):
    i=0
    res=False
    while i<len(list):
        if(list[i]==country):
            print(f"{country} found at index {i}")
        res=True
        i+=1
    return res
if find_country(countries,country_to_find):
    print(f"{country_to_find} found in countries list")
else:
    print(f"{country_to_find} not found in countries list")