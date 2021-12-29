import io

import PySimpleGUI as sg

from PIL import Image, ImageTk


def get_img_data(f, maxsize=(1200, 850), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)


file_list_column = [
    [
        sg.Text("Open an image: "),
        sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
        sg.FileBrowse(),
    ],
    [
        sg.DropDown(values=["1", "2", "3"])
    ]
]

image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column)
    ]
]

# Create the window
window = sg.Window("PhotographerMacros", layout, resizable=True)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

    if event == "-FILE-":

        filename = values["-FILE-"]
        print(f"File to open = {filename}")
        window["-IMAGE-"].update(filename=filename)
        image_elem.update(data=get_img_data(filename, first=True))

window.close()