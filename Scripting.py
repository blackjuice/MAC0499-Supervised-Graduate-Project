# 170213
# Creating, naming, sizing cubes

Change dimensions
=================
import bpy
from mathutils import Matrix
D = bpy.data
C = bpy.context
scene = C.scene

# add cube
bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 0.0))
# name cube
bpy.context.object.name = "Cube1"
# or do:
#   cube = bpy.context.object
#   cube.name = 'NewName'

# To alter scale. NOTE: scales should always be set to 1.
# bpy.context.object.scale = (2, 0.025, 1.25)

obj = bpy.context.object
current_x, current_y, current_z =  obj.dimensions
obj.dimensions = [0.7, 0.7, current_z]



Resize = original * input value
===============================
import bpy
from mathutils import Matrix
D = bpy.data
C = bpy.context
scene = C.scene

# add cube
bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 0.0))
# name cube
bpy.context.object.name = "Cube1"
# scale to one
bpy.context.object.scale = (1, 1, 1)
# the following takes the original times (*) the input value
bpy.ops.transform.resize(value=(4, .05, 2.5))



Some interesting lines of codes. It shows here switching Modes.
===============================================================
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False},     
TRANSFORM_OT_translate={"value":(0, 0, 30)})
bpy.ops.object.mode_set(mode = 'OBJECT')


Mod UI
======
sources:
* http://blender.stackexchange.com/questions/14354/simple-way-to-add-button-to-ui
