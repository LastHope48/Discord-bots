class Car:
    def __init__(
            self,
            renk: str | tuple[int, int, int],
            marka: str
        ):

        self.renk = renk
        self.marka = marka

    def info(self):
        return f"Renk: {self.renk}\nMarka: {self.marka}"

    def __str__(self):
        return f"Renk: {self.renk}\nMarka: {self.marka}"
