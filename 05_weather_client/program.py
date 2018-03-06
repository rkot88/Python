import requests
import bs4
import collections

WeatherReport = collections.namedtuple("WeatherReport", "cond, temp, scale, loc")


def main():
    # print the header
    print_the_header()

    # get zipcode from user
    code = input("What zip code do you want weather for? US only ")

    # get html from web
    html = get_html_from_web(code)

    # parse the html
    report = get_weather_from_html(html)

    # print("The temp in {} this locations is {} and {} {}".format(
    #     report[2],
    #     report[0],
    #     report[1],
    #     report[3],
    # ))

    print("The temp in {} is {} {} and {}".format(
        report.loc,
        report.temp,
        report.scale,
        report.cond,
    ))


    # display for the forecast


def print_the_header():
    print("-------------------------")
    print("--------Weather----------")
    print("-------------------------")
    print()


def get_html_from_web(zipcode):
    url = "https://www.wunderground.com/weather-forecast/{}".format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    # cityCSS = ('div.region-content-header h1')
    # weatherConditionsCss = ('div.condition-icon p')
    # weatherTempCss = ('div.current-temp span.wu-value') temperature
    # weatherScaleCss = $('div.current-temp span.wu-label') units

    soup = bs4.BeautifulSoup(html, "html.parser")

    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(condition, temp, "°" + scale, loc) only printing weather

    # return condition, temp, scale, loc # returning the tuple (condition, temp, scale, loc) parentheses not needed

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report

def find_city_and_state_from_location(loc: str):
    parts = loc.split("\n")
    return parts[0].strip()


def cleanup_text(text: str):  # use : and class name and then Pycharm will help u during
    # process giving sudgestions about available functions e.g strip
    if not text:  # if there is no text
        return text

    text = text.strip()  # build in method to the string class that will take all w hite
    # space tabs space new line \\ etc from the front end from the end of the string
    return text


if __name__ == '__main__':
    main()
