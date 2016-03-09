import os.path

# modified from http://pseentertainmentcorp.com/smf/index.php?topic=2034.0
import struct, random

# important values: offset, headerlength, width, height and colordepth
# This is for a Windows Version 3 DIB header
# You will likely want to customize the width and height
default_bmp_header = {'mn1':66,
                      'mn2':77,
                      'filesize':0,
                      'undef1':0,
                      'undef2':0,
                      'offset':54,
                      'headerlength':40,
                      'width':200,
                      'height':200,
                      'colorplanes':0,
                      'colordepth':24,
                      'compression':0,
                      'imagesize':0,
                      'res_hor':0,
                      'res_vert':0,
                      'palette':0,
                      'importantcolors':0}

def bmp_write(header, pixels, filename):
    '''It takes a header (based on default_bmp_header), 
    the pixel data (from structs, as produced by get_color and row_padding),
    and writes it to filename'''
    header_str = ""
    header_str += struct.pack('<B', header['mn1'])
    header_str += struct.pack('<B', header['mn2'])
    header_str += struct.pack('<L', header['filesize'])
    header_str += struct.pack('<H', header['undef1'])
    header_str += struct.pack('<H', header['undef2'])
    header_str += struct.pack('<L', header['offset'])
    header_str += struct.pack('<L', header['headerlength'])
    header_str += struct.pack('<L', header['width'])
    header_str += struct.pack('<L', header['height'])
    header_str += struct.pack('<H', header['colorplanes'])
    header_str += struct.pack('<H', header['colordepth'])
    header_str += struct.pack('<L', header['compression'])
    header_str += struct.pack('<L', header['imagesize'])
    header_str += struct.pack('<L', header['res_hor'])
    header_str += struct.pack('<L', header['res_vert'])
    header_str += struct.pack('<L', header['palette'])
    header_str += struct.pack('<L', header['importantcolors'])
    #create the outfile
    outfile = open(filename, 'wb')
    #write the header + pixels
    outfile.write(header_str + pixels)
    outfile.close()

def row_padding(width, colordepth):
    '''returns any necessary row padding'''
    byte_length = width*colordepth/8
    # how many bytes are needed to make byte_length evenly divisible by 4?
    padding = (4-byte_length)%4 
    padbytes = ''
    for i in range(padding):
        x = struct.pack('<B',0)
        padbytes += x
    return padbytes

def pack_color(red, green, blue):
    '''accepts values from 0-255 for each value, returns a packed string'''
    return struct.pack('<BBB',blue,green,red)

def pack_hex_color(hex_color):
    '''accepts RGB hex colors like '#ACE024', returns a packed string'''
    base = 16
    red = int(hex_color[1:3], base)
    green = int(hex_color[3:5], base)
    blue = int(hex_color[5:7], base)
    return pack_color(red, green, blue)

####################################
### the parts I wrote start here ###
####################################

def bmp_return(header, pixels):
    '''It takes a header (based on default_bmp_header), 
    the pixel data (from structs, as produced by get_color and row_padding),
    and writes it to filename'''
    header_str = ""
    header_str += struct.pack('<B', header['mn1'])
    header_str += struct.pack('<B', header['mn2'])
    header_str += struct.pack('<L', header['filesize'])
    header_str += struct.pack('<H', header['undef1'])
    header_str += struct.pack('<H', header['undef2'])
    header_str += struct.pack('<L', header['offset'])
    header_str += struct.pack('<L', header['headerlength'])
    header_str += struct.pack('<L', header['width'])
    header_str += struct.pack('<L', header['height'])
    header_str += struct.pack('<H', header['colorplanes'])
    header_str += struct.pack('<H', header['colordepth'])
    header_str += struct.pack('<L', header['compression'])
    header_str += struct.pack('<L', header['imagesize'])
    header_str += struct.pack('<L', header['res_hor'])
    header_str += struct.pack('<L', header['res_vert'])
    header_str += struct.pack('<L', header['palette'])
    header_str += struct.pack('<L', header['importantcolors'])
    #create the outfile
    return header_str + pixels

def imgCreate(rule,ruleIters,imgWidth):
    '''takes the Automaton criteria and writes the corresponding .bmp file'''
    imgLine = [0 for i in range(imgWidth/2)]+[1]+[0 for i in range(imgWidth/2)]
    imgArray = list([imgLine])
    for j in range(0,ruleIters):
        imgTemp = list()

        for i in range(0,len(imgLine)):
            # bitwise comparison; returns 1 if '1' in that position for both binary values
            if (2**imgInput(imgLine, i) & rule) !=0:
                imgTemp.append(1)
            else:
                imgTemp.append(0)
        imgLine = list(imgTemp)
        imgArray.append(imgTemp)
    return imgDraw(imgArray,rule)

def imgDraw(imgArray, rule):
    '''takes an array of 0s and 1s; writes the corresponding bmp to a file'''
    pixels = ''
    header = default_bmp_header
    header["width"] = len(imgArray[0])
    header["height"] = len(imgArray)
    for row in range(header['height']-1,-1,-1):# (BMPs are L to R from the bottom L row)
        for column in range(header['width']):
            if imgArray[row][column] == 1:
                pixels += pack_hex_color('#000000')
            else:
                pixels += pack_hex_color('#FFFFFF')
        pixels += row_padding(header['width'], header['colordepth'])
    savePath = os.path.join("img/", "cellular_automata_rule-" + str(rule).zfill(3) +".bmp")
    return bmp_return(header,pixels)

def imgVal(imgList,imgIndex):
    '''takes a list of 1s and 0s and an index; returns the value of the requested index in the image, or zero'''
    try:
        return str(imgList[imgIndex])
    except:
        return str(0)

def imgInput(imgList,imgIndex):
    '''takes a list of 1s and 0s and an index; returns an integer representation of the index input value'''
    return int(imgVal(imgList,imgIndex-1)+imgVal(imgList,imgIndex)+imgVal(imgList,imgIndex+1),2)

def imgPrint(imgList):
    '''takes an array of 1s and 0s; prints them'''
    print ' '.join(str(element) for element in imgList)
    
if __name__ == '__main__':
    from sys import argv
    if (len(argv) == 4):
        imgCreate(rule=int(argv[1]),ruleIters=int(argv[2]),imgWidth=int(argv[3]))
    else:
        print("usage: python automaton.py <rule#> <ruleIters> <imgWidth>")
        print("rule suggestions: 13, 18, 28, 45, 57, 73, 75, 93, 94, 99")
        #imgCreate(rule=18,ruleIters=200,imgWidth=401)
