from tkinter import *
import webbrowser
from datetime import date

################## WINDOW

root = Tk()
root.title('WBC')
img = PhotoImage( fil = 'D:\\Pessoal\\Documents\\wbc\\wbc.png')
root.geometry('610x80')
root.iconphoto(False, img)
menubar = Menu(root)
credits = Label(root, text = '''
Web Browser Center
11/3/2022
version 0.1
''')
credits.pack()

################## CONFIG

def close():
 exit()
 
def github():
 webbrowser.open('https://github.com/atheodog/wbc')
 
################## BROWSERS

def baidu():
 webbrowser.open('https://baidu-browser.en.softonic.com/')

def brave():
 webbrowser.open('https://brave.com/download/')
 
def bravenightly():
 webbrowser.open('https://brave.com/download-nightly/')
 
def bravebeta():
 webbrowser.open('https://brave.com/download-beta/')
 
def basilisk():
 webbrowser.open('https://www.basilisk-browser.org/')
 
def blisk():
 webbrowser.open('https://blisk.io/')
 
def beaker():
 webbrowser.open('https://beakerbrowser.com/')

def ungoogledchromium():
 webbrowser.open('https://github.com/orgs/ungoogled-software/repositories')
 
def chrome():
 webbrowser.open('https://www.google.com/chrome/')
 
def chromedev():
 webbrowser.open('https://www.google.com/chrome/dev/')
 
def chromebeta():
 webbrowser.open('https://www.google.com/chrome/beta/')
 
def chromecanary():
 webbrowser.open('https://www.google.com/chrome/canary/')

def coccoc():
 webbrowser.open('https://coccoc.com/')
 
def cent():
 webbrowser.open('https://www.centbrowser.com/')

def comododragon():
 webbrowser.open('https://www.comodo.com/home/browsers-toolbars/browser.php')

def comodoicedragon():
 webbrowser.open('https://www.comodo.com/home/browsers-toolbars/browser.php')

def cyberfox():
 webbrowser.open('https://sourceforge.net/projects/cyberfox/')

def dot():
 webbrowser.open('https://www.dothq.co/en')
 
def eldy():
 webbrowser.open('http://www.eldy.eu/en/software/download/')
 
def firefox():
 webbrowser.open('https://www.mozilla.org/en-US/firefox/new/')
 
def firefoxbeta():
 webbrowser.open('https://www.mozilla.org/en-US/firefox/channel/desktop/')
 
def firefoxdev():
 webbrowser.open('https://www.mozilla.org/en-US/firefox/channel/desktop/')
 
def firefoxnightly():
 webbrowser.open('https://www.mozilla.org/en-US/firefox/channel/desktop/')
 
def falkon():
 webbrowser.open('https://www.falkon.org/')

def ghost():
 webbrowser.open('https://ghostbrowser.com/')

def librewolf():
 webbrowser.open('https://librewolf.net/')

def maxthon():
 webbrowser.open('https://www.maxthon.com/mx6/download/')

def maxthonbeta():
 webbrowser.open('https://www.maxthon.com/mx6/beta/')

def maxthonnitro():
 webbrowser.open('https://www.maxthon.com/nitro/static.html')

def maxthonclassic():
 webbrowser.open('https://www.mediafire.com/file/g764bdkhacu90w4/MAXTHON_CLASSIC_mx_1.6.7.34.exe/file')

def midori():
 webbrowser.open('https://astian.org/en/midori-browser-desktop/')

def superbrowse():
 webbrowser.open('https://superbrowse.en.uptodown.com/windows')
 
def sidekick():
 webbrowser.open('https://www.meetsidekick.com/')
 
def tor():
 webbrowser.open('https://www.torproject.org/')
 
def seamonkey():
 webbrowser.open('https://www.seamonkey-project.org/releases/')
 
def tungsten():
 webbrowser.open('https://en.tungsten-start.net/')
 
def palemoon():
 webbrowser.open('https://www.palemoon.org/')
 
def otter():
 webbrowser.open('https://otter-browser.org/')
 
def opera():
 webbrowser.open('https://www.opera.com/browsers/opera')
 
