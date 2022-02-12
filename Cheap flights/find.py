import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent, generate_navigator


def __main__():
    cityName = input("Type in which city you want to visit: ")
    month = input("Which month you want to travel (Forexample: 202202))")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    website = f"https://www.norwegian.no/lavpriskalender/?AdultCount=1&A_City={cityName}&D_City=OSLALL&D_Month={month}&D_Day=12&R_Month=202202&R_Day=12&IncludeTransit=true&TripType=2#/?origin=OSLALL&destination=SPU&outbound=2022-04&inbound=2022-04&adults=1&currency=NOK&eventType=init"
    
    page = requests.get(website, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("strong", class_="lowfare-calendar__price ng-star-inserted")
    print(results)
    



__main__()