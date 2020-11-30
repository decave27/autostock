class Stock:
    def __init__(self, name=None, up=None, no=None, old=None, history=None):
        self.name = name
        self.up = up
        self.now = now
        self.old = old
        self.history = history
        if old < now:
            self.text = f'+ {self.name} {self.now} ( ▲ {self.now - self.old} )\n'
        elif old > now:
            self.text += f'- {self.name} {self.now} ( ▼ {self.old - self.now} )\n'
        elif old == now:
            self.text += f'~ {self.name} {self.now} ( ~ 0 )\n'
    def __repr__(self) -> str:
        return f"<Stock name={self.name} up={self.up} now={self.now} old={self.old} >"
    def plus(self):
        self.plus.text = "+"
        return
    def middle(self):
        self.middle.text = "~"
        return
    def down(self):
        self.down.text = "-"
        return
