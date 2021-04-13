# -- coding = utf-8 -- CIE YNG NGINTIP

"follow ig Aryee"
"sub to Arya Tzy"
"telegram Not"

import os, sys
import time
import random
import os.path

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m"
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

os.system('clear')

def cek():
       print merah+"Anda Akan Menginstall Bahan2 Dari Tools Ini"
       oke = raw_input(merah+"Lanjutkan (y/n) : ")
       if oke == 'y':
           cek1()
       else:
           if oke == 'n':
               sys.exit()

def cek1():
        os.system('clear')
        print merah+'izinkan akses penyimpanan'
        nxt()
        os.system(termux-setup-storage)
        nxt()
        os.system('apt install figlet -y && apt install ruby -y && gem install lolcat')
        print cyan+"Cleaning..."
        print green+"[ ! ] Starting CCTV.py"
        menu()

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def out():
        exit()

def back():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mBack \x1b[1;91m]')
        home()

def nxt():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mNext \x1b[1;91m]')
        os.system('clear')

def logo():
        f = open('asci')
        print merah+f.read()
        f.close
        print '---------------------------------------------------'
        print cyan+' Author  : '+green+'Arskuy '
        print cyan+' Github  : '+green+'http://github.com/ziyanfranz '
        print cyan+' Youtube : '+green+'Arya TZY '
        print putih+'---------------------------------------------------'
        print ''

def update():
        os.system('clear')
        os.system('git stash && git pull origin master')
        os.system('python2 install.py')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        home()

def help():
        print green+"List Commands :"
        print cyan+"===================================="
        print merah+"cctv/jabar : CCTV PUBLIC JAWA BARAT"
        print merah+"cctv/kalsel : CCTV PUBLIC KALSEL"
        print merah+"cctv/jakarta : cctv pondok gede jakarta"
        print merah+"Coming Soon"
        print cyan+"====================================="
        back()

def kalsel():
          os.system('clear')
          os.system('figlet CCTV BANJARMASIN | lolcat')
          print cyan+"1.Daerah Simpang Tower - Simpang Pal6"
          print cyan+"2.Taman Siring - Kamboja"
          kalsel = raw_input(merah+"$CCTV > ")
          if kalsel == '1':
              kalsel1()
          else:
              if kalsel == '2':
                  kalsel3()

def kalsel1():
           os.system('clear')
           print cyan+"anda akan memasuki website cctv"
           ok = raw_input(merah+"Lanjut (y/n) : ")
           if ok == 'y':
               kalsel2()
           else:
               if ok == 'y':
                   kalsel()

def kalsel2():
           os.system('clear')
           os.system('termux-open https://atcs.banjarmasinkota.go.id/')
           back()

def kalsel3():
           os.system('clear')
           os.system('termux-open https://cctv.banjarmasinkota.go.id/list')
           back()

def jabar():
         os.system('clear')
         print merah+"Anda Akan Dialihkan Ke Website CCTV JAWA BARAT"
         lol = raw_input(cyan+"Lanjut (y/n) : ")
         if lol == 'y':
             jabar1()
         else:
             if lol == 'n':
                 jabar()

def jabar1():
          os.system('clear')
          os.system('termux-open http://rttmc.dephub.go.id/rttmc/m/page/cctv')
          back()

def pongede():
           os.system('clear')
           print green+'Anda Akan Dialihkan Ke Website CCTV Pondgede(Jakarta)'
           acc = raw_input(merah+'Lajut (y/n) : ')
           if acc == 'y':
               pongede1()
           else:
               if acc == 'n':
                   pongede()

def pongede1():
            os.system('clear')
            os.system('termux-open http://jasamargalive.com/webjm3/mjm/index.php?r=site/getarea&a=2&b=568')
            back()

def menu():
        os.system('clear')
        logo()
        print cyan+"CCTV PUBLIC BY RIZZSPLOIT"
        print merah+"Tidak Untuk Dijual!!"

def pilih():
    zedd = raw_input(merah+'CCTV$ > ')
    if zedd == '':
        print merah+'[!] Ora Paham Aku'
        time.sleep(1)
        os.system('clear')
        home()
    else:
        if zedd == 'cctv/kalsel':
            kalsel()
        else:
            if zedd == 'cctv/jabar':
                jabar()
            else:
              if zedd == 'help':
                help()
                home()
              else:
                                  if zedd == 'cctv/jakarta':
                                        pongede()
                                  else:
                                         if zedd == 'update':
                                           update()
                                         else:
                                           print 'ok'
                                           if zedd == 'exit':
                                             exit()
                                           else:
                                             print '\x1b[1;91m[!] Pilih 1-6'
                                             os.system('clear')
                                             home()

def home():
        menu()
        pilih()

home()