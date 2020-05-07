class defaultdict(dict):
    
    def __init__(self,default=None):
        dict.__init__(self)
        self.default = default  
        
    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self,key)
        else:
            return self.default
        
    def get(self,key,*args):
        if not args:
            args = (self.default,)
        return dict.get(self, key, *args)
        
word_count = defaultdict(default=0)
word_count['Python'] = 1
print(word_count['Java'])
print(word_count.get('Python'))
print(word_count.get('Python',17))
print(word_count.get('Perl',42))
          