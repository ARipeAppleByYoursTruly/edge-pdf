import sys, os, subprocess
from urllib.parse import quote
from tkinter import messagebox

def main():
    argumentsLength: int = len(sys.argv)

    if argumentsLength == 1:
        showError("Please choose a PDF file, and open with edge-pdf.exe.")
    elif argumentsLength > 2:
        showError("Too many command line arguments, please pass in only 1 PDF file.")



    filepath: str = sys.argv[1]

    if not os.path.isfile(filepath):
        showFileOpenError(filepath, "File does not exist.")

    if not filepath.lower().endswith(".pdf"):
        showFileOpenError(filepath, "edge-pdf.exe can only open PDF files.")



    edgeArgumentList: str = f'"--app=`"{convertToUrl(filepath)}`" --start-maximized"'

    subprocess.run(["powershell", "start", "msedge", edgeArgumentList])



def convertToUrl(filepath: str) -> str:
    # Windows does not allow these characters in filenames
    # \ / : * ? " < > |

    # So I'm assuming filenames will never contain them



    # '\' is not allowed in f-strings
    return quote(filepath, "/:\\")



def showError(message: str):
    message += "\n\nFor more info, visit https://github.com/ARipeAppleByYoursTruly/edge-pdf"

    messagebox.showerror(title="edge-pdf Error", message=message)
    sys.exit(1)



def showFileOpenError(filepath: str, message: str):
    showError(f"Failed to open file specified by the following filepath:\n{filepath}\n\n{message}")



main()
