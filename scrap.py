from bs4 import BeautifulSoup
import cfscrape

import webbrowser

scraper = cfscrape.create_scraper()
site = "https://ww1.soul-anime.us/"
page = scraper.get(site).content

soup = BeautifulSoup(page, "html.parser")
a = soup.find("div", id="ep")
b = a.find_all("div",class_="td")

anime_list=["Boku No Hero Academia 3rd Season", "Steinsgate 0", "Boruto Naruto Next Generations", "Tokyo Ghoulre"]
episode_list = ['0', '0', '0', '0']
time_list = ['0', '0', '0', '0']
link_list = ["","","",""]

for anime in b:
    name = anime.find_next().find_next().string
    for idx, anime_name in enumerate(anime_list):
        if name == anime_name:
            episode = anime.findChildren("div", class_="ep")[0].string
            time = anime.findChildren("span")[0].string
            link = anime.findChildren("a")[1]['href']
            episode_list[idx] = episode
            time_list[idx] = time
            link_list[idx] = link
#t = Table()
#t["Anime"] = ["My Hero Academia", "Steins Gate", "Boruto", "Tokyo Ghoul:re"]
#t["Episodes"] = episode_list
#t["Time"] = time_list

html = '''<!DOCTYPE html><head><title>Anime Updates</title><style>
    body{
        background-color: #303030;
        color: white;
    }
table, td, th {    
    background-color: #424242;
    }
table {
    margin-left:auto;
    margin-right:auto;
    border-collapse: collapse;
    width: 40%;
    box-shadow: 3px 3px rgba(0, 0, 0, 0.19);
}
td {
    text-align: center;
    padding: 16px;
}
.lin{
    padding:16px 0px;
}
th {
    width: 50px;
    padding: 16px;
    background-color: #212121;
    color: white;
}
    a:link, a:visited {
    background-color: #00796B;
    color: white;
    padding: 14px 40px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
}


a:hover, a:active {
    background-color: #00E676;
}
</style>
</head>
<body>
    <table>
        <tr>    
            <th>'''

for i in range(len(anime_list)):
    if i == len(anime_list)-1:
        html = html + anime_list[i] + "</th></tr>"
        break

    html = html + anime_list[i] + "</th><th>"

for i in range(len(episode_list)):
    if i==0 :
        html = html + "<tr><td>"
    if i == len(episode_list)-1:
        html = html + episode_list[i] + "</td></tr>"
        break

    html = html + episode_list[i] + "</td><td>"


for i in range(len(time_list)):
    if i==0 :
        html = html + "<tr><td>"
    if i == len(time_list)-1:
        html = html + time_list[i] + "</td></tr>"
        break

    html = html + time_list[i] + "</td><td>"

for i in range(len(link_list)):
    if i==0 :
        html = html + "<tr><td class=\"lin\"><a href=\""
    if i == len(link_list)-1:
        html = html + link_list[i] + "\">Link</a></td></tr>"
        break

    html = html + link_list[i] + "\">Link</a></td><td class=\"lin\"><a href=\""

html = html + "</table></body></html>"

try:
    f = open("result.html", mode='w', encoding='UTF-8')
    f.write(html)
finally:
    f.close()

webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("result.html")

#print(soup.prettify())