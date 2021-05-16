from PIL import ImageColor, Image, ImageEnhance
import colorsys
import argparse


def hexToRgb(hex):
    return ImageColor.getcolor(hex, 'RGB')


def rgbToHsv(rgb):
    return colorsys.rgb_to_hsv(round(rgb[0] / 255, 2), round(rgb[1] / 255, 2), round(rgb[2] / 255, 2))


def closestColor(rgb):
    hsv = rgbToHsv(rgb)
    color_diffs = []

    if hsv[1] < 0.20:
        brightness = hsv[2]
        if brightness > 0.8:
            return '#AEBAD8'
        elif brightness > 0.7:
            return '#A598B5'
        else:
            return '#8E8086'

    for color in COLORS:
        (h, s, v) = color[0]
        hue_diff = min(abs(h - hsv[0]) * 360, 360 - abs(h - hsv[0]) * 360) / 180
        color_diffs.append((hue_diff, color[1]))

    return min(color_diffs)[1]


def adjustBrightness(closestIcon, image):
    b1 = rgbToHsv(pix[i, j])[2]
    b2 = rgbToHsv(hexToRgb(closestIcon))[2]

    if b1 == 0:
        return ImageEnhance.Brightness(image).enhance(0)
    else:
        factor = 1.0 * b1 / b2
        return ImageEnhance.Brightness(image).enhance(factor)


def paste(i, j):
    closestIcon = str(closestColor(pix[i, j])).upper()
    try:
        blank.paste(adjustBrightness(closestIcon, eval(closestIcon.replace('#', '_'))), (i * 25, j * 25))
    except:
        print(closestIcon + ' Something is wrong')


_00AECC = Image.open('icons_resized/' + '#00AECC.png')
_00E678 = Image.open('icons_resized/' + '#00E678.png')
_01BFBB = Image.open('icons_resized/' + '#01BFBB.png')
_2EBFB1 = Image.open('icons_resized/' + '#2EBFB1.png')
_3CEFA5 = Image.open('icons_resized/' + '#3CEFA5.png')
_8E8086 = Image.open('icons_resized/' + '#8E8086.png')
_37E6D4 = Image.open('icons_resized/' + '#37E6D4.png')
_54AFFF = Image.open('icons_resized/' + '#54AFFF.png')
_82A5AE = Image.open('icons_resized/' + '#82A5AE.png')
_87BBF7 = Image.open('icons_resized/' + '#87BBF7.png')
_87EB01 = Image.open('icons_resized/' + '#87EB01.png')
_97A9FF = Image.open('icons_resized/' + '#97A9FF.png')
_A598B5 = Image.open('icons_resized/' + '#A598B5.png')
_AEBAD8 = Image.open('icons_resized/' + '#AEBAD8.png')
_B0FC01 = Image.open('icons_resized/' + '#B0FC01.png')
_BD84F4 = Image.open('icons_resized/' + '#BD84F4.png')
_C10508 = Image.open('icons_resized/' + '#C10508.png')
_D5E64F = Image.open('icons_resized/' + '#D5E64F.png')
_D773F8 = Image.open('icons_resized/' + '#D773F8.png')
_DC91FF = Image.open('icons_resized/' + '#DC91FF.png')
_DFD101 = Image.open('icons_resized/' + '#DFD101.png')
_E5459D = Image.open('icons_resized/' + '#E5459D.png')
_FCB500 = Image.open('icons_resized/' + '#FCB500.png')
_FED902 = Image.open('icons_resized/' + '#FED902.png')
_FEE511 = Image.open('icons_resized/' + '#FEE511.png')
_FF2BC1 = Image.open('icons_resized/' + '#FF2BC1.png')
_FF4A1A = Image.open('icons_resized/' + '#FF4A1A.png')
_FF5EF8 = Image.open('icons_resized/' + '#FF5EF8.png')
_FF7C01 = Image.open('icons_resized/' + '#FF7C01.png')
_FF4477 = Image.open('icons_resized/' + '#FF4477.png')
_FF9101 = Image.open('icons_resized/' + '#FF9101.png')


