from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt

im = io.imread("C:\\PjtPillCounter\\images_pill\\20210125 135858-1.png", as_gray=True)
val = filters.threshold_otsu(im)
drops = ndimage.binary_fill_holes(im < val)
plt.imshow(drops, cmap='gray')
plt.show()