#
# Copyright 2018 rn9dfj3
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import bpy
from pathlib import Path
bl_info = {
    "name": "Timebank",
    "author": "rn9dfj3",
    "version": (0, 0),
    "blender": (2, 79, 0),
    "location": "Info > File",
    "description": "Save blender file named each process.",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "https://github.com/rn9dfj3/timebank/wiki",
    "tracker_url": "https://github.com/rn9dfj3/timebank/issues",
    "category": "System"
}
OPTION_SAVED = {'REGISTER'}
PROCESSES = ("modeling", "skinning", "texturing",
             "morphing", "animating", "rendering", "compositing", "scripting")
MODELING = 0
SKINNING = 1
TEXTURING = 2
MORPHING = 3
ANIMATING = 4
RENDERING = 5
COMPOSITING = 6
SCRIPTING = 7


def save(self, context, type):
        filepath = context.blend_data.filepath
        if filepath == "":
            bpy.ops.wm.save_as_mainfile('INVOKE_AREA')
            return
        path = Path(filepath)
        suffix = path.suffix
        stem = path.stem
        # num
        first = stem.rfind("_")
        base = stem
        if first == -1:  # only base
            pass
        else:
            num = stem[first+1:]
            if num.isdigit():  # hit bank
                base = stem[:first]
                # process
                first = base.rfind("_")
                if first == -1:  # not bank
                    pass
                else:
                    process = base[first+1:]
                    if process in PROCESSES:
                        base = base[:first]
        parent = path.resolve()
        files = parent.parent.glob(base+'*'+suffix)
        m = 0
        for file in files:
            file_stem = file.stem
            second = file_stem.rfind("_")
            num = file_stem[second+1:]
            if num.isdigit():
                m = max(int(num), m)
            else:
                m = max(0, m)
        num = str(m+1)
        path = path.with_name(base+"_"+PROCESSES[type]+"_"+num)
        path = path.with_suffix(suffix)
        filepath = str(path)
        self.report({'INFO'}, "Saved "+str(path))
        bpy.ops.wm.save_as_mainfile(filepath=filepath, check_existing=True)


class SaveModeling(bpy.types.Operator):
    bl_idname = "wm.timebank_modeling"
    bl_label = "Save Modeling"
    bl_description = "Save the current file as modeling process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, MODELING)
        return {'FINISHED'}


class SaveSkinning(bpy.types.Operator):
    bl_idname = "wm.timebank_skinning"
    bl_label = "Save Skinning"
    bl_description = "Save the current file as skinning process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, SKINNING)
        return {'FINISHED'}


class SaveTexturing(bpy.types.Operator):
    bl_idname = "wm.timebank_texturing"
    bl_label = "Save Texturing"
    bl_description = "Save the current file as texturing process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, TEXTURING)
        return {'FINISHED'}


class SaveMorphing(bpy.types.Operator):
    bl_idname = "wm.timebank_morphing"
    bl_label = "Save Morphing"
    bl_description = "Save the current file as morphing process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, MORPHING)
        return {'FINISHED'}


class SaveAnimating(bpy.types.Operator):
    bl_idname = "wm.timebank_animating"
    bl_label = "Save Animating"
    bl_description = "Save the current file as animating process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, ANIMATING)
        return {'FINISHED'}


class SaveRendering(bpy.types.Operator):
    bl_idname = "wm.timebank_rendering"
    bl_label = "Save Rendering"
    bl_description = "Save the current file as rendering process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, RENDERING)
        return {'FINISHED'}


class SaveCompositing(bpy.types.Operator):
    bl_idname = "wm.timebank_compositing"
    bl_label = "Save Compositing"
    bl_description = "Save the current file as compositing process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, COMPOSITING)
        return {'FINISHED'}


class SaveScripting(bpy.types.Operator):
    bl_idname = "wm.timebank_scripting"
    bl_label = "Save Scripting"
    bl_description = "Save the current file as scripting process."
    bl_options = OPTION_SAVED

    def execute(self, context):
        save(self, context, SCRIPTING)
        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SaveModeling.bl_idname, icon='EDIT')
    self.layout.operator(SaveSkinning.bl_idname, icon='WPAINT_HLT')
    self.layout.operator(SaveTexturing.bl_idname, icon='TEXTURE')
    self.layout.operator(SaveMorphing.bl_idname, icon='SHAPEKEY_DATA')
    self.layout.operator(SaveAnimating.bl_idname, icon='ACTION')
    self.layout.operator(SaveRendering.bl_idname, icon='RENDER_STILL')
    self.layout.operator(SaveCompositing.bl_idname, icon='NODETREE')
    self.layout.operator(SaveScripting.bl_idname, icon='TEXT')


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file.append(menu_fn)


def unregister():
    bpy.types.INFO_MT_file.remove(menu_fn)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
