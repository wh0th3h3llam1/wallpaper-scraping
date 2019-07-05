# Python Script to Download Wallpapers in any resolution available
# This Code Currently Works Only for WallpapersWide.com
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


from bs4 import BeautifulSoup as bs
import requests
import wget
try:
    import httplib # Python 2
except:
    import http.client as httplib # Python 3
 

def has_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


def wallpaper_scraping():

    website = 'http://wallpaperswide.com'

    categories = [
    	'/architecture-desktop-wallpapers',
    	'/artistic-desktop-wallpapers',
    	'/black_and_white-desktop-wallpapers',
    	'/computers-desktop-wallpapers',
    	'/games-desktop-wallpapers',
    	'/nature-desktop-wallpapers',
    	'/space-desktop-wallpapers',
    	'/sports-desktop-wallpapers',
    	'/travel-desktop-wallpapers',

    	]
    print()
    print("Category Of Wallpapers -->")

    i = 1

    for c in categories:
        print("\t" + str(i) + " : " + c)
        i += 1

    print()

    category_selected = int(input("Please Choose a Category : "))

    category_selected = categories[category_selected - 1]

    print("category_selected : " + category_selected)
    links = []

    pages = int(input("Enter No. of Pages to Scrape : "))


    for i in range(1, pages):
        source = requests.get(website + category_selected + '/page/' + str(i)).text
        soup = bs(source, 'lxml')

        for li in soup.find_all('li', class_='wall'):
            
            wallpaper_link = li.find('a')['href']

            link = website + "/download" + wallpaper_link
            
            links.append(link)

    resolution_available = []

    resolution_selected = "1920x1080"

    down_link = []
    for l in links:
        str(l)
        l = l[:-6] + '-' + resolution_selected + '.jpg'
        down_link.append(l)

    print("Current Resolution is : " + resolution_selected)

    download_path = input("Enter Full Path To Save all the Wallpapers : ")

    try:
        
        i = 1
        for d in down_link:
            wget.download(d, download_path + str(i) + ".jpg")
            i += 1

        print("Successfully Downloaded " + i + " Wallpapers.")

    except Exception as e:
        print("Error While Downloading Wallpapers : " + str(e))


def main():

    if has_internet():
        print("Internet is Connected.")
        print()
        
        wallpaper_scraping()
    else:
        print("No Internet Connection.")
        print("Please Try Again.")

    

main()
