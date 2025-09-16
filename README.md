# Blender-Viewport-And-Render-Visibility-Sync-Addon
An addon for Blender, controls the viewport and render visibility

中文版可以移步这里/ Here's the instructions in Chinese:[点击这里查看中文文档](README_CN.md)

# How To Use
1. Click on the file ending with .py
2. After entering the code page, click on the download button on the upper right corner, and a file ending with .py will be downloaded
3. Open Blender and click on the preference button at the bottom of the edit menu
4. Select the addon menu, click on the Install button in the upper right corner, and then **select the file ending with .py that you just downloaded to install**
5. After a while, the add-on name will pop up, and click on the box to the left of the name
6. On the sidebar that appears when you press N in Blender, the add-on name will be there, and you can start using it

# Images of Instruction
1. ![1](https://github.com/user-attachments/assets/64589ba4-6364-4474-a594-3a24dfd922a7)
2. ![2](https://github.com/user-attachments/assets/c4f2403b-35e0-42c2-8187-300587da1549)
3. ![3](https://github.com/user-attachments/assets/6bf58a6f-d924-4632-833e-9aab6c0909c2)
4. ![4](https://github.com/user-attachments/assets/7d56364a-972a-4048-8bf2-d3563ce71b60)
5. ![5](https://github.com/user-attachments/assets/c9126593-2695-414a-b581-4bee1e7b76d5)

# Tips
- As the editor, I recommend manually hiding other objects, from the Outliner view, that you plan to animate, focusing on one object at a time.
- Please make sure to use "Hide" before "Show" to avoid bugs; if you click "Show" directly, issues may occur.
- If an object needs to be visible at first but hidden at a specific frame, click "Insert Visibility Keyframe" first, then move to the frame where you want to hide the object.
- For keyframe animation, you can simply enable auto keyframe. The "Insert Visibility Keyframe" button will only take effect when the object is visible.
- The sync function in the Specials menu is not mandatory, but if you encounter a situation which an object is invisible in the view but still visible in the render, you can use this button.
- Attached is an image of the plugin panel.
- ![panel](https://github.com/user-attachments/assets/06d6e2d5-d9b8-4a26-b2f5-63ec73a0f947)


# A bug here
If, after hiding the previous objects, I select new objects and then press 'Show,' the previously hidden objects will reappear.
![bug1](https://github.com/user-attachments/assets/7987077b-b44b-4ede-96fe-c3ed06a7a73e)
![bug2](https://github.com/user-attachments/assets/4e4039e8-3f0e-4419-b3c7-1b166fec0969)

# Demo on Youtube
[![Watch on YouTube](https://img.youtube.com/vi/-M0sVv4fPIs/0.jpg)](https://www.youtube.com/watch?v=-M0sVv4fPIs)

