class Park:
    def __init__(self, sor: str):
        darabolt = sor.strip().split('@')
        self.ev = int(darabolt[0])
        self.helyTipus = int(darabolt[1])
        self.latogatas = int(darabolt[2])
        self.atlagLatogatas = float(darabolt[3].replace(",", "."))


