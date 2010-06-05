import cream
from cream.contrib.notifications import FrontendManager

class ManagerModule(cream.Module, FrontendManager):
    def __init__(self):
        cream.Module.__init__(self)
        FrontendManager.__init__(self)

if __name__ == '__main__':
   manager = ManagerModule()
   manager.main()
