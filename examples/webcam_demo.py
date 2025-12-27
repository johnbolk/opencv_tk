"""Using a PictureBox to display live video from a webcam."""

import tkinter as tk
import cv2
from opencv_tk import PictureBox, BorderStyle, ImageMode


class DemoWindow(tk.Frame):
    """The PictureBox demo window."""

    def __init__(self, root, camera):
        """Construct the PictureBox demo window."""
        super().__init__(root, bd=3, relief='ridge')
        root.resizable(False, False)
        root.title('PictureBox Demo')
        self.pack()

        self._picture_box = PictureBox(self, 400, 300)
        self._picture_box.border_style = BorderStyle.Sunken
        self._picture_box.image_mode = ImageMode.StretchImage
        self._picture_box.pack(padx=10, pady=10)

        self._camera = camera
        self._display_video()

    def _display_video(self):
        """Continuously read and display a new video frame."""
        success, frame = self._camera.read()
        if success:
            self._picture_box.display(frame)
        self.after(10, self._display_video)


if __name__ == '__main__':
    webcam = cv2.VideoCapture(0)
    if webcam.isOpened():
        demo_window = DemoWindow(tk.Tk(), webcam)
        demo_window.mainloop()
        webcam.release()
    else:
        print('No webcam was detected!')
