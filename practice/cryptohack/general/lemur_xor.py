# i actually did this challenge with photopea
# put the two images on top of each other, then put the "Difference" mask in the layer editor
# which showed me the flag and a picture of a lemur
# but ill put the code here to see if it's a different picture

from PIL import Image, ImageChops

img1 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")
img2 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")

img3 = ImageChops.difference(img1, img2)
img3.show()
img3.save("lemur+flag.png")

# nope, it's the same image, just use Photopea lol