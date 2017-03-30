# 170329
# source: 
#     http://blender.stackexchange.com/questions/19249/simplify-blender-gui-using-python
# panel removal script test
# location: C:\Users\USER\AppData\Roaming\Blender Foundation\Blender\2.77\scripts\startup

import bpy
for pt in bpy.types.Panel.__subclasses__():
    if pt.bl_space_type == 'VIEW_3D':
        if "bl_rna" in pt.__dict__:   # <-- check if we already removed!
            bpy.utils.unregister_class(pt)