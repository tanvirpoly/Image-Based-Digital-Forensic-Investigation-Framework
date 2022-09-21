from PIL import Image

img = Image.open('images/bullets_5.jpg')
#img.show()

new_img = Image.open('images/bullets_5.jpg').convert('L')
#new_img.show()



#Resize

smaller_img = Image.open('images/bullets_5.jpg')
smaller_img = img.resize((550,550))
smaller_img.show()