def operabeta():
 webbrowser.open('https://www.opera.com/browsers/opera/beta')
 
def operadev():
 webbrowser.open('https://www.opera.com/browsers/opera/beta')
 
def operacrypto():
 webbrowser.open('https://www.opera.com/crypto/next/')
 
def operagx():
 webbrowser.open('https://www.opera.com/gx')
 
def minbrowser():
 webbrowser.open('https://minbrowser.org/')
 
def pulse():
 webbrowser.open('https://pulsebrowser.app/')

def waterfox():
 webbrowser.open('https://www.waterfox.net/')
 
def whale():
 webbrowser.open('https://whale.naver.com/en/')

def wyzo():
 webbrowser.open('https://wyzo.en.uptodown.com/windows')
 
def yandex():
 webbrowser.open('https://browser.yandex.com/')
 
def vivaldi():
 webbrowser.open('https://vivaldi.com/')
  
def citrio():
 webbrowser.open('https://citrio.com/')
 
def osiris():
 webbrowser.open('https://decenternet.net/osiris')
 
def avant():
 webbrowser.open('http://www.avantbrowser.com/')
 
def avastbrowser():
 webbrowser.open('https://www.avast.com/secure-browser#pc')
 
def ghostlie():
 webbrowser.open('https://sourceforge.net/projects/ghostlie/')
 
def lightfirefox():
 webbrowser.open('https://sourceforge.net/projects/lightfirefox/')
 
def briskbard():
 webbrowser.open('https://www.briskbard.com/index.php?lang=en&pageid=featweb')
 
def chedot():
 webbrowser.open('https://landing.chedot.com/')

def chromodo():
 webbrowser.open('https://help.comodo.com/topic-72-1-623-7595-.html#cd_starting')
 
def bittube():
 webbrowser.open('https://bittube.app/')
 
def cryptotab():
 webbrowser.open('https://cryptobrowser.site/en/')
 
def operaneon():
 webbrowser.open('https://www.opera.com/browsers/neon')
 
def urbrowser():
 webbrowser.open('https://www.ur-browser.com/en-US')
 
def viasat():
 webbrowser.open('https://browser.viasat.com/')
 
def kinza():
 webbrowser.open('https://www.kinza.jp/en/')
 
def sleipnir():
 webbrowser.open('https://www.fenrir-inc.com/jp/sleipnir/')

def slimjet():
 webbrowser.open('https://www.slimbrowser.net/en/dlpage.php')
 
def qutebrowser():
 webbrowser.open('https://github.com/qutebrowser/qutebrowser')
 
def abrowser():
 webbrowser.open('https://sourceforge.net/projects/abrowser/')
 
def iridium():
 webbrowser.open('https://iridiumbrowser.de/')

def airbrowse():
 webbrowser.open('https://sourceforge.net/projects/airbrowse3/')
 
def slimboat():
 webbrowser.open('https://slimboat.en.softonic.com/')

def kingpin():
 webbrowser.open('https://kingpinbrowser.com/') 

def avgbrowser():
 webbrowser.open('https://www.avg.com/en-us/secure-browser#pc') 

def arora():
 webbrowser.open('https://arora.en.softonic.com/download')

################## CONFIG

config = Menu(menubar, tearoff=0)
config.add_command(label = 'exit', command = close)
config.add_command(label = 'github', command = github)

################## A

abrowsers = Menu(menubar, tearoff=1)
abrowsers.add_command(label = 'abrowser', command = abrowser)
abrowsers.add_command(label = 'airbrowse', command = airbrowse)
abrowsers.add_command(label = 'arora', command = arora)
abrowsers.add_command(label = 'avg browser', command = avgbrowser)
abrowsers.add_command(label = 'avant', command = avant)
abrowsers.add_command(label = 'avast browser', command = avastbrowser)

################## B

