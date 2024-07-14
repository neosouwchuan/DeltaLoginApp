
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
from datetime import datetime
from datetime import date
import qrcode
from os.path import join
from kivy.uix.screenmanager import ScreenManager, Screen
# Create the manager
sm = ScreenManager()

from kivy import kivy_home_dir
from os.path import join
store = JsonStore(join(kivy_home_dir, 'highscore.json'))
sm.add_widget(Screen(name='tipscreen1'))
sm.add_widget(Screen(name='tipscreen2'))
class MainApp(MDApp):
  def callback(self,sm):
  
    sm.current = "tipscreen2"
  def build(self):

    #store.put("perm",digit = "2207",date = date.today().strftime("%m%d%y"))
    #sm = ScreenManager(transition = RiseInTransition())
    #sm.add_widget(MenuScreen(name ="screen_one"))
    
    #sm.add_widget(SettingsScreen(name ="screen_two"))
    self.theme_cls.theme_style="Dark"
    self.theme_cls.primary_palette="BlueGray"
    
    #if store.exists("perm"):
      #store.delete('perm')


    return Builder.load_file("login.kv")
  def on_start(self):
    
    self.fps_monitor_start() 
    if store.exists("perm"):
      self.root.ids.screen_manager.current = "tipscreen2"
      digit = store.get("perm")["digit"]
      self.root.ids.generate_label.text = f"ID:{digit}"
  def logger(self):
    #print(self.root.ids.user.text)
    self.root.ids.welcome_label.text = f"Sup{self.root.ids.user.text}"
    self.root.ids.user.text = self.root.ids.user.text.replace(" ","")
    if self.root.ids.user.text!="":
      store.put("perm",digit = self.root.ids.user.text,date = date.today().strftime("%m%d%y"))
    self.root.ids.screen_manager.current = "tipscreen2"
    self.root.ids.generate_label.text = f"ID:{self.root.ids.user.text}"
  def qrgen(self):
    digit = store.get("perm")["digit"]
    self.root.ids.generate_label.text = f"ID:{digit}"
    startdate = store.get("perm")["date"]
    currtime = datetime.now().strftime("%H%M%S")
    print(startdate)
    code = digit + startdate+currtime
    temp = ""
    running = 0
    for i in code:
      temp = temp +str((running+int(i))%10)
      running += int(i)
    print(code)
    code = temp
    img = qrcode.make(code)
  
    img.save("qrcode.png")
    self.root.ids.oneimage.source = "qrcode.png"
    self.root.ids.oneimage.reload()
sample = MainApp()
sample.run()

# MDTopAppBar:
#     id: toolbar
#     right_action_items: [["cog", lambda x: app.callback(x)]]2441178914437814
