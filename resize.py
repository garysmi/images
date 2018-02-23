import Image

#infile = "/home/gary/Pictures/2018-02-22 07-43-37.png"
infile = "/home/gary/Pictures/2017-02-12 11.27.05.jpg"
#infile = "/home/gary/Pictures/20171018_151735.jpg"
outfile = "/tmp/thumb.jpg"

try:
    im = Image.open(infile)
    orig_w, orig_h = im.size

    if orig_w > orig_h:
        orig_ratio = float(orig_w) / float(orig_h)
        new_w = float(200) * orig_ratio
        print new_w
        size = new_w, 200
        im.thumbnail(size)
        offset = int((new_w - 200) /2)
        print offset
        im = im.crop((offset,0,(200 + offset),200))
    else:
        orig_ratio = float(orig_h) / float(orig_w)
        new_h = float(200) * orig_ratio
        size = 200, new_h
        im.thumbnail(size)
        offset = int((new_h - 200) /2)
        im = im.crop((0,offset, 200, (200 + offset)))

    im.save(outfile, "JPEG")
except IOError:
    print "cannot create thumbnail for", infile