import random
import webbrowser 
import keyboard

def on_enter(event):
  alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #all simbols
  #generation rnd url
  if event.name == 'enter':
    a = ''
    for i in range(4):
      a += str(random.choice(alf))
    b = "https://clck.ru/"+ str(random.randint(30, 39)) + a #random link
    keyboard.send('ctrl+w') #close the tab
    webbrowser.open(b) #open new rnd tab
    
keyboard.on_press(on_enter)


keyboard.wait('esc') #stop the code