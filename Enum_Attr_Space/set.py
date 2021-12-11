import maya.cmds as cmds

class Set():
    
    @classmethod
    def set_keyframeconst(cls,full_nameattrs_const,space_attr,nameenum_list):
        
        for index,nameenum in enumerate(nameenum_list):
            
            cmds.setAttr(space_attr,index)
            for nameattr_const in full_nameattrs_const:
                if nameenum in nameattr_const:
                    cmds.setAttr(nameattr_const,1)
                else:
                    cmds.setAttr(nameattr_const,0)
        
                cmds.setDrivenKeyframe(nameattr_const,currentDriver=space_attr)
    
    @classmethod    
    def set_newparent_to_enum(self,list_nameenum,namespace_attr):
        
        enum_str=""
        for nameenum in list_nameenum:
            enum_str+=nameenum+":"
        cmds.addAttr(namespace_attr,e=True,en=enum_str,keyable=True)
          