from PIL import Image

def sum(list):
    x = 0
    for i in list:
        x+=i
    return x

class open_Image:
    def __init__(self,path):
        self.path = path
    def open_File(self):
        image = Image.open(self.path)
        all_Pixel = image.load()
        return self.decode_File_Data(all_Pixel, image.size)
    def decode_File_Data(self, all_Pixel, size):
        array = []
        for i in range(0, size[0]):
            for j in range(0, size[1]):
                array.append(self.convert(all_Pixel[i,j]))
        return array
    def convert(self, number):
        return (-1*sum(number)+len(number)*255)/len(number)/255