import bpy

scene = bpy.context.scene
start_frame = scene.frame_start
end_frame = scene.frame_end

#detect if the object is visible when animation starts
for frame in range (start_frame - 1, start_frame):
    for obj in scene.objects:
         if obj.hide_viewport:
                obj.hide_render = True
         else:
                obj.hide_render = False
         obj.keyframe_insert(data_path="hide_render", frame=frame)
        

#loop each frame
for frame in range(start_frame-1, end_frame + 1):
    scene.frame_set(frame)
    
    #see if there's an animation keyframe
    for obj in scene.objects:
        if obj.animation_data and obj.animation_data.action:
            current_hide_render = obj.hide_render
            current_hide_viewport = obj.hide_viewport
            
            # if it's invisible in viewport, hide in render
            if current_hide_viewport:
                obj.hide_render = True
            else:
                obj.hide_render = False
            
            # insert keyframe only if the visibility status changed
            if obj.hide_render != current_hide_render:
                obj.keyframe_insert(data_path="hide_render", frame=frame)

# update the scene after code finish running
bpy.context.view_layer.update()