bbrowsers = Menu(menubar, tearoff=1)
bbrowsers.add_command(label = 'baidu', command = baidu)
bbrowsers.add_command(label = 'basilisk', command = basilisk)
bbrowsers.add_command(label = 'beaker', command = beaker)
bbrowsers.add_command(label = 'bittube', command = bittube)
bbrowsers.add_command(label = 'blisk', command = blisk)
bbrowsers.add_command(label = 'brave', command = brave)
bbrowsers.add_command(label = 'brave beta', command = bravebeta)
bbrowsers.add_command(label = 'brave nightly', command = bravenightly)
bbrowsers.add_command(label = 'briskbard', command = briskbard)

################## C

cbrowsers = Menu(menubar, tearoff=1)
cbrowsers.add_command(label = 'cent', command = cent)
cbrowsers.add_command(label = 'chedot', command = chedot)
cbrowsers.add_command(label = 'chrome', command = chrome)
cbrowsers.add_command(label = 'chrome beta', command = chromebeta)
cbrowsers.add_command(label = 'chrome canary', command = chromecanary)
cbrowsers.add_command(label = 'chrome dev', command = chromedev)
cbrowsers.add_command(label = 'chromodo', command = chromodo)
cbrowsers.add_command(label = 'citrio', command = citrio)
cbrowsers.add_command(label = 'coc coc', command = coccoc)
cbrowsers.add_command(label = 'comodo dragon', command = comododragon)
cbrowsers.add_command(label = 'comodo ice dragon', command = comodoicedragon)
cbrowsers.add_command(label = 'cryptotab', command = cryptotab)
cbrowsers.add_command(label = 'cyberfox', command = cyberfox)

################## D

dbrowsers = Menu(menubar, tearoff=1)
dbrowsers.add_command(label = 'dot', command = dot)

################## E

ebrowsers = Menu(menubar, tearoff=1)
ebrowsers.add_command(label = 'eldy', command = eldy)

################## F

fbrowsers = Menu(menubar, tearoff=1)
fbrowsers.add_command(label = 'falkon', command = falkon)
fbrowsers.add_command(label = 'firefox', command = firefox)
fbrowsers.add_command(label = 'firefox beta', command = firefoxbeta)
fbrowsers.add_command(label = 'firefox dev', command = firefoxdev)
fbrowsers.add_command(label = 'firefox nightly', command = firefoxnightly)

################## G

gbrowsers = Menu(menubar, tearoff=1)
gbrowsers.add_command(label = 'ghost', command = ghost)
gbrowsers.add_command(label = 'ghostlie', command = ghostlie)

################## H

hbrowsers = Menu(menubar, tearoff=1)

################## I

ibrowsers = Menu(menubar, tearoff=1)
ibrowsers.add_command(label = 'iridium', command = iridium)

################## J

jbrowsers = Menu(menubar, tearoff=1)

################## K

kbrowsers = Menu(menubar, tearoff=1)
kbrowsers.add_command(label = 'kingpin', command = kingpin)
kbrowsers.add_command(label = 'kinza', command = kinza)

################## L

lbrowsers = Menu(menubar, tearoff=1)
lbrowsers.add_command(label = 'librewolf', command = librewolf)
lbrowsers.add_command(label = 'light firefox', command = lightfirefox)

################## M

mbrowsers = Menu(menubar, tearoff=1)
mbrowsers.add_command(label = 'maxthon', command = maxthon)
mbrowsers.add_command(label = 'maxthon nitro', command = maxthonnitro)
mbrowsers.add_command(label = 'maxthon beta', command = maxthonbeta)
mbrowsers.add_command(label = 'maxthon (CLASSIC/OLD)', command = maxthonclassic)
mbrowsers.add_command(label = 'midori', command = midori)
mbrowsers.add_command(label = 'min', command = minbrowser)

################## N

nbrowsers = Menu(menubar, tearoff=1)

################## O
obrowsers = Menu(menubar, tearoff=1)
obrowsers.add_command(label = 'opera', command = opera)
obrowsers.add_command(label = 'opera beta', command = operabeta)
obrowsers.add_command(label = 'opera crypto', command = operacrypto)
obrowsers.add_command(label = 'opera dev', command = operadev)
obrowsers.add_command(label = 'opera gx', command = operagx)
obrowsers.add_command(label = 'opera neon', command = operaneon)
obrowsers.add_command(label = 'osiris', command = osiris)
obrowsers.add_command(label = 'otter', command = otter)

