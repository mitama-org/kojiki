from mitama.app import App, Router
from mitama.utils.controllers import static_files
from mitama.app.method import view

from .controller import WelcomeController


class App(App):
    name = '今事記'
    description = 'コジキって読むよ。'
    router = Router(
        [
            view("/", HomeController),
            view("/static/<path:path>", static_files()),
        ]
    )
