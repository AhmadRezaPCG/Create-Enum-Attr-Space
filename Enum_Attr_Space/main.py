import maya.cmds as cmds

from .func import Func

class Main(Func):
     
    @classmethod
    def CRConstKey(self,type_const = "parent"):
        self.constraint(type_const)
