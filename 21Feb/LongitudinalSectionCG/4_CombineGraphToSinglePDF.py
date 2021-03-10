from PIL import Image
import os


def main():
    image_folder = r"D:\Nitish\26_States\2_MP\MP_LongitudinalSection\TripletCharts"
    pdf_path = r"D:\Nitish\26_States\2_MP\MP_LongitudinalSection\MP_LongitudinalSection_Combined.pdf"

    triplet_list = return_triplets()
    images = []
    for i in triplet_list:
        image_name = 'MP_Long_Sec_{}_{}_{}.png'.format(i[0], i[1], i[2])
        print(image_name)
        image_path = os.path.join(image_folder, image_name)
        a_image = Image.open(image_path)
        images.append(a_image)

    a_image = Image.open(os.path.join(image_folder, "MP_Long_Sec_1279.png")).convert('RGB')
    images.append(a_image)
    images[0].save(pdf_path, save_all=True, append_images=images[1:])


def return_triplets():
    triplet_list = []
    triplet_count = 0
    triplets = []
    for i in range(1, 1279 + 1):
        # print(triplet_count)
        if triplet_count < 3:
            triplets.append(i)
            triplet_count += 1

        if triplet_count == 3:
            triplet_count = 0
            # print(triplets)
            triplet_list.append(triplets)
            triplets = []

    return triplet_list


main()
