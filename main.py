from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgageCalculator(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Mortgage Calculator", halign="center")


MortgageCalculator().run()