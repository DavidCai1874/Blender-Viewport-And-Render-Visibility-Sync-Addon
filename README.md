# Blender_Visibility_Addon
An addon for Blender, controls the viewport and render visibility

***
由于插件还在改进与测试中, 暂时readme文件大部分都是中文

# 如何使用
1. 点击.py后缀结尾的文件
2. 进入代码页面后, 点击右上角的下载, 会下载一个.py结尾的文件
3. 打开Blender, 点击在edit菜单中最下面的preference
4. 选中addon菜单, 点击右上角的Install, 然后**选择刚刚下载的.py结尾的文件安装**
5. 等待一小会, 会跳出来插件名, 点击名称左边的方框
6. 在Blender按N出现的侧栏中, 会显示插件名, 开始使用即可

# 图片版
1. ![1](https://github.com/user-attachments/assets/64589ba4-6364-4474-a594-3a24dfd922a7)
2. ![2](https://github.com/user-attachments/assets/c4f2403b-35e0-42c2-8187-300587da1549)
3. ![3](https://github.com/user-attachments/assets/6bf58a6f-d924-4632-833e-9aab6c0909c2)
4. ![4](https://github.com/user-attachments/assets/7d56364a-972a-4048-8bf2-d3563ce71b60)
5. ![5](https://github.com/user-attachments/assets/c9126593-2695-414a-b581-4bee1e7b76d5)

# 一些Tips
- 作为编辑者, 我建议是手动在大纲视角隐藏掉其他准备做动画的物件, 专注于一个一个k
- Hide和Show请务必先使用hide, 如果直接点Show, 会出现bug
- 如果物件在一开始需要显示, 在某一帧再隐藏, 可以先点一下"Insert Visibility Keyframe",再拖到需要隐藏的帧隐藏
- 需要k动画可以直接打开auto keyframe, "Insert Visibility Keyframe"这个键只会在物体显示的时候生效
- specials中的同步功能不是必须的, 但万一出现了物件视图中没有, 但是渲染中有的情况,可以点一下
- 此处附上插件面板图
![panel](https://github.com/user-attachments/assets/06d6e2d5-d9b8-4a26-b2f5-63ec73a0f947)


# 已知的bug
如果在隐藏了上一批以后, 在选中新的要隐藏的物件时点了Show, 上一批隐藏的会重新显示
![bug1](https://github.com/user-attachments/assets/7987077b-b44b-4ede-96fe-c3ed06a7a73e)
![bug2](https://github.com/user-attachments/assets/4e4039e8-3f0e-4419-b3c7-1b166fec0969)

