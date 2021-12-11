import maya.cmds as cmds

class Check():
    
    @classmethod
    def check_nameattr(cls,nameattr,nameobj):
        
        if cmds.attributeQuery(nameattr,node = nameobj,exists=True):
            return True
        else:
            return False