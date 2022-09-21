from PIL import Image

#img = Image.open('images/pistol_64.jpg')

#Resize
#smaller_img = img.resize((350,350))
#smaller_img.show()

#Crop
#box = (10,60,150,250)
#region = img.crop(box)
#region.show()

#Rotation
img2 = Image.open('images/Bullets_7.jpg')
rotated_img = img2.rotate(90)
rotated_img.show()
