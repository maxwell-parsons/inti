import rawpy
from cv2 import imwrite
from skimage.io import imsave
import matplotlib.pyplot as plt
import numpy as np
from inti.io import import_raw_from_t3i


def main():
    im_file = "C:\\Users\\maxwe\\Dropbox\\raw photos\\20200725-Plants and hunter\\favorites\\favorites\\IMG_8821.cr2"
    name = 'hunter_curled_up'
    gamma = 1.
    color_balance = [1., 1., 1.0]
    rgb = import_raw_from_t3i(im_file)
    for i, cb in enumerate(color_balance):
        rgb[:, :, i] = rgb[:, :, i] * cb
    # fig, ax = plt.subplots(1, 1)
    # cax = ax.imshow(rgb[:, :, 1]**(1. / 2.2), cmap='gray')
    # fig.colorbar(cax)
    # plt.show()
    # plt.hist(rgb[:, :, 0].flatten(), bins=1000)
    # plt.show()
    rgb = rgb**gamma
    rgb = np.round(rgb / np.max(rgb.flatten()) * 2**16).astype(np.uint16)
    #rgb[:, :, 1] = 64000
    #plt.hist(rgb[:, :, 0].flatten(), bins=500)
    # plt.show()
    # plt.imshow(rgb)
    # plt.show()
    # plt.hist(rgb[:, :, 0].flatten(), bins=1000)
    # plt.show()
    rgb_new = np.zeros_like(rgb)
    rgb_new[:, :, 0] = rgb[:, :, 2]
    rgb_new[:, :, 1] = rgb[:, :, 1]
    rgb_new[:, :, 2] = rgb[:, :, 0]
    imwrite(name +'.png', rgb_new.astype(np.uint16))

if __name__ == "__main__":
    main()