
class automata:
    def __init__(self, language):
        self.language = language
        self.result = ""
        self.machines = {'m1':['m1','m2'],'m2':['m3','m2'],'m3':['m2','m2']}

    def add_machine():
        pass

    def __str__(self):
        return 'finished'

if __name__=='__main__':
    automata('01000101')