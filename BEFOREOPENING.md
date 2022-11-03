# before opening wbc.pyw:
when you open/run/execute wbc.pyw, it wont run because in line 9 there is:

img = PhotoImage( fil = 'DIRECTORY\\\wbc.png')

this defines the icon of the window, if you want you can comment it ( #abc ) it to remove the icon, or you can go to where you downloaded it and get the directory, it should be something similar to this:

D:\yourname\paste1\paste2\wbc

\* the D: can be another letter

\* "yourname" it's the name of your user

\* "paste1" can be downloads, documents, desktop etc and doesn't need to be 2 pastes

after that, edit like this:

D:\\\yourname\\\paste1\\\paste2\\\wbc

then, paste it in DIRECTORY:

img = PhotoImage( fil = 'D:\\\yourname\\\paste1\\\paste2\\\wbc\\\wbc.png')

save it and you are done!
