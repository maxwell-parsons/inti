import rawpy

def import_raw_from_t3i(im_file):
    raw = rawpy.imread(im_file)
    rgb = raw.postprocess(no_auto_bright=True, use_auto_wb=False, use_camera_wb=False, gamma=None, output_bps=16)
    return rgb
