import maya.cmds as cmds

from .get import GET

class Init():
    
    selected = cmds.ls(sl=True,long=True)
    main_obj = GET.get_mainjnt(selected)
        
    