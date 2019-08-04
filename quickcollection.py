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
    buttonNumber = 20
    
   
    @classmethod
    def poll(cls, context):
        ob = context.object
        return ob
   
    def setup(self, context):
        buttons = []
        counter = 1
        
        # Amount of buttons
        for i in range(self.buttonNumber):
            button = self.gizmos.new("GIZMO_GT_button_2d")
            buttons.append(button)
           
        for button in buttons:
            button.icon = 'BLANK1'
            button.draw_options = {'BACKDROP', 'OUTLINE'}
 
            #button.alpha = 0.0
            button.color = 0.5,0.5,0.5
            button.alpha_highlight = 1
           
            promp = button.target_set_operator("object.hide_collection")
            promp.collection_index = counter
            promp.toggle = True
           
           # but size. if changed draw_prepare "runningoffset" needs adjustment
            button.scale_basis = 3 
            counter = counter + 1
           
        self.buttonsfoo = buttons
 
    def draw_prepare(self, context):
        region = context.region
        lButtons = self.buttonsfoo
        coll = context.view_layer.layer_collection.children
        
        perRow = 5
        offsetwidth = 0
        offsetheight = 0
        runningoffset = 7
       
        counter = 0
        for but in lButtons:
            
            if counter%perRow == 0 and counter != 0:
                offsetheight = runningoffset
                
            if counter == len(lButtons)/2:
                # probably if more buttons are added. the + perRow needs to be multiplied 
                offsetwidth = perRow * runningoffset + perRow
                offsetheight = 0
                
            but.matrix_basis[0][3] = (region.width/2) + offsetwidth + ((counter%perRow) * runningoffset)
            but.matrix_basis[1][3] = (region.height - 33) - offsetheight
                
            counter = counter +1
            
        # Might be a performance hog. 
        collCounter = 0
        for c in coll:
            if c.is_visible == False:
                lButtons[collCounter].color = 0.1,0.1,0.1
            if c.is_visible == True:
                lButtons[collCounter].color = 0.5,0.5,0.5
                
            collCounter = collCounter + 1
       
bpy.utils.register_class(QuickCollectionManager)