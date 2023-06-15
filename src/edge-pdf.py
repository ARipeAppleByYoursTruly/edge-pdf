import sys, os, subprocess
from tkinter import messagebox

def main():
    argumentsLength: int = len(sys.argv)

    if argumentsLength == 1:
        showError("Please choose a PDF file, and open with edge-pdf.exe.")
    elif argumentsLength > 2:
        showError("Too many command line arguments, please pass in only 1 PDF file.")



    fileToOpen: str = sys.argv[1]

    if not os.path.isfile(fileToOpen):
        showFileOpenError(fileToOpen, "File does not exist.")

    if not fileToOpen.lower().endswith(".pdf"):
        showFileOpenError(fileToOpen, "edge-pdf.exe can only open PDF files.")

    if not isFilepathAsciiCharactersOnly(fileToOpen):
        showFileOpenError(fileToOpen, "Filepath contains non-ASCII characters, please rename the file and try again.")




    edgeArgumentList: str = f'"--app=`"{createEncodedURL(fileToOpen)}`" --inprivate --start-maximized"'

    subprocess.run(["powershell", "start", "msedge", edgeArgumentList])



def isFilepathAsciiCharactersOnly(filepath: str) -> bool:
    for ch in filepath:
        if ord(ch) not in range(32, 128):
            return False

    return True



def createEncodedURL(filepath: str) -> str:
    # Windows does not allow these characters in filenames
    # \ / : * ? " < > |

    url = filepath.replace("%", "%25") # Must encode '%' first
    url = filepath.replace(" ", "%20")
    url = filepath.replace("!", "%21")
    url = filepath.replace("#", "%23")
    url = filepath.replace("$", "%24")
    url = filepath.replace("&", "%26")
    url = filepath.replace("'", "%27")
    url = filepath.replace("(", "%28")
    url = filepath.replace(")", "%29")
    url = filepath.replace("*", "%2A")
    url = filepath.replace("+", "%2B")
    url = filepath.replace(",", "%2C")
    url = filepath.replace(";", "%3B")
    url = filepath.replace("=", "%3D")
    url = filepath.replace("@", "%40")
    url = filepath.replace("[", "%5B")
    url = filepath.replace("]", "%5D")

    return url



def showError(message: str):
    message += "\n\nFor more info, visit https://github.com/ARipeAppleByYoursTruly/edge-pdf"

    messagebox.showerror(title="edge-pdf Error", message=message)
    sys.exit(1)



def showFileOpenError(filepath: str, message: str):
    showError(f"Failed to open file specified by the following filepath:\n{filepath}\n\n{message}")



main()
