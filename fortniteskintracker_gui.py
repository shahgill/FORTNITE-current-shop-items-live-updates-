from tkinter import *
import requests
import json

root = Tk()
#73231

photol = PhotoImage(file = "YOUR FAVOURITE FORTNITE BACKGROUND'S URL")
label= Label(root, image = photol)
label.pack()

title = Label(root, text = 'CURRENT SHOP ITEMS', font = ("bauhaus 93", 30), fg = "white", bg = "red")
title.place(x = 10, y = 100)

title_two = Label(root, text = 'PLAYER RANKINGS', font = ("bauhaus 93", 30), fg = "white", bg = "red")
title_two.place(x = 800, y = 95)
#title.pack()


url = "https://fortnite-public-api.theapinetwork.com/prod09/store/get"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"language\"\r\n\r\nen\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Authorization': "5cdcbcb049eed987ddf6643f781268e4"
    }


r = requests.request("POST", url, data=payload, headers=headers)
r.encoding = 'ISO-8859-1'
text = r.json()

items = text['items']
print(items)
#print(items[0])
nine = (items[0].get('name'),items[0].get('cost'), 'V Bucks')
#print(items[1])
zero = (items[1].get('name'),items[1].get('cost'), 'V Bucks')
#zeroo = (items[1].get('cost'), 'V Bucks')
#print(items[2])
one = (items[2].get('name'),items[2].get('cost'), 'V Bucks')
#print(items[2].get('cost'), 'V Bucks')
#print(items[3])
two = (items[3].get('name'),items[3].get('cost'), 'V Bucks')
#print(items[3].get('cost'), 'V Bucks')
#print(items[4])
three = (items[4].get('name'),items[4].get('cost'), 'V Bucks')
#print(items[4].get('cost'), 'V Bucks')
#print(items[5])
four = (items[5].get('name'),items[5].get('cost'), 'V Bucks')
#print(items[5].get('cost'), 'V Bucks')
#print(items[6])
five = (items[6].get('name'),items[6].get('cost'), 'V Bucks')
#print(items[6].get('cost'), 'V Bucks')
#print(items[7])
six = (items[7].get('name'),items[7].get('cost'), 'V Bucks')
#print(items[7].get('cost'), 'V Bucks')
#print(items[8])
seven = (items[8].get('name'),items[8].get('cost'), 'V Bucks')
#print(items[8].get('cost'), 'V Bucks')
#print(items[9])
eight = (items[9].get('name'),items[9].get('cost'), 'V Bucks')
#print(items[9].get('cost'), 'V Bucks')


'''for p in items :
  print(p['name'],p['cost'], "V Bucks")'''

  

items_zero = Label(root, text = zero , font = ("arial black", 10), fg = "white", bg = "red")
items_zero.place(x = 10, y = 210)

items_one = Label(root, text = one , font = ("arial black", 10), fg = "white", bg = "red")
items_one.place(x = 10, y = 250)

items_two = Label(root, text = two , font = ("arial black", 10), fg = "white", bg = "red")
items_two.place(x = 10, y = 290)

items_nine = Label(root, text = nine , font = ("arial black", 10), fg = "white", bg = "red")
items_nine.place(x = 10, y = 330)

items_three = Label(root, text = three , font = ("arial black", 10), fg = "white", bg = "red")
items_three.place(x = 10, y = 370)

items_four = Label(root, text =four , font = ("arial black", 10), fg = "white", bg = "red")
items_four.place(x = 10, y = 410)

items_five = Label(root, text = five , font = ("arial black", 10), fg = "white", bg = "red")
items_five.place(x = 10, y = 450)

items_six = Label(root, text = six , font = ("arial black", 10), fg = "white", bg = "red")
items_six.place(x = 10, y = 490)

items_seven = Label(root, text = seven , font = ("arial black", 10), fg = "white", bg = "red" )
items_seven.place(x = 10, y = 530)

items_eight = Label(root, text = eight , font = ("arial black", 10), fg = "white", bg = "red")
items_eight.place(x = 10, y = 570)

new_items = Label(root, text = "New items at 4:00 AM" , font = ("verdana", 10), fg = "white", bg = "red")
new_items.place(x = 10, y = 680)


url = "https://fortnite-public-api.theapinetwork.com/prod09/leaderboards/get"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"window\"\r\n\r\ntop_10_kills\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Authorization': "5cdcbcb049eed987ddf6643f781268e4"
    }

