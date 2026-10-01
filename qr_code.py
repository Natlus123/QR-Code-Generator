import tkinter as tk
from tkinter import filedialog

import qrcode
from PIL import Image, ImageTk
PREVIEW_SIZE = 300


def createQR(url):
    code = qrcode.QRCode()
    code.add_data(url)
    code.make(fit = True)
    return code.make_image(fill_color = "black", back_color = "white").get_image().convert("RGB")

class QRGui:
    def __init__(self, root):
        root.title("QR-Code-Generator")
        root.resizable(False, False)

        self.image = None
        self.photo = None

        frame = tk.Frame(root, padx=15, pady=15)
        frame.pack()

        tk.Label(frame, text= "Enter the URL or plaintext: ").pack(anchor = "w")
        self.entry = tk.Entry(frame, width = 40)
        self.entry.pack(fill = "x", pady = (0, 10))
        self.entry.bind("<Return>", lambda event: self.generate())
        self.entry.focus()

        tk.Button(frame, text = "Generate", command = self.generate).pack(fill = "x")

        self.preview = tk.Label(frame)
        self.preview.pack(pady = 10)
        self.show(Image.new("RGB", (PREVIEW_SIZE, PREVIEW_SIZE), "#eeeeee"))

        self.save_button = tk.Button(frame, text = "Save as PNG", state = "disabled", command = self.save)
        self.save_button.pack(fill = "x")

        self.status = tk.Label(frame, text = "", fg = "gray")
        self.status.pack(pady = (10, 0))

    def show(self, image):
        small = image.resize((PREVIEW_SIZE, PREVIEW_SIZE), Image.Resampling.NEAREST)
        self.photo = ImageTk.PhotoImage(small)
        self.preview.config(image = self.photo)

    def generate(self):
        url = self.entry.get().strip()
        if not url:
            self.status.config(url = "Please enter an URL or plaintext.")
            return
        try:
            self.image = createQR(url)
        except Exception as error:
            self.status.config(url = f"Error: {error}")
            return
        self.show(self.image)
        self.save_button.config(state = "normal")
        self.status.config(text = "QR Code successfully generated :)")

    def save(self):
        path = filedialog.asksaveasfilename(
            defaultextension = ".png", filetypes = [("PNG image", "*.png")]
        )
        if path:
            self.image.save(path)
            self.status.config(text = f"Saved to {path}")

if __name__ == "__main__":
    root = tk.Tk()
    QRGui(root)
    root.mainloop()

