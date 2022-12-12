from bs4 import BeautifulSoup as BS
import requests as REQ

def scapeOGR():
    url=REQ.get('https://warhammer-40k-darktide.fandom.com/wiki/Ogryn:_Skullbreaker') #needs url
    soup=BS(url.text, "html.parse")
    stats=soup.find_all(attrs={'class':'fandom-table'})
    print(stats)
    return(stats)
    

# def scapeZEL():
#     url=REQ.get() #needs url
#     stats=#[list of stats]
#     return(stats)

# def scapePHY():
#     url=REQ.get() #needs url
#     stats=#[list of stats]
#     return(stats)

# def scapeVET():
#     url=REQ.get() #needs url
#     stats=#[list of stats]
#     return(stats)
def main():
    scapeOGR
main()