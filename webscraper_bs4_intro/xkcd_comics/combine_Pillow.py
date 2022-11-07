from PIL import Image

img1 = 'wirecutter_recommendation.png'
img2 = 'konigsberg.png'
combined = 'combined.png'

img1Read = Image.open(img1)
img2Read = Image.open(img2)

def get_concat_v_blank(im1, im2, color=(256, 256, 256)):
    combinedImg = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    combinedImg.paste(im1, (0, 0))
    combinedImg.paste(im2, (0, im1.height))
    return combinedImg

combinedImgBinary = get_concat_v_blank(img1Read, img2Read)
combinedImgBinary.save('combined.pdf')
