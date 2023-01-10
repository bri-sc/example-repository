
year = 2012

if year%4 == 0 and year%400 == 0:
    leap_year = "Yes"
elif year%4 == 0 and year%100 == 0:
    leap_year = "No"
elif year%4 == 0:
    leap_year = "Yes"
else:
    leap_year = "No"

print(f"Is {year} a leap year? {leap_year}")
