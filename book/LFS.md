# Git LFS repository for big and binary files

```{note}
This is an alternative to the FTP-server described in [FTP.md](./FTP.md). We aim to phase out the FTP-server in the future.
```

To keep our websites small and efficient, we're storing our big (>0.5 MB) and binary files (e.g. .JPEG, .zip) in a separate repository which makes use of git LFS. Furthermore, this allows us to share single assignments files without attachments.

To access the Git LFS repository, you must be added to the 'content writers' team in the MUDE GitHub organization. Tom van Woudenberg can add you to this team.

Add your big and binary files in the `./file/`-directory. Don't be afraid of things becoming a mess, that's fine! As long as you don't delete existing files, although GitHub shouldn't allow you to do so ;). And of course, DON't put any copyrighted material on this FTP server.

To use a file, you can use the url `https://github.com/TUDelft-MUDE/source-files/raw/main/file/<filename>`. For example the file `MUDE_Logo-small.png` in `./file/` can be referenced by with `https://github.com/TUDelft-MUDE/source-files/raw/main/file/MUDE_Logo-small.png`, which gives you the image below:

![](https://github.com/TUDelft-MUDE/source-files/raw/main/file/MUDE_Logo-small.png)

Figures can be referenced in any markdown text using the normal syntax for a figure:

```md
![](https://github.com/TUDelft-MUDE/source-files/raw/main/file/<filename>)
```

If you want to have students download files from a `.ipynb`-file, you can use the following lines of code:

```python
import os
from urllib.request import urlretrieve

def findfile(fname):
    if not os.path.isfile(fname):
        print(f"Downloading {fname}...")
        urlretrieve('https://github.com/TUDelft-MUDE/source-files/raw/main/file/'+fname, fname)

findfile('<filename>')
```

If you use the code above, add the file to the `.gitignore` to make sure it will not get synced with github.
