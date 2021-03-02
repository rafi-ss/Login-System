from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from popupfile import OurPopup, LogininPopup

Builder.load_file('main.kv')
Builder.load_file('popupdesign.kv')

class RegistrationScreen(Screen):
    def registerUser(self):
        uname = self.ids.username.text
        passwd = self.ids.password.text
        confirm_pass = self.ids.confirm_password.text
        
        if uname != "" and passwd != "" and passwd == confirm_pass:
            f = open("users.txt", "a")
            f.write(uname+"#"+passwd+"\n")
            f.close()

            p = OurPopup()
            p.open()

    def goToLoginScreen(self):
        self.manager.current = "login"


class loginScreen(Screen):

    def checklogin(self):
        input_user = self.ids.username.text
        input_pass = self.ids.password.text

        checker = False

        f = open("users.txt", 'r')
        for user in f:
            p = user.split('#')

            uname = p[0]
            passwd = p[1][0:len(p[1])-1]

            if uname == input_user and passwd == input_pass:
                checker = True
                self.manager.current = 'menu'

        if checker == False:
            pop = LogininPopup()
            pop.open()

    def goToRegisterPage(self):
        self.manager.current = 'register'

class MenuScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(RegistrationScreen(name='register'))
sm.add_widget(loginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))


class MyApp(App):
    def build(self):
        return sm


if __name__== '__main__':
    MyApp().run()