rr = requests.request("POST", url, data=payload, headers=headers)
rr.encoding = 'ISO-8859-1'
textt = rr.json()

entries = textt['entries']

ten = (entries[0].get('username'),entries[0].get('kills'),entries[0].get('wins'),entries[0].get('matches'),entries[0].get('minutes'),entries[0].get('score'),entries[0].get('platform'),entries[0].get('rank'))
eleven = (entries[1].get('username'),entries[1].get('kills'),entries[1].get('wins'),entries[1].get('matches'),entries[1].get('minutes'),entries[1].get('score'),entries[1].get('platform'),entries[1].get('rank'))
twelve = (entries[2].get('username'),entries[2].get('kills'),entries[2].get('wins'),entries[2].get('matches'),entries[2].get('minutes'),entries[2].get('score'),entries[2].get('platform'),entries[2].get('rank'))
thirteen = (entries[3].get('username'),entries[3].get('kills'),entries[3].get('wins'),entries[3].get('matches'),entries[3].get('minutes'),entries[3].get('score'),entries[3].get('platform'),entries[3].get('rank'))
fourteen = (entries[4].get('username'),entries[4].get('kills'),entries[4].get('wins'),entries[4].get('matches'),entries[4].get('minutes'),entries[4].get('score'),entries[4].get('platform'),entries[4].get('rank'))
fifteen = (entries[5].get('username'),entries[5].get('kills'),entries[5].get('wins'),entries[5].get('matches'),entries[5].get('minutes'),entries[5].get('score'),entries[5].get('platform'),entries[5].get('rank'))
sixteen = (entries[6].get('username'),entries[6].get('kills'),entries[6].get('wins'),entries[6].get('matches'),entries[6].get('minutes'),entries[6].get('score'),entries[6].get('platform'),entries[6].get('rank'))
seventeen = (entries[7].get('username'),entries[7].get('kills'),entries[7].get('wins'),entries[7].get('matches'),entries[7].get('minutes'),entries[7].get('score'),entries[7].get('platform'),entries[7].get('rank'))
eighteen = (entries[8].get('username'),entries[8].get('kills'),entries[8].get('wins'),entries[8].get('matches'),entries[8].get('minutes'),entries[8].get('score'),entries[8].get('platform'),entries[8].get('rank'))
nineteen = (entries[9].get('username'),entries[9].get('kills'),entries[9].get('wins'),entries[9].get('matches'),entries[9].get('minutes'),entries[9].get('score'),entries[9].get('platform'),entries[9].get('rank'))

items_ten = Label(root, text = ten , font = ("arial black", 10), fg = "white", bg = "red")
items_ten.place(x = 750, y = 210)

items_eleven = Label(root, text = eleven , font = ("arial black", 10), fg = "white", bg = "red")
items_eleven.place(x = 750, y = 250)

items_twelve = Label(root, text = twelve , font = ("arial black", 10), fg = "white", bg = "red")
items_twelve.place(x = 750, y = 290)

items_thirteen = Label(root, text = three , font = ("arial black", 10), fg = "white", bg = "red")
items_thirteen.place(x = 750, y = 330)

items_fourteen = Label(root, text = fourteen , font = ("arial black", 10), fg = "white", bg = "red")
items_fourteen.place(x = 750, y = 370)

items_fifteen = Label(root, text =fifteen , font = ("arial black", 10), fg = "white", bg = "red")
items_fifteen.place(x = 750, y = 410)

items_sixteen = Label(root, text = sixteen , font = ("arial black", 10), fg = "white", bg = "red")
items_sixteen.place(x = 750, y = 450)

items_seventeen = Label(root, text = seventeen , font = ("arial black", 10), fg = "white", bg = "red")
items_seventeen.place(x = 750, y = 490)

items_eighteen = Label(root, text = eighteen , font = ("arial black", 10), fg = "white", bg = "red" )
items_eighteen.place(x = 750, y = 530)

items_nineteen = Label(root, text = nineteen , font = ("arial black", 10), fg = "white", bg = "red")
items_nineteen.place(x = 750, y = 570)

indicator = Label(root, text = "USER NAME|KILLS|WINS|MATCHES|SCORE|PLATFORM|RANK" , font = ("arial black", 9), fg = "white", bg = "red")
indicator.place(x = 740, y = 175)

root.mainloop()
