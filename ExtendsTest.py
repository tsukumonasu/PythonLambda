#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Tank:
    def __init__(self):
        self.guns = "なし"
        self.turrets = "なし"
        self.suspensions = "なし"
       
    def PrintParts(self):
        print('砲は{}'.format(self.guns))
        print('砲塔は{}'.format(self.turrets))
        print('履帯は{}'.format(self.suspensions))

class LT38(Tank):
    def __init__(self):
        self.guns = "Pz.Kpfw 38(t) Ausf. G"
        self.turrets = "4,7 cm Kw.K. 38 (t) L/43"
        self.suspensions = "Pz.Kpfw 38(t) Ausf. E"

class Hetzer(LT38):
    def __init__(self):
        self.guns = "10.5 cm Stu.H. 42 L/28"
        self.turrets = "ヘッツァー改装キット"
        self.suspensions = LT38().suspensions
    
if __name__ == '__main__':
    Tank().PrintParts()
    LT38().PrintParts()
    Hetzer().PrintParts()
    
    
    