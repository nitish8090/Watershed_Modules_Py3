from PIL import Image
import os


class CIMPGroup:
    def __init__(self, path):
        self.path = path
        self.items = []

    def set_cimps(self):
        cimps = os.listdir(self.path)
        for cimp in cimps:
            cimp_path = os.path.join(self.path, cimp)
            if os.path.isdir(cimp_path):
                new_cimp = CIMP(cimp_path)
                self.items.append(new_cimp)


class CIMP:
    def __init__(self, full_path):
        self.path = full_path
        self.name = os.path.split(full_path)[1]
        self.image_list = []

    def read_image_list(self):
        self.image_list = os.listdir(self.path)


class CombinedImage(Image.new):
    def __init__(self, mode, size, color):
        a = 20
        super().__init__(mode='RGB', size, color)

    @classmethod
    def set_example_image(cls, path):
        cls.ex_image = Image.open(path)

    @classmethod
    def set_heading_image_path(cls, path):
        cls.heading_image = Image.open(path)

    @classmethod
    def set_legend_image_path(cls, path):
        cls.legend_image = Image.open(path)

    def create(self):
        self.image = Image.new(
            'RGB',
            (self.heading_image.size[0] + self.ex_image.size[0] + self.legend_image.size[0], 4 * self.ex_image.size[1]),
            (250, 250, 250)
        )
        self.image.paste(self.heading_image, (0, 0))
        self.image.paste(self.legend_image, (self.heading_image.size[0] + self.ex_image.size[0], 0))
        return self

    def add_image(self, path, y):
        new_image = Image.open(path)
        self.image.paste(new_image, (self.heading_image.size[0], y))

    def add_overlay(self, overlay_image_path):
        overlay_image = Image.open(overlay_image_path)
        self.image.paste(overlay_image, (0,0), overlay_image)

    def landscape_to_portrait(self):
        portrait_image = Image.new('RGB', (self.image.size[1], self.image.size[0]))



groups = {'Drought': ['Rel_P_DROUGHT.png', 'Res_P_DROUGHT.png', 'RRV_P_DROUGHT.png', 'Vul_P_DROUGHT.png'],
          'GW': ['Rel_PERC_GW.png', 'Res_PERC_GW.png', 'RRV_PERC_GW.png', 'Vul_PERC_GW.png'],
          'PET': ['Rel_PET.png', 'Res_PET.png', 'RRV_PET.png', 'Vul_PET.png'],
          'SURQ_HIGH': ['Rel_SURQ_HIGH.png', 'Res_SURQ_HIGH.png', 'RRV_SURQ_HIGH.png', 'Vul_SURQ_HIGH.png'],
          'SYLD': ['Rel_SYLD.png', 'Res_SYLD.png', 'RRV_SYLD.png', 'Vul_SYLD.png'],
          'WHI': ['Rel_WHI.png', 'Res_WHI.png', 'WHI.png', 'Vul_WHI.png']}


# 'WHI_C.png'

def main():
    cimp_group = CIMPGroup(r'D:\Nitish\2102_Feb\4_PolygonToRaster\piCharts4')
    cimp_group.set_cimps()

    output_folder = r"D:\Nitish\2102_Feb\4_PolygonToRaster\Stiched_Images2"

    legend_path = r"D:\Nitish\2102_Feb\4_PolygonToRaster\stitching_stuff\legend.png"
    CombinedImage.set_legend_image_path(legend_path)

    heading_image_path = r"D:\Nitish\2102_Feb\4_PolygonToRaster\stitching_stuff\headings.png"
    CombinedImage.set_heading_image_path(heading_image_path)

    ex_image_path = r"D:\Nitish\2102_Feb\4_PolygonToRaster\piCharts3\book3CIMP5 RCP 4.5\Rel_P_DROUGHT.png"
    CombinedImage.set_example_image(ex_image_path)

    overlay_image_path = r"D:\Nitish\2102_Feb\4_PolygonToRaster\stitching_stuff\overlay_alphabets.png"

    for cimp in cimp_group.items:
        print("Processing CIMP: {}".format(cimp.name))
        print("CIMP Path: {}".format(cimp.path))

        output_cimp = os.path.join(output_folder, cimp.name)
        os.mkdir(output_cimp)

        for key in groups.keys():
            print("\tStitching: {}".format(key))
            print("\tGroup Images:")

            combined_image = CombinedImage().create()
            # Add Side Image
            init_pos_y = 0
            for n in groups[key]:
                print("\t\t{}".format(n))
                n_path = os.path.join(cimp.path, n)
                print("\t\t{}".format(n_path))
                combined_image.add_image(n_path, y=init_pos_y)
                init_pos_y += combined_image.ex_image.size[1]

            combined_image.add_overlay(overlay_image_path)

            combined_image.image = combined_image.image.rotate(-90, expand=1)
            save_path = os.path.join(output_cimp, key + ".png")
            combined_image.image.save(save_path, "PNG")

            # combined_image.image.save(r'D:\Nitish\2102_Feb\4_PolygonToRaster' + r'\test_image.png', "PNG")
            # combined_image.image.show()




main()