COLORS = (
    (rgbToHsv(hexToRgb('#00AECC')), '#00AECC'),
    (rgbToHsv(hexToRgb('#00E678')), '#00E678'),
    (rgbToHsv(hexToRgb('#01BFBB')), '#01BFBB'),
    (rgbToHsv(hexToRgb('#2EBFB1')), '#2EBFB1'),
    (rgbToHsv(hexToRgb('#3CEFA5')), '#3CEFA5'),
    (rgbToHsv(hexToRgb('#8E8086')), '#8E8086'),
    (rgbToHsv(hexToRgb('#37E6D4')), '#37E6D4'),
    (rgbToHsv(hexToRgb('#54AFFF')), '#54AFFF'),
    (rgbToHsv(hexToRgb('#82A5AE')), '#82A5AE'),
    (rgbToHsv(hexToRgb('#87BBF7')), '#87BBF7'),
    (rgbToHsv(hexToRgb('#87EB01')), '#87EB01'),
    (rgbToHsv(hexToRgb('#97A9FF')), '#97A9FF'),
    (rgbToHsv(hexToRgb('#A598B5')), '#A598B5'),
    (rgbToHsv(hexToRgb('#AEBAD8')), '#AEBAD8'),
    (rgbToHsv(hexToRgb('#B0FC01')), '#B0FC01'),
    (rgbToHsv(hexToRgb('#BD84F4')), '#BD84F4'),
    (rgbToHsv(hexToRgb('#C10508')), '#C10508'),
    (rgbToHsv(hexToRgb('#D5E64F')), '#D5E64F'),
    (rgbToHsv(hexToRgb('#D773F8')), '#D773F8'),
    (rgbToHsv(hexToRgb('#DC91FF')), '#DC91FF'),
    (rgbToHsv(hexToRgb('#DFD101')), '#DFD101'),
    (rgbToHsv(hexToRgb('#E5459D')), '#E5459D'),
    (rgbToHsv(hexToRgb('#FCB500')), '#FCB500'),
    (rgbToHsv(hexToRgb('#FED902')), '#FED902'),
    (rgbToHsv(hexToRgb('#FEE511')), '#FEE511'),
    (rgbToHsv(hexToRgb('#FF2BC1')), '#FF2BC1'),
    (rgbToHsv(hexToRgb('#FF4A1A')), '#FF4A1A'),
    (rgbToHsv(hexToRgb('#FF5EF8')), '#FF5EF8'),
    (rgbToHsv(hexToRgb('#FF7C01')), '#FF7C01'),
    (rgbToHsv(hexToRgb('#FF4477')), '#FF4477'),
    (rgbToHsv(hexToRgb('#FF9101')), '#FF9101'),
)


parser = argparse.ArgumentParser("image2adobe")
parser.add_argument("--input", type=str, help="Path to input image")
parser.add_argument("--output", type=str, default="final.png", help="Path to output image")
parser.add_argument("--quality", type=str, default="medium", choices=["low", "medium", "high"], help="low = 25 X ?, medium = 50 X ?, high = 100 X ?")
args = parser.parse_args()


if args.quality == 'low':
    size = 25
elif args.quality == 'medium':
    size = 50
elif args.quality == 'high':
    size = 100

image_type = args.input.split('.')[1]

img = Image.open(args.input)
(x, y) = img.size

if image_type == 'jpg' or image_type == 'png':
    if x > 2 * y or y > 2 * x:
        print('Image is too long. One side can\'t be more than two times longer than the other.')

    else :
        if x > y:
            y = round(y * size / x)
            x = size
        elif x == y:
            x = size
            y = size
        elif x < y:
            x = round(x * size / y)
            y = size

        img_resize = img.resize((x, y))
        img_resize.save(args.input.split('.')[0] + '-resized.png')

        blank = Image.new('RGB', (x * 25, y * 25), color='white')

        im = Image.open(args.input.split('.')[0] + '-resized.png')
        pix = im.load()

        for i in range(0, x):
            for j in range(0, y):
                paste(i, j)

        blank.save(args.output)

else:
    print('The type of image is not supported. Only .jpg and .png are allowed.')


