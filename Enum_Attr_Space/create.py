import maya.cmds as cmds
from . import get

class Create(get.Get):
    
    @classmethod
    def create_spaceattribute(cls,longnameattr,obj,type_const):
        
        enum_str = "{0}_Itself:".format(cls.get_absolutename(obj))
        
        for name_attr in longnameattr:
            enum_str+=cls.get_absolutename(name_attr)+":"
            
        cmds.addAttr(obj,ln="Space_"+type_const,at="enum",en=enum_str,keyable=True)
        
        enum_list = enum_str.split(":")
        del enum_list[-1]
        return enum_list