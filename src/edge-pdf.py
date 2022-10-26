import os, sys
from tkinter import messagebox

def main():
    # Check command line syntax
    argLen = len(sys.argv)

    if (argLen == 1):
        triggerError("Please choose a PDF file, and open with edge-pdf.exe.")
    elif (argLen > 2):
        triggerError("Too many command line arguments, please pass in only 1 PDF file.")


    # Check arugment's file type
    fileToOpen = sys.argv[1]

    if (not fileToOpen.endswith(".pdf")):
        triggerError("edge-pdf.exe can only open PDF files.")


    # Replace ' ' in fileToOpen to '%20' because URLs can't contain literal spaces
    fileToOpen.replace(" ", "%20")

    # Open the file with Microsoft Edge in app mode
    os.system("start msedge --app=\"" + fileToOpen + "\"")



def triggerError(msg):
    msg += "\n\nFor more info, visit https://github.com/ARipeAppleByYoursTruly/edge-pdf"

    messagebox.showerror(title="edge-pdf Error", message=msg)
    sys.exit(1)



main()