################## P

pbrowsers = Menu(menubar, tearoff=1)
pbrowsers.add_command(label = 'palemoon', command = palemoon)
pbrowsers.add_command(label = 'pulse', command = pulse)

################## Q

qbrowsers = Menu(menubar, tearoff=1)
qbrowsers.add_command(label = 'qutebrowser', command = qutebrowser)

################## R

rbrowsers = Menu(menubar, tearoff=1)

################## S

sbrowsers = Menu(menubar, tearoff=1)
sbrowsers.add_command(label = 'seamonkey', command = seamonkey)
sbrowsers.add_command(label = 'sidekick', command = sidekick)
sbrowsers.add_command(label = 'sleipnir', command = sleipnir)
sbrowsers.add_command(label = 'slimboat', command = slimboat)
sbrowsers.add_command(label = 'slimjet', command = slimjet)
sbrowsers.add_command(label = 'superbrowse', command = superbrowse)

################## T

tbrowsers = Menu(menubar, tearoff=1)
tbrowsers.add_command(label = 'tor', command = tor)
tbrowsers.add_command(label = 'tungsten', command = tungsten)

################## U

ubrowsers = Menu(menubar, tearoff=1)
ubrowsers.add_command(label = 'ungoogled chromium', command = ungoogledchromium)
ubrowsers.add_command(label = 'ur browser', command = urbrowser)

################## V

vbrowsers = Menu(menubar, tearoff=1)
vbrowsers.add_command(label = 'vivaldi', command = vivaldi)

################## W

wbrowsers = Menu(menubar, tearoff=1)
wbrowsers.add_command(label = 'waterfox', command = waterfox)
wbrowsers.add_command(label = 'whale', command = whale)
wbrowsers.add_command(label = 'wyzo', command = wyzo)

################## X

xbrowsers = Menu(menubar, tearoff=1)

################## Y

ybrowsers = Menu(menubar, tearoff=1)
ybrowsers.add_command(label = 'yandex', command = yandex)

################## Z

zbrowsers = Menu(menubar, tearoff=1)

################## END

menubar.add_cascade(label = 'config', menu=config)
menubar.add_cascade(label = 'A', menu=abrowsers)
menubar.add_cascade(label = 'B', menu=bbrowsers)
menubar.add_cascade(label = 'C', menu=cbrowsers)
menubar.add_cascade(label = 'D', menu=dbrowsers)
menubar.add_cascade(label = 'E', menu=ebrowsers)
menubar.add_cascade(label = 'F', menu=fbrowsers)
menubar.add_cascade(label = 'G', menu=gbrowsers)
menubar.add_cascade(label = 'H', menu=hbrowsers)
menubar.add_cascade(label = 'I', menu=ibrowsers)
menubar.add_cascade(label = 'J', menu=jbrowsers)
menubar.add_cascade(label = 'K', menu=kbrowsers)
menubar.add_cascade(label = 'L', menu=lbrowsers)
menubar.add_cascade(label = 'M', menu=mbrowsers)
menubar.add_cascade(label = 'N', menu=nbrowsers)
menubar.add_cascade(label = 'O', menu=obrowsers)
menubar.add_cascade(label = 'P', menu=pbrowsers)
menubar.add_cascade(label = 'Q', menu=qbrowsers)
menubar.add_cascade(label = 'R', menu=rbrowsers)
menubar.add_cascade(label = 'S', menu=sbrowsers)
menubar.add_cascade(label = 'T', menu=tbrowsers)
menubar.add_cascade(label = 'U', menu=ubrowsers)
menubar.add_cascade(label = 'V', menu=vbrowsers)
menubar.add_cascade(label = 'W', menu=wbrowsers)
menubar.add_cascade(label = 'X', menu=xbrowsers)
menubar.add_cascade(label = 'Y', menu=ybrowsers)
menubar.add_cascade(label = 'Z', menu=zbrowsers)

root.config(menu = menubar)
root.mainloop()
