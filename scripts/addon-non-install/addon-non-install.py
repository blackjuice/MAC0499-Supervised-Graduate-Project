# 

#-------------------------------------------------------------------------
# remove panels

import bpy
for pt in bpy.types.Panel.__subclasses__():
    if pt.bl_space_type == 'VIEW_3D':
        if "bl_rna" in pt.__dict__:   # <-- check if we already removed!
            bpy.utils.unregister_class(pt)

#-------------------------------------------------------------------------
# create panel

import bpy
from bpy.types import Panel

# Class for panel
class SimpleToolPanel(Panel):
  bl_space_type   = 'VIEW_3D'
  bl_region_type  = 'TOOLS'
  bl_label        = 'Tools Tab Label'
  bl_context      = 'objectmode'
  bl_category     = 'ForensicFR'

  # UI elements
  def draw(self, context):
    layout = self.layout
    layout.operator('mesh.primitive_cube_add', text = 'Add new cube')

# Register
def register():
  bpy.utils.register_class(SimpleToolPanel)

# Unregister
def unregister():
  bpy.utils.unregister_class(SimpleToolPanel)

# run script
if __name__ == '__main__':
  register()