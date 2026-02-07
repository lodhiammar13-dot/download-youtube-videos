from pytubefix import YouTube

import tkinter as tk
from tkinter import messagebox

# Download function
def download_video():
    link = link_entry.get()

    if not link:
        messagebox.showerror("Error", "Please enter a YouTube link")
        return

    try:
        yt = YouTube(link)

        title_label.config(text=f"Title: {yt.title}")
        views_label.config(text=f"Views: {yt.views}")

        ys = yt.streams.get_highest_resolution()
        ys.download("D:\\youtube downloaded videos")

        messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


# GUI Window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")
root.resizable(False, False)

# Title
tk.Label(root, text="YouTube Downloader", font=("Arial", 16, "bold")).pack(pady=10)

# Link Entry
tk.Label(root, text="Paste YouTube Link:").pack()
link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

# Download Button
tk.Button(root, text="Download Video", command=download_video, bg="green", fg="white").pack(pady=10)

# Video Info Labels
title_label = tk.Label(root, text="Title: ", wraplength=450)
title_label.pack(pady=5)

views_label = tk.Label(root, text="Views: ")
views_label.pack(pady=5)

root.mainloop()

