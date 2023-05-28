import io
import os.path

import PySimpleGUI as sg

from PIL import Image, ImageTk
from models.folder_view_file import FolderViewFiles


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


class FolderView:
    def __init__(self):
        pass

    def main_loop(self):
        """
        The main program that contains the event loop.
        It will call the make_window function to create the window.
        """

        icon = sg.EMOJI_BASE64_HAPPY_IDEA
        sg.user_settings_filename('psgdemos.json')
        sg.set_options(icon=icon)

        files = self.__load_files('/home/lyubolp/PhotographerMacros/sample')

        window = self.__make_window()
        window.force_focus()

        window['FILES_LIST'].update(values=files.get_filenames())
        while True:
            event, values = window.read()

            print(event, values)

            if event in (sg.WINDOW_CLOSED, 'Exit'):
                break

            if event == 'FILES_LIST':
                filename = values['FILES_LIST'][0]
                file = files.get_file_by_filename(filename)

                image_window_size = window['-IMAGE-'].Size
                print(image_window_size)
                image_data = get_img_data(file.path, first=True, maxsize=image_window_size)

                window['-IMAGE-'].update(data=image_data)

        window.close()

    @staticmethod
    def __load_files(path: str) -> FolderViewFiles:
        files = FolderViewFiles(path)

        for dirname, _, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirname, filename)
                files.add_file(filename, full_path)

        return files

    @staticmethod
    def __make_window():
        """
        Creates the main window
        :return: The main window object
        :rtype: (sg.Window)
        """
        theme = sg.OFFICIAL_PYSIMPLEGUI_THEME
        sg.theme(theme)

        left_col = sg.Column([
            [sg.Listbox(values=[], select_mode=sg.SELECT_MODE_SINGLE, size=(50, 20),
                        bind_return_key=True, key='FILES_LIST',
                        expand_x=True, expand_y=True, enable_events=True)],
            [sg.Button('Mark'), sg.B('Copy marked images to...')],
        ], element_justification='l', expand_x=True, expand_y=True)

        right_col = [
            [
                sg.Image(key="-IMAGE-", source=sg.EMOJI_BASE64_HAPPY_IDEA,
                         expand_x=True, expand_y=True, size=(500, 500))
            ],
            [sg.Button('Previous'), sg.Button('Next')],
        ]

        choose_folder_at_top = sg.pin(
            sg.Column([[sg.T('Choose a directory'),
                        sg.Combo(sorted(sg.user_settings_get_entry('-folder names-', [])),
                                 default_value=sg.user_settings_get_entry('-demos folder-', ''),
                                 size=(50, 30), key='-FOLDERNAME-',
                                 enable_events=True, readonly=True)]],
                      pad=(0, 0), k='-FOLDER CHOOSE-'))
        # ----- Full layout -----

        layout = [
            [sg.Text('PySimpleGUI Demo Program & Project Browser', font='Any 20')],
            [choose_folder_at_top],
            [sg.Pane([
                sg.Column([[left_col], ], element_justification='l', expand_x=True, expand_y=True),
                sg.Column(right_col, element_justification='c', expand_x=True, expand_y=True)],
                orientation='h', relief=sg.RELIEF_SUNKEN,
                expand_x=True, expand_y=True, key='-PANE-')]]

        # --------------------------------- Create Window ---------------------------------
        window = sg.Window('PSG Demo & Project Browser', layout, finalize=True,  resizable=True,
                           use_default_focus=False,
                           right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)
        window.set_min_size(window.size)

        window.bring_to_front()
        return window


if __name__ == '__main__':
    folder_view = FolderView()
    folder_view.main_loop()
