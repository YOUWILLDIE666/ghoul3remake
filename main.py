import random as m
import sys
from time import sleep as wait
from tkinter.filedialog import askdirectory as adir
from tkinter.messagebox import showerror as e

import requests

l = 'https://usaupload.com/77ul/Ghouls_Forest.7z?download_token=213df1a6b3bf921aedf494134cd45feee5b3510fda7bae9bb555acd2f24a6626'
dic = adir()
f = f'{dic}/Ghouls Forest.7z'

spectrum = ['@','#','$','%','&','*','/','|','X']
if __name__ == '__main__':
  if dic:
      with open(f,'wb') as f:
          print('Downloading Ghouls Forest.7z')
          response = requests.get(l,stream=True)
          tl = response.headers.get('content-length')
  
          if tl is None:
              f.write(response.content)
              exit('Error: incorrect url (?)')
          else:
              dl = 0
              tl = int(tl)
              for data in response.iter_content(chunk_size=4096):
                  dl += len(data)
                  f.write(data)
                  done = int(50*dl/tl)
                  sys.stdout.write('\r[%s%s]'%(m.choice(spectrum)*done,' '*(50-done)))
                  sys.stdout.flush()
  else:
      e('progra~1', 'NO DIR SELECTED')
      exit('Error: no dir selected')
  print(f'\nSuccess\n\nControls: WASD - walk\nSpace - jump\nGender - Object\n\nHave fun')
  wait(10)
