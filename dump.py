import os, sys, re, time, random



os.system("git pull")

b="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[00m"
r="\033[1;31m"
g="\033[1;32m"
y = "\033[1;33m"



try:
    import requests
except:
    print(f"{w}[{r}+{w}] Installing requests module\n\n")
    os.system("pip install requests")
try:
    import requests
except:
    os.system("pkg update -y && pkg upgrade -y && pip uninstall requests && pkg install python3 && pip3 install requests")
    sys.exit(f"{w}[{r}+{w}] Please Restart")
try:
    from bs4 import BeautifulSoup as bs
except:
    print(f"\n{w}[{r}+{w}] Installing bs4 module\n\n")
    os.system("pip install bs4")
    sys.exit(f"\n\n{w}[{r}+{w}] Please Restart")
time.sleep(1)





def clear():
    os.system("clear")


def logo():
    txt = f"""{w}
 █████╗ ██████╗       ██╗     ██╗
██╔══██╗██╔══██╗      ██║     ██║
███████║██████╔╝█████╗██║     ██║
██╔══██║██╔══██╗╚════╝██║     ██║
██║  ██║██║  ██║      ███████╗██║
╚═╝  ╚═╝╚═╝  ╚═╝      ╚══════╝╚═╝
        
        
        
       {w}CREATOR  MA KA SHA 
       {w}TOOL     FB-ID-DUMP
       {w}SCRIPT   TAST/FREE 
       {w}VERSION  1.0
"""
    for x in txt:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.007)

idz = []
target = []

def loopz():
    sys.stdout.write(f"\r\r{w}[{r}+{w}] SUCCESS DUMP ID ————({g} {str(len(idz))} {w})————\r")
    sys.stdout.flush()

def finish(lct):
    for i in target:
        pass
    txt = f"\n\n\n{w}[{r}+{w}] Success to dump id from {g}{i}\n{w}[{r}+{w}] FILE SAVE IN {g}{lct}\n"
    for t in txt:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.03)


def writes():
        for xd in idz:
            open(lct,"a").write(xd+"\n")

class Location:
    def __init__(self):
        global lct
        lct = input(f"\n\n\n\n{w}[{r}+{w}] SAVE FILE LOCATION{g} ")
        try:
            open(lct).read()
            clear()
            logo()
        except:
            print(f"{w}[{r}!{w}]{r} FILE NOT FOUND ERROR ...")
            time.sleep(3)
            clear()
            logo()
            Location()




