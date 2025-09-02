def calculate_age(year_of_birth):
    current_year = 2025
    print(current_year)
    return current_year - year_of_birth

def bio(name, year, gender):
    
    return {
        "name": name,
        "age": calculate_age(year),
        "gender": gender
    }
    
print(bio("tom", 2000, "M"))
print(calculate_age(2000))    