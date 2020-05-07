from contextlib import ContextDecorator
    
class mycontext(ContextDecorator):
    def __init__(self,tag):
        ContextDecorator.__init__(self)
        self.__tag__ = tag
        
    def __enter__(self):
        print('<'+self.__tag__+'>')
        return self

    def __exit__(self,*exec):
        print('</'+self.__tag__+'>')
        return False
        
        
with mycontext('h1'):
     print('My string!')    
