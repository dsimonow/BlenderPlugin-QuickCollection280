# Script by https://github.com/dsimonow
# Quick Collection Overlay for Blender
# Free to use 
# For now just CopyPaste it in the Scripting Tab and Run it

import bpy
from bpy.types import (
    GizmoGroup,
)
 
class QuickCollectionManager(GizmoGroup):
    bl_idname = "QuickCollection"
    bl_label = "QuickCollection"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'PERSISTENT', 'SCALE'}
   
    @classmethod
    def poll(cls, context):
       
        ob = context.object
        return ob
   
    def setup(self, context):
        buttons = []
        counter = 1
        for i in range(16):
            button = self.gizmos.new("GIZMO_GT_button_2d")
            buttons.append(button)
           
        for button in buttons:
            button.icon = 'BLANK1'
            button.draw_options = {'BACKDROP', 'OUTLINE'}
 
            #button.alpha = 0.0
            button.color = 0.5,0.5,0.5
            button.color_highlight = 0.8, 0.8, 0.8
            button.alpha_highlight = 1
           
            promp = button.target_set_operator("object.hide_collection")
            promp.collection_index = counter
            promp.toggle = True
           
           
            #drawselect = button.draw
            button.scale_basis = 3 # Same as buttons defined in C
            counter = counter + 1
           
        self.buttonsfoo = buttons
 
    def draw_prepare(self, context):
        region = context.region
        lButtons = self.buttonsfoo
       
        counter = 0
        i = 0
        j = 0
        for but in lButtons:
            but.matrix_basis[0][3] = (region.width / 2 )+j + (counter%4 * 7)
            but.matrix_basis[1][3] = region.height - 33 - i
            counter = counter + 1
           
            if counter%4 == 0 and j == 5*7 and i == 0:
                i = 7
            if counter%4 == 0 and i == 7 and j == 0:
                j = 5*7
                i = 0
            if counter%4 == 0 and i == 0 and j == 0:
                i = 7    
    def invoke_prepare(self,context, gizmo):
        lButtons = self.buttonsfoo
        gizmoIndex = lButtons.index(gizmo)
        coll = context.view_layer.layer_collection.children
       
        if not (gizmoIndex > len(coll)):
            if coll[gizmoIndex].is_visible == True:
                lButtons[gizmoIndex].color = 0.1,0.1,0.1
            if coll[gizmoIndex].is_visible == False:
                lButtons[gizmoIndex].color = 0.5,0.5,0.5
       
bpy.utils.register_class(QuickCollectionManager)