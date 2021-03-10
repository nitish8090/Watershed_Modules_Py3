from PIL import Image
import os


def main():
    image_folder = r"D:\Nitish\26_States\2_MP\MP_LongitudinalSection\TripletCharts"
    pdf_path = r"D:\Nitish\26_States\2_MP\MP_LongitudinalSection\MP_LongitudinalSection_Combined.pdf"

    # Generate a triplet list for the images in the folder,
    # The last factor of three will be considered
    n = int(1279 / 3)
    triplet_list = [(i * 3 - 2, i * 3 - 1, i * 3) for i in range(1, n + 1)]

    # Loop through each triplet list
    images = []
    for i in triplet_list:
        image_name = 'MP_Long_Sec_{}_{}_{}.png'.format(i[0], i[1], i[2])
        image_path = os.path.join(image_folder, image_name)

        # Open image and append it to image list
        a_image = Image.open(image_path)
        images.append(a_image)

    # Open and append the last images which are not divisible by 3
    a_image = Image.open(os.path.join(image_folder, "MP_Long_Sec_1279.png")).convert('RGB')
    images.append(a_image)

    # Open the first image and append all images to it and save it to PDF
    images[0].save(pdf_path, save_all=True, append_images=images[1:])


main()
