import trimesh
from maps import MAPS

def patchify(in_path, out_path):
    mesh = trimesh.load(in_path)
    mesh = mesh.simplify_quadric_decimation(1024)
    mesh = MAPS(mesh.vertices, mesh.faces, base_size=256).mesh_upsampling(3)
    mesh.export(out_path)
    
if __name__ == "__main__":
    patchify("Trial_Model_1.stl", "Trial_Patches_1.stl")