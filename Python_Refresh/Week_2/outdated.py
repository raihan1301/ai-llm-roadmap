def main():
    date = input("enter your date: ")
    response = convert(date)
    print(response)

def convert(date):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    if "/" in date:
        month,day,year = date.split("/")

        month = int(month)
        day = int(day)
        year = int(year)

    else:
        month,day,year = date.split(" ")

        month = months.index(month) + 1  #because index starts from 0, here we are getting index from months list
        day = int(day.replace(",",""))
        year = int(year)
    
    return f"{year:04}-{month:02}-{day:02}"  #02 this shows how many number it should display, if its just 7 it will show 07

main()