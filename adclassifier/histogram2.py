try:
    import Image
    import ImageDraw
except ImportError:
    from PIL import Image
    from PIL import ImageDraw


def get_colors(infile, outfile, numcolors=4, swatchsize=200, resize=150):

    image = Image.open(infile)
    image = image.resize((resize, resize))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize * resize)
    print(colors)
    # Save colors to file

    pal = Image.new('RGB', (swatchsize * numcolors, swatchsize))
    draw = ImageDraw.Draw(pal)

    posx = 0
    for count, col in colors:
        draw.rectangle([posx, 0, posx + swatchsize, swatchsize], fill=col)
        posx = posx + swatchsize

    del draw
    pal.save(outfile, "PNG")

if __name__ == '__main__':
    infile = r"D:\ypai\data\image\test\bs-apr5-erica-2016-05-09-23-13-43-601\frame-31.png"
    outfile = r"D:\ypai\data\image\test\bs-apr5-erica-2016-05-09-23-13-43-601\frame-31.jpg"
    get_colors(infile, outfile)
