class DSU:
    def __init__(self):
        self.mapping = {}
    
    def find(self, i):
        if i not in self.mapping:
            self.mapping[i] = i
        a = self.mapping[i]
        if a != i and a in self.mapping:
            self.mapping[i] = self.find(a)
        return self.mapping[i]
        
    def merge(self, i, j):
        a, b = self.find(i), self.find(j)
        if a < b:
            self.mapping[b] = self.mapping[a]
        else:
            self.mapping[a] = self.mapping[b]