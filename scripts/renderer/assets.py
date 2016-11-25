from taichi_utils import *

class Materials:
    def __init__(self):
        self.materials = {}

    def get_material(self, name):
        if name not in self.materials:
            self.materials[name] = getattr(self, 'get_material_' + name)()
        return self.materials[name]

    def get_material_gold(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(1.0, 1.0, 0.6), specular_color=(0.1, 0.1, 0.1), glossiness=-1, transparent=False))
        return material

    def get_material_wall(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(1.0, 1.0, 0.6), specular_color=(0.0, 0.0, 0.0), glossiness=-1, transparent=False))
        return material

    def get_material_glass(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(0, 0, 0), specular_color=(1.0, 1.0, 1.0), glossiness=-1,
                              transparent=True, ior=1.0))
        return material


materials = Materials()
