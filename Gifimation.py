import io
import os
import sys
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, simpledialog, Text, Frame
from PIL import Image, ImageDraw, ImageTk, ImageFont
import urllib.request


class AgreementSplash:
    """Startup Splash Screen for the Cranbero License Agreement"""
    def __init__(self, root):
        self.root = root
        self.root.title("Gifimation - License Agreement")
        self.root.geometry("450x300")
        self.root.resizable(False, False)

        frame = tk.Frame(root, padx=20, pady=20, bg="#f5f5f5")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            frame, 
            text="Welcome to Gifimation by 17YZX", 
            font=("Arial", 14, "bold"), 
            bg="#f5f5f5"
        ).pack(pady=(0, 15))

        agreement_text = (
            "By using Gifimation you agree to our Cranbero License.\n\n"
            "Please review the terms in the application menu "
            "if needed before proceeding."
        )
        
        tk.Label(
            frame, 
            text=agreement_text, 
            font=("Arial", 10), 
            bg="#f5f5f5", 
            justify=tk.CENTER,
            wraplength=380
        ).pack(pady=(0, 20))

        agree_btn = tk.Button(
            frame, 
            text="Agree", 
            command=self.open_main_studio, 
            bg="#4caf50", 
            fg="white", 
            font=("Arial", 11, "bold"),
            width=15,
            height=2
        )
        agree_btn.pack()

    def open_main_studio(self):
        self.root.destroy()
        main_root = tk.Tk()
        GifimationStudio(main_root)
        main_root.mainloop()


class GifimationStudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Gifimation by 17YZX")
        self.root.geometry("1050x720")
        self.root.minsize(950, 680)

        self.canvas_width = 750
        self.canvas_height = 640

        # State variables
        self.current_tool = "drag"
        self.brush_color = "#000000"
        self.brush_size = 5
        self.frames = []
        self.canvas_elements = [] 
        self.selected_element_idx = None
        self.draw_start_x = None
        self.draw_start_y = None

        # Load Logo & Set Icon
        self.logo_img = self.load_logo_from_url()
        if self.logo_img:
            try:
                self.root.iconphoto(True, ImageTk.PhotoImage(self.logo_img))
            except Exception:
                pass

        # --- Cranbero License Text ---
        self.cranbero_license_text = """Cranbero License
Version 26.0.3 October, 2026

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
Established by Seok-bong, Hunter Tigner.

1. Redistributing base-projects
You may redistribute base projects, but if the code includes a 0.6:1.0 similarity ratio, this exceeds the usage permissions and is code plagiarism, as mentioned in Term 3. Term 8 and Term 9 may apply. 

2. Authors of base-project
If an author's name of any kind (display, user, email, real, and other similar things.) exceeds 25 characters, a separate CREDITS file may be used. The NOTICE file must reference the CREDITS file. this is to prevent abuse so base-project author can't abuse and bloat NOTICE file with 1,000 letters to be annoying 

3. Usage Permissions
By using the project, you can copy an amount of 0.3:1.0 similarity ratio, pass: This exceeds the usage permissions being code plagiarism, and abuses the license. It may result in an immediate cease-and-desist, a DMCA takedown, or license revocation under Section 9.

4. Brand Identity 
Logos may not exceed a 0.6:1.0 similarity ratio, and banners may not exceed 0.1:1.0. Exceeding these limits is considered brand theft, resulting in an immediate Cease-and-Desist, DMCA Takedown, or license revocation under Section 9.

5. Expiration Date
Expiration Date (Optional by base-project) Expiration date is optional for creators of base-project but must include a valid date within 0 to 2 years. Expiration date is optional for the base-project. Expiration date is optional. Use this if you don't want people copying your project to make their own project based on yours, and you don't want them using base-project forever as their default.

6. Limitation Of Liability for (new-project / base-project)
Damage of individuals computer, is not new-projects fault if new-project includes 0-10% harm rate (0-10% means file-move, file-delete, no system-breaks,) if more than 10% or more than list described, than new-project is at fault of visitors computer breaking.

7. Severability  
redistributing the new-project and converting it into an illegal new-project, with source-code that violates laws in countries mentioned: United States, Benin, Mexico. As this may cause you to go to jail or cause A lawsuit between A user and the author of new-project but also visitors, visiting new-project.

8. Revocation time
Revocation Time (Required by base-project) Revocation Time is required for creators of base-project but must include a valid date within 70 to 125 days. Revocation Time date is required for the base-project. Revocation Time is required.  
this is for if the base-project creators, don't want people immediately coming back to use base-project after 70 days.

9. Revocation of rights
$250-fine if the base-project contains, 95 assets, with 5,000 lines of program-code (not text)
$1,000-fine if the base-project contains, 190 assets, with 6,250 lines of program-code (not text)
$4,000-fine if the base-project contains, 380 assets, with 8,560 lines of program-code (not text)

10. Previous License Versions
Any individual developer/team/company using previous license versions will stay on that license until they decide to update it. If not, they will continue on the old license version with the exact replica of the original license terms and conditions.

11. Dictionary
$-fine = An owed amount of money, to use base-project, again if new-project revocations of rights.
Revocation = Revoking rights and crossing the line 
0.N:1.0 = Ratio of how similar a project can be. The third digit "N" is A number if it is A number 1-9 it means the percentage multiplied by 10, 0.5:1.0 = (50%/100%)
Individual = Human using the software, new-project or base-project 
Individual developer = human creating a new project or base project. 
Team = A small group of humans (5-35) that have created a new-project or base-project 
Company = A large group of humans (100-5,000) that have created a new project or base project 

12. Limitation Of Liability for (Cranbero)
Any individual developer/team/company using this license, if anything goes wrong using the license, for example, to abuse it: you can send feedback, but not sue us. If any individual computer has broken or passed the 0-10% harm rate, any individual cannot do any suing to Cranbero License due to, we have no fault creator is at fault if goes wrong within 0-10% harm-rate, if A individual/team/company using this license detects A abuse switch to A safer license or closed-source while we fix the abuse."""

        # --- Main Layout Container ---
        self.main_container = Frame(root)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.create_menu_bar()
        self.create_studio_ui()

    def load_logo_from_url(self):
        """Downloads logo from the provided URL."""
        try:
            url = "https://i.ibb.co/39gvqrF9/Screenshot-2026-10-17-142427.png"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                image_data = response.read()
                image = Image.open(io.BytesIO(image_data))
                return image
        except Exception:
            return None

    def create_menu_bar(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Export Animated GIF", command=self.export_gif)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        license_menu = tk.Menu(menubar, tearoff=0)
        license_menu.add_command(label="View Cranbero License", command=self.show_license_in_app)
        menubar.add_cascade(label="Cranbero License", menu=license_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About Gifimation", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def show_license_in_app(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

        lic_frame = Frame(self.main_container, bg="#f9f9f9")
        lic_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        tk.Label(lic_frame, text="📜 Cranbero License (Version 26.0.3)", font=("Arial", 14, "bold"), bg="#f9f9f9").pack(anchor="w", pady=(0, 10))
        tk.Button(lic_frame, text="⬅ Back to Studio", command=self.return_to_studio, bg="#2196f3", fg="white", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 10))

        text_area = Text(lic_frame, wrap=tk.WORD, padx=10, pady=10, font=("Courier", 9))
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(lic_frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)

        text_area.insert(tk.END, self.cranbero_license_text)
        text_area.config(state=tk.DISABLED)

    def return_to_studio(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()
        self.create_studio_ui()
        self.redraw_canvas()

    def show_about(self):
        messagebox.showinfo("About Gifimation", "Gifimation by 17YZX\nAn interactive animation and paint studio built with Tkinter and Pillow.")

    def create_studio_ui(self):
        toolbar = tk.Frame(self.main_container, width=260, bg="#f0f0f0", padx=10, pady=10)
        toolbar.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # Display Logo in Toolbar if loaded successfully
        if self.logo_img:
            try:
                thumb = self.logo_img.copy()
                thumb.thumbnail((120, 60))
                self.logo_tk = ImageTk.PhotoImage(thumb)
                tk.Label(toolbar, image=self.logo_tk, bg="#f0f0f0").pack(pady=(0, 5))
            except Exception:
                pass

        tk.Label(toolbar, text="🎬 Gifimation by 17YZX", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 5))

        tools_frame = tk.Frame(toolbar, bg="#f0f0f0")
        tools_frame.pack(fill=tk.X, pady=5)

        tk.Button(tools_frame, text="👆 Drag/Move", command=lambda: self.set_tool("drag"), width=12).grid(row=0, column=0, padx=2, pady=2)
        tk.Button(tools_frame, text="🖌 Paint Brush", command=lambda: self.set_tool("draw"), width=12).grid(row=0, column=1, padx=2, pady=2)
        tk.Button(tools_frame, text="⬛ Rectangle", command=lambda: self.set_tool("rectangle"), width=12).grid(row=1, column=0, padx=2, pady=2)
        tk.Button(tools_frame, text="⭕ Oval/Circle", command=lambda: self.set_tool("oval"), width=12).grid(row=1, column=1, padx=2, pady=2)
        tk.Button(tools_frame, text="🔺 Triangle", command=lambda: self.set_tool("triangle"), width=12).grid(row=2, column=0, padx=2, pady=2)
        tk.Button(tools_frame, text="➖ Line", command=lambda: self.set_tool("line"), width=12).grid(row=2, column=1, padx=2, pady=2)
        tk.Button(tools_frame, text="🔤 Times Text", command=lambda: self.set_tool("text"), width=12).grid(row=3, column=0, padx=2, pady=2)
        tk.Button(tools_frame, text="📁 Upload Media", command=self.upload_image_or_gif, width=12, bg="#ffecb3").grid(row=3, column=1, padx=2, pady=2)

        tk.Label(toolbar, text="", bg="#f0f0f0").pack()

        # Style Options
        style_frame = tk.LabelFrame(toolbar, text=" Style Options ", bg="#f0f0f0", padx=5, pady=5)
        style_frame.pack(fill=tk.X, pady=5)

        tk.Button(style_frame, text="🎨 Choose Color", command=self.choose_color, bg="#e0e0e0", width=20).pack(pady=3)
        tk.Label(style_frame, text="Size / Thickness:", bg="#f0f0f0").pack(anchor="w")
        self.size_slider = tk.Scale(style_frame, from_=1, to=50, orient=tk.HORIZONTAL, bg="#f0f0f0")
        self.size_slider.set(5)
        self.size_slider.pack(fill=tk.X, pady=2)

        tk.Label(toolbar, text="", bg="#f0f0f0").pack()

        # Animation Controls
        anim_frame = tk.LabelFrame(toolbar, text=" Animation Controls ", bg="#f0f0f0", padx=5, pady=5)
        anim_frame.pack(fill=tk.X, pady=5)

        tk.Button(anim_frame, text="📸 Capture Frame", command=self.capture_frame, bg="#4caf50", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)
        self.frame_label = tk.Label(anim_frame, text=f"Frames captured: {len(self.frames)}", bg="#f0f0f0", font=("Arial", 9))
        self.frame_label.pack(pady=2)

        tk.Button(anim_frame, text="💾 Export GIF", command=self.export_gif, bg="#2196f3", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)
        tk.Button(anim_frame, text="🗑 Clear All Frames", command=self.clear_frames, bg="#f44336", fg="white", width=22).pack(pady=2)
        tk.Button(anim_frame, text="🧹 Clear Canvas", command=self.clear_canvas, bg="#9e9e9e", fg="white", width=22).pack(pady=2)

        # Canvas Frame
        canvas_frame = Frame(self.main_container, bg="#dddddd", bd=2, relief=tk.SUNKEN)
        canvas_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.canvas = tk.Canvas(canvas_frame, width=self.canvas_width, height=self.canvas_height, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

    def set_tool(self, tool_name):
        self.current_tool = tool_name
        self.root.title(f"Gifimation by 17YZX — Active Tool: {tool_name.upper()}")

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Color")
        if color_code[1]:
            self.brush_color = color_code[1]

    def upload_image_or_gif(self):
        file_path = filedialog.askopenfilename(
            title="Select Image or GIF",
            filetypes=[("Image/GIF Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        try:
            pil_img = Image.open(file_path).convert("RGBA")
            if pil_img.width > 250 or pil_img.height > 250:
                pil_img.thumbnail((250, 250))

            element = {
                "type": "image",
                "x": 100, "y": 100,
                "pil_img": pil_img
            }
            self.canvas_elements.append(element)
            self.redraw_canvas()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image: {e}")

    def clear_canvas(self):
        self.canvas_elements.clear()
        self.redraw_canvas()

    def on_canvas_click(self, event):
        self.brush_size = self.size_slider.get()

        if self.current_tool == "drag":
            self.selected_element_idx = None
            for idx, el in enumerate(reversed(self.canvas_elements)):
                ex, ey = el.get("x", 0), el.get("y", 0)
                if ex <= event.x <= ex + 150 and ey <= event.y <= ey + 150:
                    self.selected_element_idx = len(self.canvas_elements) - 1 - idx
                    break
        elif self.current_tool == "draw":
            self.draw_start_x = event.x
            self.draw_start_y = event.y
        elif self.current_tool in ["rectangle", "oval", "triangle", "line"]:
            self.draw_start_x = event.x
            self.draw_start_y = event.y
        elif self.current_tool == "text":
            text_val = simpledialog.askstring("Add Text", "Enter text (Times New Roman):")
            if text_val:
                element = {
                    "type": "text",
                    "x": event.x, "y": event.y,
                    "text": text_val,
                    "color": self.brush_color,
                    "size": max(12, self.brush_size * 2)
                }
                self.canvas_elements.append(element)
                self.redraw_canvas()

    def on_canvas_drag(self, event):
        if self.current_tool == "drag" and self.selected_element_idx is not None:
            el = self.canvas_elements[self.selected_element_idx]
            el["x"] = event.x
            el["y"] = event.y
            self.redraw_canvas()
        elif self.current_tool == "draw":
            if self.draw_start_x and self.draw_start_y:
                element = {
                    "type": "line_segment",
                    "x1": self.draw_start_x, "y1": self.draw_start_y,
                    "x2": event.x, "y2": event.y,
                    "color": self.brush_color,
                    "width": self.brush_size
                }
                self.canvas_elements.append(element)
                self.draw_start_x = event.x
                self.draw_start_y = event.y
                self.redraw_canvas()

    def on_canvas_release(self, event):
        self.selected_element_idx = None
        if self.current_tool in ["rectangle", "oval", "triangle", "line"] and self.draw_start_x is not None:
            element = {
                "type": self.current_tool,
                "x1": self.draw_start_x, "y1": self.draw_start_y,
                "x2": event.x, "y2": event.y,
                "color": self.brush_color,
                "width": self.brush_size
            }
            self.canvas_elements.append(element)
            self.redraw_canvas()

        self.draw_start_x = None
        self.draw_start_y = None

    def redraw_canvas(self):
        self.canvas.delete("all")
        self.tk_images_cache = []

        for el in self.canvas_elements:
            etype = el["type"]
            if etype == "rectangle":
                self.canvas.create_rectangle(el["x1"], el["y1"], el["x2"], el["y2"], outline=el["color"], width=el["width"])
            elif etype == "oval":
                self.canvas.create_oval(el["x1"], el["y1"], el["x2"], el["y2"], outline=el["color"], width=el["width"])
            elif etype == "line" or etype == "line_segment":
                self.canvas.create_line(el.get("x1", el.get("x")), el.get("y1", el.get("y")), el["x2"], el["y2"], fill=el["color"], width=el["width"], capstyle=tk.ROUND)
            elif etype == "triangle":
                x1, y1, x2, y2 = el["x1"], el["y1"], el["x2"], el["y2"]
                mid_x = (x1 + x2) / 2
                self.canvas.create_polygon(mid_x, y1, x1, y2, x2, y2, outline=el["color"], fill="", width=el["width"])
            elif etype == "text":
                self.canvas.create_text(el["x"], el["y"], text=el["text"], fill=el["color"], font=("Times New Roman", el["size"]), anchor="nw")
            elif etype == "image":
                tk_img = ImageTk.PhotoImage(el["pil_img"])
                self.tk_images_cache.append(tk_img)
                self.canvas.create_image(el["x"], el["y"], image=tk_img, anchor="nw")

    def capture_frame(self):
        img = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        draw = ImageDraw.Draw(img)

        for el in self.canvas_elements:
            etype = el["type"]
            if etype == "rectangle":
                draw.rectangle([el["x1"], el["y1"], el["x2"], el["y2"]], outline=el["color"], width=el["width"])
            elif etype == "oval":
                draw.ellipse([el["x1"], el["y1"], el["x2"], el["y2"]], outline=el["color"], width=el["width"])
            elif etype == "line" or etype == "line_segment":
                draw.line([el.get("x1", el.get("x")), el.get("y1", el.get("y")), el["x2"], el["y2"]], fill=el["color"], width=el["width"])
            elif etype == "triangle":
                x1, y1, x2, y2 = el["x1"], el["y1"], el["x2"], el["y2"]
                mid_x = (x1 + x2) / 2
                draw.polygon([(mid_x, y1), (x1, y2), (x2, y2)], outline=el["color"], width=el["width"])
            elif etype == "text":
                try:
                    if sys.platform.startswith("win"):
                        f = ImageFont.truetype("C:\\Windows\\Fonts\\times.ttf", el["size"])
                    else:
                        f = ImageFont.load_default()
                except:
                    f = ImageFont.load_default()
                draw.text((el["x"], el["y"]), el["text"], fill=el["color"], font=f)
            elif etype == "image":
                pil_sub = el["pil_img"]
                img.paste(pil_sub, (int(el["x"]), int(el["y"])), pil_sub)

        self.frames.append(img)
        self.frame_label.config(text=f"Frames captured: {len(self.frames)}")

    def export_gif(self):
        if not self.frames:
            messagebox.showerror("Error", "No frames captured yet! Capture frames before exporting.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("Animated GIF", "*.gif")])
        if file_path:
            self.frames[0].save(
                file_path,
                save_all=True,
                append_images=self.frames[1:],
                duration=200,
                loop=0
            )
            messagebox.showinfo("Success!", f"Gifimation successfully exported to:\n{file_path}")

    def clear_frames(self):
        self.frames = []
        self.frame_label.config(text=f"Frames captured: {len(self.frames)}")


if __name__ == "__main__":
    splash_root = tk.Tk()
    AgreementSplash(splash_root)
    splash_root.mainloop()
