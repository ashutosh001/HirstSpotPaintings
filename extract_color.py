import colorgram

def extract_colors(file,n):
    """Extracts n colors from image file using colorgram and returns (r,g,b) for each color"""
    print("Extracting colors...")
    colors = []
    for color in colorgram.extract(file, n):
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r > 200 and g > 200 and b > 200:
            #rejecting whitish colors
            continue
        colors.append((r,g,b))
    return colors
    

if __name__ == "__main__":
    print(extract_colors('images/hirst_painting.jpg', 10))