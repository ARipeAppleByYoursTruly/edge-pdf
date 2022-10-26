# edge-pdf
If you and I have a few things in common, then it would be that:
- We both use Mozilla Firefox as our web browser
- We both set MS Edge as the default app to open PDF files
- We both realized that double-clicking recently downloaded PDF files in Firefox launches MS Edge but with a slightly different UI
- We both spent hours trying to figure out how to open PDF files with MS Edge, in that specific look, without going through Firefox, but to no avail

If the last point somewhat fits your description and you've stumbled upon here, then `edge-pdf` is what you're looking for.

## What Is This?
`edge-pdf` is an executable that opens .pdf files with MS Edge in application/app mode, which hides the browser's toolbar. To my knowledge, app mode is actually used to prevent users from using MS Edge to browse the web. But that works in my favor, as I intent to use MS Edge for opening PDF files only.

Here's a comparison shot of opening a PDF file using MS Edge vs `edge-pdf`:
![A PDF file opened using MS Edge](docs/comparison-msedge.png)
Opened using MS Edge

![A PDF file opened using edge-pdf](docs/comparison-edgepdf.png)
Opened using `edge-pdf`

## How Does It Work?
`edge-pdf` simply executes the command line `start msedge --app=<filepath-to-pdf-file>`, where `<filepath-to-pdf-file>` is the PDF file that you choose to `Open With edge-pdf.exe`.

It is not an standalone desktop app, nor does it have a GUI. `edge-pdf` should be thought of as a shortcut to execute the command line stated above, but in the executable (.exe) format so users can configure `edge-pdf.exe` as the default program to open PDF files.

## Installing and Setting Up `edge-pdf`
### Prerequisites
1. You're using a Windows PC

   If you're on different OS, and dead set on using MS Edge as the default PDF Editor, you can try:
   - Building the "app" yourself using the `src` folder (which requires some knowledge on programming using Python), or
   - Use an external program to run `edge-pdf.exe`

2. You have MS Edge installed
3. You **actually** use MS Edge as your go-to PDF viewer and editor

### Step-By-Step
1. Download and extract `edge-pdf.zip` to your desired location
2. Open Microsoft Edge, go to `Settings > Cookies and site permissions`, scroll down and click `PDF documents`, and turn off `Always download PDF files`
![MS Edge settings image 1](docs/installation-msedge-settings-1.jpeg)
![MS Edge settings image 2](docs/installation-msedge-settings-2.jpeg)

3. Go to File Explorer, find a .pdf file, right click and select `Open with > Chooe another app`
![File explorer image 1](docs/installation-file-explorer-1.png)

4. Check `Always use this app to open .pdf files`, scroll down and click `More apps`, scroll down again and click `Look for another app on this PC`

![File explorer image 2](docs/installation-file-explorer-2.png)
![File explorer image 3](docs/installation-file-explorer-3.png)

5. Go to the location where you've extracted `edge-pdf.zip` to, and select `edge-pdf.exe` in the `edge-pdf` folder
![File explorer image 4](docs/installation-file-explorer-4.png)

6. If MS Edge opens your .pdf file, then you have successfully installed `edge-pdf`
