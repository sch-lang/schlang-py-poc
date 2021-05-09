class SymbolTable:
    symbols = {}

    def add(self, indentifier, symbol):
        self.symbols[indentifier] = symbol
    
    def get(self, indentifier):
        if (self.has(indentifier)):
            return self.symbols[indentifier]

        return False

    def has(self, indentifier):
        return indentifier in self.symbols