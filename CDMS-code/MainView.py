import NavigationView as navigation
import testView as testview

def Main():
    testview.TestView.login()
    while True:
        navigator.mainMenu()

navigator = navigation.Navigator()
Main()