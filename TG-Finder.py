import requests,random,os
a1 = '\x1b[1;31m'
a2 = '\x1b[1;34m'
a3 = '\x1b[1;32m'
a4 = '\x1b[1;33m'
a5 = '\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
print(a5+"—"*60)
TOK =input(f"{a5}[{a4}?{a5}]{a6} TOKEN:{a3}")
#«♡» 
ID =input(f"{a5}[{a4}?{a5}]{a6} ID:{a3}")
os.system("clear")
print(f"""
{a5}[{a3}1{a5}]{a4} 3-ID | #_#_#  
{a5}[{a3}2{a5}]{a4}  3_ID | #__#_#
{a5}[{a3}3{a5}]{a4} 4-ID | #_#_#_#
{a5}[{a3}4{a5}]{a4} 5ID | #####
""")
C=input(f"{a5}[{a4}?{a5}]{a6} CHOSE:{a3}")
#------------[TELEGRAM]-------------
def TLE():
    R="".join(random.choices("qwertyuiopasdfghjklzxcvbnm"))
    R2="".join(random.choices("_"))
    R3="".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    R5="".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    R6="".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    R7="".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    if C =="1":
        RND=R+R2+R3+R2+R5
    elif C =="2":
        RND=R+R2+R2+R6+R2+R5
    elif C =="3":
        RND=R+R2+R7+R2+R3+R2+R5
    elif C=="4":
        RND=R+R3+R5+R6+R7
    else:
        print(f"{a5}[{a3}✗{a5}]{a1} BaD CHOSE")
    url = f"https://fragment.com/username/{RND}"
    req = requests.get(url).text
    if len(req) < 20000:
        print(f"{a5}[{a4}•{a5}]{a3} GooD:{RND}")
        TLE=f"""< TELEGRAM USERNAME > GooD
[•] < @{RND} > 🔸
_______
BY : [ @KoXVX ]\nCHANNEL: [ @l27_0 ]"""
        requests.get('https://api.telegram.org/bot' + str(TOK) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(TLE))
    else:
        print(f"{a5}[{a3}✗{a5}]{a1} BaD:{RND}")
while True:
    TLE()