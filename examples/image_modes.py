"""Demonstrate the image display modes of the PictureBox."""

import tkinter as tk
from tkinter import Tk
from opencv_tk import PictureBox, BorderStyle, ImageMode

options = {
    'Normal': ImageMode.Normal,
    'Center': ImageMode.CenterImage,
    'Stretch': ImageMode.StretchImage,
    'Zoom': ImageMode.Zoom,
}


class DemoWindow(tk.Frame):
    """The PictureBox demo window."""

    def __init__(self, master: Tk) -> None:
        """Construct the PictureBox demo window."""
        super().__init__(master, bd=3, relief='ridge', pady=10)
        master.resizable(False, False)
        master.title('Image Display Modes')
        self.pack()

        self._picture_box = PictureBox(self, 840, 520)
        self._picture_box.set_background('silver')
        self._picture_box.load('images/flowers.jpg')
        self._picture_box.border_style = BorderStyle.Solid
        self._picture_box.grid(row=0, column=0, padx=(10, 5))

        self._image_mode = tk.IntVar(self, value=self._picture_box.image_mode)
        mode_group = tk.LabelFrame(self, text='Image Modes')
        for i, name in enumerate(options):
            mode = tk.Radiobutton(
                mode_group,
                text=name,
                value=options[name],
                variable=self._image_mode,
                command=self._on_mode_change,
            )
            mode.grid(row=i, column=0, padx=20, pady=5, sticky='w')
        mode_group.grid(row=0, column=1, padx=15, sticky='n')

    def _on_mode_change(self) -> None:
        """Set the selected image display mode."""
        self._picture_box.image_mode = self._image_mode.get()


if __name__ == "__main__":
    root = Tk()
    main_form = DemoWindow(root)
    main_form.mainloop()
