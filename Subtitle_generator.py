from PIL import Image,ImageFont,ImageDraw
from io import BytesIO
import win32clipboard
from sys import argv

def image_to_clipboard(Image):
    output = BytesIO()
    Image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def split_message(str: str, row_lenght: int):
    words = str.split()
    r1 = ""
    r2 = ""
    r3 = ""
    amount = 0

    for word in words:
        for letter in word:
            amount += 1
        if amount < row_lenght:
            r1 = r1 + " " + word
            amount += 1
        else:
            if amount < row_lenght * 2:
                r2 = r2 + " " + word
                amount += 1
            else:
                if amount < row_lenght * 3:
                    r3 = r3 + " " + word
                    amount += 1

    return (r1[1:], r2[1:], r3[1:])

try:
    test_open_with = argv[1]
    open_with = True
except IndexError:
    open_with = False

if open_with == True:
    path = argv[1]
else:
    from tkinter import Tk
    from tkinter import filedialog
    root = Tk()
    root.title("Subtitle generator")
    path = filedialog.askopenfilename(title = "Select a file", filetypes=(("Image files",'*.png; *.jpg'),("All files", "*.*")))
Image = Image.open(path)
W, H = Image.size
msg = input("enter the subtitle text: ")
#45
size = int((H + W) / 45)
#size = int((H + W) / 45)
blackWidh = int((H + W) / 350)
blackWidh2 = int(blackWidh * 1.4)
myFont = ImageFont.truetype("trebuc.ttf", size)
stroke_color = 000,000,000
draw = ImageDraw.Draw(Image)
print(size)
print(W)
row_lenght = 55
#row_lenght = round(size - (W / 320))
print(row_lenght)
r1,r2,r3 = split_message(msg,row_lenght)

if r2 == "":
    w, h = draw.textsize(r1, font=myFont)
    draw.text((((W-w)/2)*1.006,((H-h)/1.05)*1.007), r1, fill="Black",stroke_width=blackWidh,stroke_fill=stroke_color, font=myFont)
    draw.text(((W-w)/2,(H-h)/1.05), r1, fill="White",stroke_width=blackWidh2,stroke_fill=stroke_color, font=myFont)
else:
    if r3 == "":
        w, h = draw.textsize(r2, font=myFont)
        draw.text((((W-w)/2)*1.006,((H-h)/1.05)*1.007), r2, fill="Black",stroke_width=blackWidh,stroke_fill=stroke_color, font=myFont)
        draw.text(((W-w)/2,(H-h)/1.05), r2, fill="White",stroke_width=blackWidh2,stroke_fill=stroke_color, font=myFont)

        w, h = draw.textsize(r1, font=myFont)
        draw.text((((W-w)/2)*1.006,((H-h)/1.15)*1.007), r1, fill="Black",stroke_width=blackWidh,stroke_fill=stroke_color, font=myFont)
        draw.text(((W-w)/2,(H-h)/1.15), r1, fill="White",stroke_width=blackWidh2,stroke_fill=stroke_color, font=myFont)

    else :
        w, h = draw.textsize(r1, font=myFont)
        draw.text((((W-w)/2)*1.006,((H-h)/1.27)*1.007), r1, fill="Black",stroke_width=blackWidh,stroke_fill=stroke_color, font=myFont)
        draw.text(((W-w)/2,(H-h)/1.27), r1, fill="White",stroke_width=blackWidh2,stroke_fill=stroke_color, font=myFont)

        w, h = draw.textsize(r2, font=myFont)
        draw.text((((W-w)/2)*1.006,((H-h)/1.15)*1.007), r2, fill="Black",stroke_width=blackWidh,stroke_fill=stroke_color, font=myFont)
        draw.text(((W-w)/2,(H-h)/1.15), r2, fill="White",stroke_width=blackWidh2,stroke_fill=stroke_color, font=myFont)

        w, h = draw.textsize(r3, font=myFont)
        draw.text((((W-w)/2)*1.006,((H-h)/1.05)*1.007), r3, fill="Black",stroke_width=blackWidh,stroke_fill=stroke_color, font=myFont)
        draw.text(((W-w)/2,(H-h)/1.05), r3, fill="White",stroke_width=blackWidh2,stroke_fill=stroke_color, font=myFont)





image_to_clipboard(Image)
quit()
Image.show()

save = str(input("save image?: "))

#55
if save.lower().startswith('y'):
    fsi = path[:-4]
    Image.save(f"{fsi} _Sub.png")