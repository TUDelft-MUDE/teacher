# FTP-server for big and binary files

To keep our websites small and efficient, we're using a TU-Delft provided FTP-server to host all big (>0.5 MB) and binary files (e.g. .JPEG, .zip). Furthermore, this allows us to share single assignments files without attachments.

To access the FTP-server, you must be connected to the TU Delft network or use [a VPN](https://intranet.tudelft.nl/-/openvpn)

Add this FTP-server by following [as shown here for Windows](https://www.wintips.org/how-to-connect-to-an-ftp-server-from-windows-explorer/) or [these steps for Mac](https://ftp-mac.com/how-to-use-ftp-on-mac.html). The server is `ftp://files.mude.citg.tudelft.nl` and the username `files.mude`. Tom van Woudenberg can give you the password.

Add your big and binary files in the `./httpdocs/`-directory. Don't be afraid of things becoming a mess, that's fine! As long as you don't overwrite existing files ;). And of course, DON't put any copyrighted material on this FTP server.

To use a file, you can use the url `https://files.mude.citg.tudelft.nl/<filename>`. For example the file `MUDE_NoTextVector.svg` in `./httpdocs/` can be referenced by with https://files.mude.citg.tudelft.nl/MUDE_NoTextVector.svg, which gives you the image below:

![](https://files.mude.citg.tudelft.nl/MUDE_NoTextVector.svg)

Figures can be referenced in any markdown text using the normal syntax for a figure:

```md
![](https://files.mude.citg.tudelft.nl/<filename>)
```

If you want to have students download files from a `.ipynb`-file, you can use the following lines of code:

```python
import os
from urllib.request import urlretrieve

def findfile(fname):
    if not os.path.isfile(fname):
        print(f"Downloading {fname}...")
        urlretrieve('http://files.mude.citg.tudelft.nl/'+fname, fname)

findfile('<filename>')
```