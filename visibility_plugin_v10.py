bl_info = {
    "name":"Visibility Animation Plugin",
    "author":"David Cai",
    "version":(1,0),
    "blender":(2,90,0),
    "location":"View 3D > Tool Shelf",
    "warning":"",
    "github_url":"https://github.com/DavidC1874",
    "category":"Animation",
}





import bpy

class Main_VA_Panel(bpy.types.Panel):
    bl_label = "Visibility Animation"
    bl_idname = "VIEW3D_PT_Vaim"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Visibility Anim"
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        row = layout.row()
        row.operator("ob.hide_both", text = "Hide Objects")
        
        row = layout.row()
        row.operator("ob.show_both", text = "Show Objects")
              
        row = layout.row()
        row.label(text="Animations")
        row = layout.row()
        row.operator("va.insert_key", text = "Insert Visibility Keyframe")
        
        row = layout.row()
        row.prop(bpy.context.scene.tool_settings, "use_keyframe_insert_auto", text="Auto Keyframe")



class Hide_Both_Op(bpy.types.Operator):
    bl_idname = "ob.hide_both"
    bl_label = "Hide in Viewport & Render"

    previous_selected_objs = []

    def execute(self, context):
        selected_objs = bpy.context.selected_objects
        
        for obj in bpy.context.view_layer.objects:
            if obj.get("was_hidden_by_op"):
                del obj["was_hidden_by_op"]

        for obj in selected_objs:
            obj.hide_viewport = True
            obj.hide_render = True
            obj["was_hidden_by_op"] = True

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                obj.keyframe_insert(data_path="hide_viewport")
                obj.keyframe_insert(data_path="hide_render")

        self.previous_selected_objs = list(selected_objs)
        
        return {'FINISHED'}

class Show_Both_Op(bpy.types.Operator):
    bl_idname = "ob.show_both"
    bl_label = "Show in Viewport & Render"

    def execute(self, context):

        for obj in bpy.context.view_layer.objects:
            if obj.get("was_hidden_by_op"):
                obj.hide_viewport = False
                obj.hide_render = False

                if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                    obj.keyframe_insert(data_path="hide_viewport")
                    obj.keyframe_insert(data_path="hide_render")
                    
                del obj["was_hidden_by_op"]
                obj.select_set(True)

        if bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]

        return {'FINISHED'}
  
class Insert_Keyframe_Op(bpy.types.Operator):
    bl_idname = "va.insert_key"
    bl_label = "Insert Keyframe in Viewport & Render" 

    def execute(self, context):
        scene = context.scene
        current_frame = scene.frame_current
        selected_objs = bpy.context.selected_objects

        for obj in selected_objs:
            obj.keyframe_insert(data_path="hide_viewport", frame=current_frame)
            obj.keyframe_insert(data_path="hide_render", frame=current_frame)

        bpy.context.view_layer.update()

        return {'FINISHED'}





class Panel_Special(bpy.types.Panel):
    bl_label = "Speicals"
    bl_idname = "Sync_PVA"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = 'Visibility Anim'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.3
        
        row = layout.row()
        row.operator("ob.show_all", icon = "HIDE_OFF")
        row = layout.row()
        row.label(text="Click Before Final Render↓")
        row = layout.row()
        row.operator("va.sync_render",text = "Sync Visibility", icon = "UV_SYNC_SELECT")
        
        
        
class Show_All_Op(bpy.types.Operator):
    bl_idname = "ob.show_all"
    bl_label = "Show All Hidden"
    
    def execute(self, context):
        for obj in bpy.context.view_layer.objects:
            if obj.hide_viewport or obj.hide_render:
                obj.hide_viewport = False
                obj.hide_render = False
        return {'FINISHED'}
        
class Sync_VR_Op(bpy.types.Operator):
    bl_idname = "va.sync_render"
    bl_label = "Sync View & Render Visibility"

    def execute(self, context):
        scene = context.scene
        start_frame = scene.frame_start
        end_frame = scene.frame_end

        for frame in range(start_frame - 1, start_frame):
            for obj in scene.objects:
                if obj.hide_viewport:
                    obj.hide_render = True
                else:
                    obj.hide_render = False
                obj.keyframe_insert(data_path="hide_render", frame=frame)
                
        for frame in range(start_frame, end_frame + 1):
            scene.frame_set(frame)
            
            for obj in scene.objects:
                if obj.animation_data and obj.animation_data.action:
                    current_hide_render = obj.hide_render
                    current_hide_viewport = obj.hide_viewport
                    
                    if current_hide_viewport:
                        obj.hide_render = True
                    else:
                        obj.hide_render = False
    
                    if obj.hide_render != current_hide_render:
                        obj.keyframe_insert(data_path="hide_render", frame=frame)

        bpy.context.view_layer.update()
        
        return {'FINISHED'}



def register():
    bpy.utils.register_class(Main_VA_Panel)
    bpy.utils.register_class(Hide_Both_Op)
    bpy.utils.register_class(Show_Both_Op)
    bpy.utils.register_class(Insert_Keyframe_Op)
    bpy.utils.register_class(Panel_Special)
    bpy.utils.register_class(Show_All_Op)
    bpy.utils.register_class(Sync_VR_Op)

def unregister():
    bpy.utils.unregister_class(Main_VA_Panel)
    bpy.utils.unregister_class(Hide_Both_Op)
    bpy.utils.unregister_class(Show_Both_Op)
    bpy.utils.unregister_class(Insert_Keyframe_Op)
    bpy.utils.unregister_class(Panel_Special)
    bpy.utils.unregister_class(Show_All_Op)
    bpy.utils.unregister_class(Sync_VR_Op)
    
if __name__ == "__main__":
    register()