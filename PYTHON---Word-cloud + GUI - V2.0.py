import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

class WordCloudGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Cloud Generator")
        self.root.geometry("400x300")

        # Default settings
        self.file_path = None
        self.bg_color = "white"
        self.max_font_size = 50

        # GUI components
        tk.Button(root, text="Open Text File", command=self.open_file).pack(pady=10)
        tk.Label(root, text="Max Font Size:").pack()
        self.font_size_entry = tk.Entry(root)
        self.font_size_entry.insert(0, str(self.max_font_size))
        self.font_size_entry.pack(pady=5)

        tk.Button(root, text="Choose Background Color", command=self.choose_color).pack(pady=10)
        tk.Button(root, text="Generate Word Cloud", command=self.generate_word_cloud).pack(pady=10)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_path:
            messagebox.showinfo("File Selected", f"File loaded: {self.file_path}")

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Background Color")
        if color[1]:  # If a color is selected
            self.bg_color = color[1]

    def generate_word_cloud(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a text file first.")
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                text = file.read()

            # Get font size from input
            try:
                self.max_font_size = int(self.font_size_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid font size. Please enter a number.")
                return

            # Generate Word Cloud
            wordcloud = WordCloud(
                width=800, height=400,
                background_color=self.bg_color,
                max_font_size=self.max_font_size,
                stopwords=STOPWORDS
            ).generate(text)

            # Display Word Cloud
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = WordCloudGUI(root)
    root.mainloop()
