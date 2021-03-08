import os
from PIL import Image


def main():
    image_folder = r"F:\Watershed_Works\2102 Feb 2021\CG_Longitudinal_Section\ImagesLongSec"
    test_save = r"F:\Watershed_Works\2102 Feb 2021\CG_Longitudinal_Section\ImagesLongSec\test\test.png"
    output_folder = r"F:\Watershed_Works\2102 Feb 2021\CG_Longitudinal_Section\combines_images"
    third_counter = 0
    for i in range(1, 1237):
        print("Index: {}".format(i))
        if third_counter == 0:
            print("\t\tCreating new image, i: {}".format(i))
            image_size = (595 * 2, 842 * 2)
            img = Image.new(
                'RGB',
                image_size,
                (250, 250, 250)
            )
            print(image_size)
            h = 60

        image_path = os.path.join(image_folder, 'Stream_{}_LongitudinalSection.png'.format(i))
        print("\tReading {}".format(image_path))
        new_image = Image.open(image_path)
        img.paste(new_image, (100, h))
        h = h + 500

        if third_counter == 2:
            image_name = "CG_Long_Sec_{}_{}_{}.png".format(i-2, i-1, i)
            path = os.path.join(output_folder, image_name)
            print("\t\tSaving at: {}".format(path))
            img.save(path, "PNG")


        third_counter = third_counter + 1

        if third_counter == 3:
            third_counter = 0



main()
