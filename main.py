from search import Search
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Input, Static
from textual.containers import Horizontal, VerticalScroll

class App(App):
    """A Textual app for searching the web in the terminal"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("q", "quit", "Quit")]

    CSS_PATH="main.tcss"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header(show_clock=True, icon="🔍")
        yield Footer()
        yield Horizontal(
            VerticalScroll(
                Input(placeholder="Enter search query", id="search-input"),
                Button("Search", id="search-button", variant="primary"),
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = App()
    app.run()
