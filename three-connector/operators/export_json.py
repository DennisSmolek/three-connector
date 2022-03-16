import bpy
import json

from bpy_extras.io_utils import ImportHelper
from bpy.types import (Operator)
from bpy.props import StringProperty

from ..utils.scene_parser import SceneParser

class THREECONNECTOR_OT_ExportJsonPath(Operator, ImportHelper):
    bl_idname = 'object.threeconnector_export_json_path'
    bl_label = 'Accept'
    bl_options = {'PRESET', 'UNDO'}
 
    filename_ext = '.json'

    filter_glob: StringProperty(
        default='*.json',
        options={'HIDDEN'}
    )
 
    def execute(self, context):
        scene = bpy.context.scene
        scene.three_connector.export_json_path = self.filepath
        return {'FINISHED'}

class THREECONNECTOR_OT_ExportJson(Operator):
    bl_idname = 'object.threeconnector_export_json'
    bl_label = 'Accept'
    
    def execute(self, context):
        scene = bpy.context.scene
        data = SceneParser().get_animation_date()
        path = scene.three_connector.export_json_path

        with open( path, mode='wt', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
            
        return {'FINISHED'}

