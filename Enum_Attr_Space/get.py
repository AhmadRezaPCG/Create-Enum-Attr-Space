    
import maya.cmds as cmds
import maya.OpenMaya as om

class Get():
    
    @classmethod
    def get_child_const(cls,list_selected=[]):
        
        if not len(list_selected)>0:
            om.MGlobal.displayError("Your selected list is empty.")
            return None
            
        return list_selected[-1]
        
    @classmethod
    def get_parentsname_const(cls,list_selected=[]):
        
        if not len(list_selected)>1:
            om.MGlobal.displayError("Your selected are not enouth.")
            return None
            
        del list_selected[-1]
        return list_selected
        
    @classmethod
    def get_longname(cls,parent,child):
        
        return "{0}|{1}".format(parent,child)
        
    @classmethod
    def get_absolutename(cls,name):
        
        name_split = name.split("|")
        return name_split[-1]
        
    @classmethod
    def get_attrconstraint(cls,parents_name,const_name):
        
        attrs_const = cmds.listAttr(const_name,keyable=True,userDefined=True)
        parents_name_new = [cls.get_absolutename(x) for x in parents_name]
        
        if type(parents_name) != type([]):
            
            for attr_const in attrs_const:
                if parents_name in attr_const:
                    return [parents_name]
        else:
            list_attrs_constraint = []
            
            for attr_const in attrs_const:
                for parent_name in parents_name_new: 
                    if parent_name in attr_const :
                        list_attrs_constraint.append(attr_const)
                    
            return list_attrs_constraint
    
    @classmethod        
    def get_full_attrname(cls,object_name,attr_name):
        
        list_full_nameattrs = []
        if type(attr_name) == type([]):
            
            for attr in attr_name :
                list_full_nameattrs.append("{0}.{1}".format(object_name,attr))
            return list_full_nameattrs
            
        else:
            return ["{0}.{1}".format(object_name,attr_name)]
                
    
    @classmethod
    def get_attrname(cls,nameattr,nameobj):
        
        if type(nameattr) == type([]):
            name_attrs = []
            for attr in nameattr:
                name_attrs.append("{0}.{1}".format(nameobj,attr))
        
            return name_attrs
        
        else:
            return ["{0}.{1}".format(nameobj,nameattr)]
    
    @classmethod
    def get_nameconstraint(cls,obj,type_const):
        
        return "{0}_{1}Constraint1".format(obj,type_const)
        
    
    @classmethod
    def get_enumname(cls,obj,type_const):
        
        enum_string = cmds.addAttr("{0}.Space_{1}".format(obj,type_const),q=True,en=True)
        enum_list = enum_string.split(":")
        return enum_list
        
    @classmethod
    def get_all_attrconstraint(cls,obj):
        
        return cmds.listAttr(obj,keyable=True,userDefined=True)
        
    @classmethod
    def get_namecorrectattr(cls,more_attr,less_attr):
        
        correct_name = []
        
        for less in less_attr:
            for more in more_attr:
                if less in more:
                    correct_name.append(more)
        return correct_name
        
    @classmethod
    def get_correct_parent(cls,listcheck,forchecks):
        
        is_checked = []
        
        for forcheck in forchecks:
            for checker in listcheck:
                if cls.get_absolutename(forcheck) in checker:
                    continue
                else:
                    is_checked.append(cls.get_absolutename(forcheck))
                    break
                    
        return is_checked
    
    @classmethod
    def get_correct_full_nameattrs_const(cls,full_nameattrs_const,nameenum_list):
        
        correct_const = []
        
        for name_const in full_nameattrs_const:
            for nameenum in nameenum_list:
                if nameenum in name_const:
                    correct_const.append(name_const)
                    
        return correct_const