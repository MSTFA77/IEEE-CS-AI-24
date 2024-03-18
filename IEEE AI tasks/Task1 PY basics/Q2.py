from datetime import datetime, timedelta
def getom(d, m, y):
    cd = datetime(y, m, d)
    nd = cd + timedelta(days=1)
    return nd.day, nd.month, nd.year
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
nd, nm, ny = getom(day, month, year)
print("Tomorrow's date:")
print("Day:", nd,"Month:", nm,"Year:", ny)
