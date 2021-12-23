from PIL import Image

inputi = input('Enter your image\n')
outputi = input('Enter your imageout\n')

me = Image.open(inputi)
bg = Image.open(outputi)
bg.paste(me,(0,0),me)
bg.save('Outputfromcode.jpg')
bg.show()