class Login:
    def __init__(self):
        try:
            os.mkdir("d2")
        except:
            pass
        self.ses = requests.Session()
        self.cookie_()
    
    def Format_(self):
        clear()
        logo()
        print(f"\n\n\n\n{w}[{r}1{w}]{g} LOGIN WITH COOKIE\n{w}[{r}2{w}]{g} LOGIN WITH {b}USERNAME{w}/{c}PASSWORD")
        format_ = input(f"\n\n\n\n{w}[{r}+{w}] INPUT LOGIN FORMAT {g}")
        if "1" == format_:
            self.cookie_inp()
        elif "2" == format_:
            self.pass_lg()
        else:
            print(f"\n{w}[{r}!{w}]{r} INPUT WRONG")
            time.sleep(2)
            self.Format_()
            
    def pass_lg(self):
        clear()
        logo()
        self.email = input(f"\n\n\n\n{w}[{r}+{w}] INPUT FB USER NAME {g}")
        self.pwd = input(f"\n{w}[{r}+{w}] INPUT FB PASSWORD {r}")
        ses = requests.Session()
        web = ses.get("https://mbasic.facebook.com").text
        insp = bs(web, "html.parser")
        ld = insp.find("input", {"name":"lsd"})['value']
        jzoest = insp.find("input", {"name":"jazoest"})['value']
        mts = insp.find("input", {"name":"m_ts"})['value']
        lo = insp.find("input", {"name":"li"})['value']
        trynumber = "0"
        unrecognizedtries = "0"
        bixrwh = "0"
        data = {"lsd":ld,"jazoest":jzoest,"m_ts":mts,"li":lo,"try_number":trynumber,"unrecognized_tries":unrecognizedtries,"bi_xrwh":bixrwh,"email":self.email,"pass":self.pwd,"login":"Log In"}
        us1 = "Mozilla/5.0 (Linux; Android "
        us2 = "; XIAOMI Redmi Note"
        us3 = "Pro Build/"
        us4 = ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
        us6 = "Mobile Safari/537.36 AlohaBrowser/2.19.3"
        android_version = random.randint(6,13)
        mobile_version = random.randint(5,14)
        one = random.randint(10,99)
        two = random.randint(1000,9999)
        three = random.randint(100,999)
        usg = f"{us1} {android_version}{us2} {mobile_version} {us3}GT-I9300{us4}{one}. 0.{two}.{three}{us6}"
        header = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-MM,en;q=0.9,my-MM;q=0.8,my;q=0.7,en-GB;q=0.6,en-US;q=0.5','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': usg}
        ps = ses.post("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", data=data, headers=header, allow_redirects=True)
        ck = ses.cookies.get_dict()
        if "c_user" in ck:
            self.cookie = ";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
            open("d2/cookie",'w').write(self.cookie)
            self.Token_g()
        else:
            clear()
            print(f"\n{w}[{r}!{w}] INVAILD {g}USERNAME{w}/{r}PASSWORD ")
            time.sleep(3)
            self.Format_()
        
            
    def cookie_(self):
        clear()
        try:
            self.cookie = {"cookie":open("d2/cookie").read().strip()}
            self.token_g = open("d2/token_g",'r').read()
            self.token_b = open("d2/token_b",'r').read()
            self.token_j = open("d2/token_j",'r').read()
            a = self.ses.get("https://graph.facebook.com/me?fields=name,id&access_token="+self.token_g, cookies=self.cookie).json()['name']
            m = self.ses.get("https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token="+self.token_b, cookies=self.cookie).json()['summary']['total_count']
            n = self.ses.get("https://graph.facebook.com/me?fields=friends.limit(0).fields(id,name,birthday)&access_token="+self.token_j ,cookies=self.cookie).json()['friends']
            clear()
            dump_F()
        except:
            clear()
            print(f"{w}[{r}!{w}]{r} INVAILD COOKIE")
            time.sleep(3)
            clear()
            self.Format_()
            
    def cookie_inp(self):
        clear()
        logo()
        self.cookie = input(f"\n\n\n\n{w}[{r}+{w}] INPUT COOKIE {g}")
        open("d2/cookie",'w').write(self.cookie)
        self.Token_g()
        
    def Token_g(self):
        try:
            self.cookies = open("d2/cookie").read().strip()
            self.respones = self.ses.get("https://business.facebook.com/business_locations", cookies={"cookie":self.cookies}).text
            self.token = re.search('(\["EAAG\w+)', self.respones).group(1).replace('["','')
            open("d2/token_g",'w').write(self.token)
            self.Token_b()
        except:
            clear()
            print(f"{w}[{r}!{w}]{r} INVAILD COOKIE")
            time.sleep(3)
            self.Format_()
        
    def Token_b(self):
        try:
            self.response = self.ses.get("https://www.facebook.com/adsmanager/manage/campaigns", cookies={"cookie":self.cookie})
            self.zz = re.search('act=(.*?)&nav_source',str(self.response.content)).group(1)
            self.zx = f"https://www.facebook.com/adsmanager/manage/campaigns?act={self.zz}&nav_source=no_referrer"
            self.response = self.ses.get(self.zx,cookies={"cookie":self.cookie})
            self.token_ = re.search('accessToken="(.*?)"',str(self.response.content)).group(1)
            open("d2/Token_b",'w').write(self.token_)
            self.Token_j()
        except:
            pass
        
    def Token_j(self):
        try:
            self.cookiie = {"cookie":self.cookie}
            self.ida  = '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e'
            self.data = {"access_token": self.ida, "scope": ""}
            self.response = self.ses.post('https://graph.facebook.com/v16.0/device/login/',data=self.data).json()
            self.code = self.response['code']
            self.u_code = self.response['user_code']
            self.link  = f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={self.code}&access_token={self.ida}"
            self.gt  = bs(self.ses.get('https://mbasic.facebook.com/device',cookies=self.cookiie).content,'html.parser')
            self.find  = self.gt.find('form',{'method':'post'})
            self.data = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(self.find)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(self.gt)).group(1), 'qr' : '0', 'user_code' : self.u_code}
            self.lin  = 'https://mbasic.facebook.com' + self.find['action']
            post  = bs(self.ses.post(self.lin,data=self.data,cookies=self.cookiie).content,'html.parser')
            self.dat  = {}
            self.date  = post.find('form',{'method':'post'})
            for x in self.date('input',{'value':True}):
                try:
                    if x['name'] == '__CANCEL__' :
                        pass
                    else:
                        self.dat.update({x['name']:x['value']})
                except:
                    pass
        except:
            pass
        try:
            links = 'https://mbasic.facebook.com' + self.date['action']
            post = bs(self.ses.post(links,data=self.dat,cookies=self.cookiie).content,'html.parser')
            req = self.ses.get(self.link,cookies=self.cookiie).json()
            tokenx = req['access_token']
            open("d2/token_j",'w').write(tokenx)
        except:
            pass
        Login()




class dump_F:
    def __init__(self):
        clear()
        logo()
        Location()
        self.ses = requests.Session()
        self.cookie = {"cookie":open("d2/cookie").read().strip()}
        self.token_j = open("d2/token_j",'r').read()
        self.token_g = open("d2/token_g",'r').read()
        self.idz = input(f"\n\n\n\n\n{w}[{r}+{w}] FRIENDS ID {g}")
        target.append(self.idz)
        self.check_target()
        
    def check_target(self):
        try: 
            url = f"https://graph.facebook.com/{self.idz}?fields=name&access_token={self.token_g}"
            name = self.ses.get(url, cookies=self.cookie).json()["name"]
            urlz = f"https://graph.facebook.com/{self.idz}?fields=friends.limit(0).fields(id,name,birthday)&access_token={self.token_j}"
            
            fri = self.ses.get(urlz, cookies=self.cookie).json()['friends']['summary']['total_count']
            clear()
            logo()
            print(f"\n\n\n\n{w}[{r}+{w}] FROM ————({g} {name} {w})————\n\n[{r}+{w}] TOTAL FRIENDS ————({g} {str(fri)} {w})————\n\n")
            self.dump_()
        except Exception as e:
            print(f"{w}[{r}+{w}] THIS IS PRIVATE ACCOUNT {r}{self.idz}")
            time.sleep(3)
            self.dump_()
            
    def dump_(self):
        url_ = f"https://graph.facebook.com/{self.idz}?fields=friends.limit(5000).fields(id,name,birthday)&access_token={self.token_j}"
        try:
            dataz = self.ses.get(url_,cookies=self.cookie).json()
            for data in dataz['friends']['data']:
                try:
                    xd, name = data['id'], data['name']
                    idz.append(xd+"|"+name)
                    writes()
                    loopz()
                except:
                    pass
        except:
            pass
        finish(lct)
    
if __name__=='__main__':
    Login()