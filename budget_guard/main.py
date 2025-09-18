import flet as ft
from datetime import date

def main(page: ft.Page):
    page.title = "Home budget guard"
    page.add(ft.Text("Welcome to our budget guard app, hope you'll like it!"))


ft.app(target=main)
