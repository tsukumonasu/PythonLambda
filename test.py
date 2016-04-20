# -*- coding: utf-8 -*- 

from abc import ABCMeta, abstractmethod, abstractproperty

class TankInterface(object, metaclass=abc.ABCMeta):
    
    @abstractproperty
        def name(self):
            pass
            


# if __name__ == "__main__":

#     classList    =    []
#     classList.append(TankInterface(1,"テスト１"))
#     classList.append(TankInterface(2,"テスト２"))

#     for value in classList:
#         print "===== class ====="
#         print "code --> " + str(value.code)
#         print "name --> " + value.name
