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

bl_info = {
  "name": "ForensicFR",
  "description": "3D Forensic Facial Reconstruction",
  "author": "Lucas Sung Jun Hong",
  "version": (0, 0),
  "blender": (2, 72, 0),
  "location": "Tool Shelf",
  "warning": "", # used for warning icon and text in add-ons panel
  "wiki_url": "http://my.wiki.urlhttps://github.com/blackjuice/MAC0499-Supervised-Graduate-Project",
  "tracker_url": "",
  "support": "",
  "category": "ForensicFR"
  }

import bpy

#
# Add additional functions here
#

def register():
  from . import properties
  from . import ui
  properties.register()
  ui.register()

def unregister():
  from . import properties
  from . import ui
  properties.unregister()
  ui.unregister()

if __name__ == '__main__':
  register()
