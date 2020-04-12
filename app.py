import re
import mechanize
from time import sleep

br = mechanize.Browser()

response = br.open('https://api.census.gov/data/2018/acs/acs5/variables.html')

for link in br.links():
    siteMatch = re.compile( '.json' ).search( link.url )
    if siteMatch:
        sleep(0.001)
        resp = br.follow_link( link )
        f = open(link.url, "wb")
        f.write(resp.get_data())
        br.back()
        print("File ", link.url, " has been downloaded")