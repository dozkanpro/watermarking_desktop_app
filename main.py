import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageDraw, ImageFont

GREEN = "#008170"
logo_path = None


# Function to add watermark to the image
def add_watermark():
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])

    if not image_path:
        return

    image = Image.open(image_path)

    watermark_text = watermark_entry.get()
    watermark_position = (int(watermark_x_entry.get()), int(watermark_y_entry.get()))
    watermark_color = watermark_color_var.get()
    font_size = int(font_size_entry.get())
    font = ImageFont.truetype("arial.ttf", size=font_size)

    draw = ImageDraw.Draw(image)
    draw.text(watermark_position, watermark_text, fill=watermark_color, font=font)

    if logo_path:
        logo = Image.open(logo_path)
        image.paste(logo, (10, 10))

    image_with_watermark_path = "output_image.png"
    image.save(image_with_watermark_path)

    result_label.config(text="Watermark added successfully!", fg=GREEN, font=('Arial', 12, 'bold'))

    img = tk.PhotoImage(file=image_with_watermark_path)
    image_label.config(image=img)
    image_label.image = img


def select_logo():
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if logo_path:
        logo_label.config(text="Logo: " + logo_path)


def select_color():
    color = colorchooser.askcolor()[1]
    watermark_color_var.set(color)


app = tk.Tk()
app.title("Image Watermark Tool")
app.minsize(height=400, width=300)

watermark_label = tk.Label(app, text="Watermark Text:", font=('Arial', 11, 'bold'))
watermark_label.pack()
watermark_entry = tk.Entry(app)
watermark_entry.focus()
watermark_entry.pack()

position_label = tk.Label(app, text="Watermark Position (X, Y):", font=('Arial', 11, 'bold'))
position_label.pack()
watermark_x_entry = tk.Entry(app)
watermark_x_entry.pack()
watermark_y_entry = tk.Entry(app)
watermark_y_entry.pack()

font_size_label = tk.Label(app, text="Font Size:", font=('Arial', 11, 'bold'))
font_size_label.pack()
font_size_entry = tk.Entry(app)
font_size_entry.pack()

watermark_color_label = tk.Label(app, text="Watermark Color:", font=('Arial', 11, 'bold'))
watermark_color_label.pack()
watermark_color_var = tk.StringVar()
watermark_color_entry = tk.Entry(app, textvariable=watermark_color_var)
watermark_color_entry.pack()
color_button = tk.Button(app, text="Select Color", command=select_color, font=('Arial', 9, 'bold'))
color_button.pack()

logo_label = tk.Label(app, text="Logo: None", font=('Arial', 11, 'bold'))
logo_label.pack()
select_logo_button = tk.Button(app, text="Select Logo", command=select_logo, font=('Arial', 9, 'bold'))
select_logo_button.pack()

apply_button = tk.Button(app, text="Apply", command=add_watermark, font=('Arial', 9, 'bold'), width=10, bg=GREEN)
apply_button.pack(pady=20)

result_label = tk.Label(app, text="")
result_label.pack()

image_label = tk.Label(app)
image_label.pack()

app.mainloop()
