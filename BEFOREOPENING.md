# before opening tvalist.pyw:
(windows)


if you don't have python installed, install it here: https://www.python.org/downloads/
after installing, you will be able to run .py files and .pyw files, if not, you will need to click in "open with", when you installed python it should have said where it was going to install, go to that directory using "open with" and assign .py files with python and .pyw files with pythonw.

after that, you open/run/execute tvalist.pyw, it wont run because in line 9 there is:

img = PhotoImage( fil = 'DIRECTORY\\\tvalist.png')

this defines the icon of the window, if you want you can comment it ( #abc ) it to remove the icon, or you can go to where you downloaded it and get the directory, it should be something similar to this:

D:\yourname\paste1\paste2\tvalist

\* the D: can be another letter

\* "yourname" it's the name of your user

\* "paste1" can be downloads, documents, desktop etc and doesn't need to be 2 pastes

after that, edit like this:

D:\\\yourname\\\paste1\\\paste2\\\tvalist

then, paste it in DIRECTORY:

img = PhotoImage( fil = 'D:\\\yourname\\\paste1\\\paste2\\\tvalist\\\tvalist.png')

save it and you are done!
