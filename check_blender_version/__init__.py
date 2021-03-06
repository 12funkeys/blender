import bpy

bl_info = {
    "name" : "Check blender version",
    "author" : "12funkeys",
    "version" : (2,1), 
    "blender" : (2, 80, 0),
    "location" : "Info header", 
    "description" : "check .blender version", 
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "System"
}

class INFO_HT_Ver(bpy.types.Header):

    bl_region_type = 'HEADER'
    bl_space_type = 'TOPBAR'
    
    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)

        #check blender file version
        X = str(bpy.data.version[0])
        Y = str(bpy.data.version[1]).zfill(2)
        Z = str(bpy.data.version[2]).zfill(2)

        #check blender app version
        appX = str(bpy.app.version[0])
        appY = str(bpy.app.version[1]).zfill(2)
        appZ = str(bpy.app.version[2]).zfill(2)

        bl_file_ver = ("@" + X + "." + Y + "." + Z)
        bl_file_int = int(X + Y + Z)
        bl_app_int = int(appX + appY + appZ)

        #version check
        if bl_file_int > bl_app_int:
            row.label(text=bl_file_ver + " caution! .blender with newer version." , icon='ERROR', translate=False)
        else:
            row.label(text=bl_file_ver, icon='FILE_BLEND', translate=False)

def register():
    bpy.utils.register_class(INFO_HT_Ver)

def unregister():
    bpy.utils.unregister_class(INFO_HT_Ver)

if __name__ == "__main__":
    register()
