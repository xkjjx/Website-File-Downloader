import sys
import tkinter as tk
from processing import full
def submit():
    try:
        website = websiteEntry.get()
        extensions = extensionsEntry.get().split(",")
        folder = folderEntry.get()
        successes,failures = full(website,extensions,folder,False)
        print("Website:", website)
        print("Extensions:", extensions)
        print("Folder:", folder)
        print("Use source file name for local file names:", useSourceFileNameState.get())
        print("Select that:", indexedFileNameState.get())
        message = str(len(successes)) + " files succesfully downloaded"
        for success in successes:
            message += "File succesfully downloaded from: " + success + "\n"
        for failure in failures:
            message += "File cannot be downloaded from: " + failure + "\n"
        messageLabel.configure(state="normal")
        messageLabel.insert("end", message)

        messageLabel.configure(state="disabled")
    except:
        messageLabel.configure(state="normal")
        messageLabel.insert("end", sys.exc_info())

        messageLabel.configure(state="disabled")

def xor1():
    indexedFileNameCheckbox.deselect()

def xor2():
    useSourceFileNameCheckbox.deselect()



root = tk.Tk()
root.title("Website file downloader")

# Set the desired window size
window_width = 800
window_height = 1000

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position for the window to be centered
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Website URL
websiteLabel = tk.Label(root, text="Website:")
websiteLabel.pack(pady=10)
websiteEntry = tk.Entry(root)
websiteEntry.pack(pady=5, padx=20, fill=tk.X)

# File Extensions
extensionsLabel = tk.Label(root, text="File Extensions (comma-separated):")
extensionsLabel.pack(pady=10)
extensionsEntry = tk.Entry(root)
extensionsEntry.pack(pady=5, padx=20, fill=tk.X)

# Folder Name
folderLabel = tk.Label(root, text="Folder Name:")
folderLabel.pack(pady=10)
folderEntry = tk.Entry(root)
folderEntry.pack(pady=5, padx=20, fill=tk.X)
# Check Boxes

useSourceFileNameState = tk.BooleanVar(value=True)
useSourceFileNameCheckbox = tk.Checkbutton(root, text="Use source file name for local file names", variable=useSourceFileNameState, onvalue=True, offvalue=False,command=xor1)
useSourceFileNameCheckbox.pack(pady=5)

indexedFileNameState = tk.BooleanVar()
indexedFileNameCheckbox = tk.Checkbutton(root, text="Index local file name from 0", variable=indexedFileNameState, onvalue=True, offvalue=False,command=xor2)
indexedFileNameCheckbox.pack(pady=5)

# Submit Button
submitButton = tk.Button(root, text="Submit", command=submit)
submitButton.pack(pady=10)


# Create a scrollable frame
scrollableFrame = tk.Frame(root)
scrollableFrame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a message label widget
messageLabel = tk.Text(scrollableFrame, wrap="word", relief="flat", height=10)
messageLabel.pack(side="left", fill="both", expand=True)
messageLabel.configure()

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(scrollableFrame, orient="vertical", command=messageLabel.yview)
scrollbar.pack(side="right", fill="y")

# Configure the message label widget to use the scrollbar
messageLabel.configure(yscrollcommand=scrollbar.set)
messageLabel.configure(state="disabled",background="#ececec")

root.mainloop()


root.mainloop()
