# Blender Add-on Template
# Contributor(s): Lucas Sung Jun Hong (lucas.sj.hong@gmail.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Panel

#
# Add additional functions here
#

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

def register():
  bpy.utils.register_class(MyPanel)

def unregister():
  bpy.utils.unregister_class(MyPanel)
