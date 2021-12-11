import maya.cmds as cmds
import maya.OpenMaya as om

from . import get
from . import create
from . import check
from . import set

class Func(get.Get,create.Create,check.Check,set.Set):
    
    @classmethod
    def constraint(self,type_const):
        
        
        
        list_selected = cmds.ls(sl=True,long=True)
        child_const = self.get_child_const(list_selected)
        parents_const = self.get_parentsname_const(list_selected)
        
        
        if type_const == "parent":
            name_const = cmds.parentConstraint(parents_const,child_const,mo=True,weight = 1)
        elif type_const == "orient":
            name_const = cmds.orientConstraint(parents_const,child_const,mo=True,weight = 1)
        else:
            name_const = cmds.pointConstraint(parents_const,child_const,mo=True,weight = 1)
        
        cmds.refresh(f=True)
        
        space_attr = self.get_attrname("Space_"+type_const,child_const)
        boole_nameattr = self.check_nameattr("Space_"+type_const,child_const)
        
        if boole_nameattr:
            return_add_info = self.add_constraint(space_attr[0],parents_const,child_const,type_const)
            nameenum_list = return_add_info[0]
            full_nameattrs_const = return_add_info[1]
        else:
            nameenum_list = self.create_spaceattribute(parents_const,child_const,type_const)
            name_const = self.get_longname(child_const,self.get_absolutename(name_const[0]))
            attrs_const = self.get_attrconstraint(parents_const,name_const)
            full_nameattrs_const = self.get_full_attrname(name_const,attrs_const)
        
        full_nameattrs_const = self.get_correct_full_nameattrs_const(full_nameattrs_const,nameenum_list)
        self.set_keyframeconst(full_nameattrs_const,space_attr[0],nameenum_list)
    
    @classmethod
    def add_constraint(self,namespace_attr,objs_parent,obj,type_const):
        
        name_constraint = self.get_nameconstraint(self.get_absolutename(obj),type_const)
        name_constraint = self.get_longname(obj,self.get_absolutename(name_constraint))
        list_nameenum = self.get_enumname(obj,type_const)
        list_definedattr = self.get_all_attrconstraint(name_constraint)
        full_nameattrs_const = self.get_full_attrname(name_constraint,list_definedattr)
        
        list_correctparent = self.get_correct_parent(list_nameenum,objs_parent)

        for correctparent in list_correctparent:
            if not correctparent in list_nameenum:
                list_nameenum.append(correctparent)
        self.set_newparent_to_enum(list_nameenum,namespace_attr)
        
        return [list_nameenum,full_nameattrs_const]
        
    