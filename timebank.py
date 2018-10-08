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
MODELING_ICON = 'EDIT'
SKINNING_ICON = 'WPAINT_HLT'
TEXTURING_ICON = 'TEXTURE'
MORPHING_ICON = 'SHAPEKEY_DATA'
ANIMATING_ICON = 'ACTION'
RENDERING_ICON = 'RENDER_STILL'
COMPOSITING_ICON = 'NODETREE'
SCRIPTING_ICON = 'TEXT'

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


class LoadLatest(bpy.types.Operator):
    bl_idname = "wm.timebank_load_latest"
    bl_label = "Load Latest file"
    bl_description = "Load the latest file."
    bl_options = OPTION_SAVED

    def execute(self, context):
        #save(self, context, SCRIPTING)
        filepath = context.blend_data.filepath
        if filepath == "":
            #bpy.ops.wm.save_as_mainfile('INVOKE_AREA')
            #return
            return {'CANCELLED'}
        path = Path(filepath)
        suffix = path.suffix
        stem = path.stem
        first = stem.rfind("_")
        base = stem
        if first == -1:
            return {'CANCELLED'}
        base = base[:first]
        first = base.rfind("_")
        if first == -1:
            return {'CANCELLED'}                
        base = base[:first]
        #self.report({'INFO'}, base)
        parent = path.resolve()
        files = parent.parent.glob(base+'*'+suffix)
        max_num = 0
        max_file = None
        for file in files:
            file_stem = file.stem
            if not file_stem.startswith(base):
                continue
            #self.report({'INFO'}, file_stem)
            first = file_stem.rfind("_")
            num = file_stem[first+1:]
            if num.isdigit():
                #self.report({'INFO'}, num)                        
                num = int(num)                        
                if num > max_num:
                    max_num = num
                    max_file = file
        self.report({'INFO'}, "Loaded "+str(max_file))
        bpy.ops.wm.open_mainfile(filepath=str(max_file))
        return {'FINISHED'}

#class Load(bpy.types.Operator):
#    bl_idname = "wm.timebank_load"
#    bl_label = "Load"
#    bl_description = "Load the file."
#    bl_options = OPTION_SAVED

#    def execute(self, context):
#        #save(self, context, SCRIPTING)
#        filepath = context.blend_data.filepath
#        if filepath == "":
#            #bpy.ops.wm.save_as_mainfile('INVOKE_AREA')
#            #return
#            return {'CANCELLED'}
#        path = Path(filepath)
#        suffix = path.suffix
#        stem = path.stem
#        first = stem.rfind("_")
#        base = stem
#        if first == -1:
#            return {'CANCELLED'}
#        else:
#            base = base[:first]
#            first = base.rfind("_")
#            if first == -1:
#                return {'CANCELLED'}                
#            else:
#                base = base[:first]
#                #self.report({'INFO'}, base)
#                parent = path.resolve()
#                files = parent.parent.glob(base+'*'+suffix)
#                max_num = 0
#                max_file = None
#                #for file in files:
#                #    file_stem = file.stem
#                #    self.report({'INFO'}, file_stem)
#                #    first = file_stem.rfind("_")
#                #    num = file_stem[first+1:]
#                #    if num.isdigit():
#                #        self.report({'INFO'}, num)                        
#                #        num = int(num)                        
#                #        if num > max_num:
#                #            max_num = num
#                #            max_file = file
#                self.report({'INFO'}, "Loaded "+str(max_file))
#                bpy.ops.wm.open_mainfile(filepath=str(max_file))
#        return {'FINISHED'}

class TimebankLoadMenu(bpy.types.Menu):
    bl_label = "Load Timebank"
    bl_idname = "INFO_MT_timebank_load_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator(LoadLatest.bl_idname)
        layout.menu(TimebankAllMenu.bl_idname, icon="RECOVER_LAST")
        
        
class TimebankAllMenu(bpy.types.Menu):
    bl_label = "All files"
    bl_idname = "INFO_MT_timebank_all_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'EXEC_DEFAULT'
        filepath = context.blend_data.filepath
        if filepath == "":
            return
        path = Path(filepath)
        suffix = path.suffix
        stem = path.stem
        first = stem.rfind("_")
        base = stem
        if first == -1:
            return
        base = base[:first]
        first = base.rfind("_")
        if first == -1:
            return
        base = base[:first]
        #self.report({'INFO'}, base)
        parent = path.resolve()
        files = parent.parent.glob(base+'*'+suffix)
        files = sorted(files, key = num_fn, reverse=True)
        #max_num = 0
        #max_file = None
        for file in files:
            file_stem = file.stem
            #layout.label(text=file_stem)
            first = file_stem.rfind("_")
            if first == -1:
                continue
            pro = file_stem[:first]
            first = pro.rfind("_")
            if first == -1:
                continue
            pro = pro[first+1:]
            icon = "NONE"
            if pro == PROCESSES[MODELING]:
                icon = MODELING_ICON
            if pro == PROCESSES[SKINNING]:
                icon = SKINNING_ICON
            if pro == PROCESSES[TEXTURING]:
                icon = TEXTURING_ICON
            if pro == PROCESSES[MORPHING]:
                icon = MORPHING_ICON
            if pro == PROCESSES[ANIMATING]:
                icon = ANIMATING_ICON
            if pro == PROCESSES[RENDERING]:
                icon = RENDERING_ICON
            if pro == PROCESSES[COMPOSITING]:
                icon = COMPOSITING_ICON
            if pro == PROCESSES[SCRIPTING]:
                icon = SCRIPTING_ICON
            if icon == "NONE":
                continue
            op = layout.operator("wm.open_mainfile", text = file.name, icon=icon)
            op.filepath = str(file)
            #op.bl_options = OPTION_SAVED
            #op.label = file.name
        #    self.report({'INFO'}, file_stem)
        #    first = file_stem.rfind("_")
        #    num = file_stem[first+1:]
        #    if num.isdigit():
        #        self.report({'INFO'}, num)                        
        #        num = int(num)                        
        #        if num > max_num:
        #            max_num = num
        #            max_file = file
        #self.report({'INFO'}, "Loaded "+str(max_file))
        #bpy.ops.wm.open_mainfile(filepath=str(max_file))

def num_fn(file):
    stem = file.stem
    first = stem.rfind("_")
    num = stem[first+1:]
    if not num.isdigit():
        num = -1
    return int(num)

def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(TimebankLoadMenu.bl_idname, icon="RECOVER_LAST")
    self.layout.operator(SaveModeling.bl_idname, icon=MODELING_ICON)
    self.layout.operator(SaveSkinning.bl_idname, icon=SKINNING_ICON)
    self.layout.operator(SaveTexturing.bl_idname, icon=TEXTURING_ICON)
    self.layout.operator(SaveMorphing.bl_idname, icon=MORPHING_ICON)
    self.layout.operator(SaveAnimating.bl_idname, icon=ANIMATING_ICON)
    self.layout.operator(SaveRendering.bl_idname, icon=RENDERING_ICON)
    self.layout.operator(SaveCompositing.bl_idname, icon=COMPOSITING_ICON)
    self.layout.operator(SaveScripting.bl_idname, icon=SCRIPTING_ICON)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file.append(menu_fn)


def unregister():
    bpy.types.INFO_MT_file.remove(menu_fn)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
