#!/usr/bin/env python

import glob
import os

import pydoc
from pathlib import Path

import sys

"""
Generate the code documentation, using pydoc.
"""

DOC_DIR = "doc"
SOURCE_DIR = 'src'

class HTMLDocSubmodule(pydoc.HTMLDoc):
    def classlink(self, object, modname):
        link = super().classlink(object, modname)
        return self._remove_prefix(modname, link)

    def _remove_prefix(self, modname, link):
        prefix = ".".join((modname.split(".")[0:-1]))+"."
        return link.replace(prefix, "")
    
doc = HTMLDocSubmodule()
for path in Path("src").rglob("*"):
    if path.suffix != ".py":
        continue
    
    root_dir = path.parent
    module_dir =  path.stem
    
    root_name = ".".join(root_dir.parts)
    module_name = str(module_dir)

    print("----")
    print("path: ",path)
    print("root_dir: ", root_dir)
    print("root_dir_absolute: ", root_dir.absolute())
    print("module_name: ", module_name)
    
    sys.path.append(str(root_dir.absolute()))
    module = pydoc.safeimport(module_name)

    
    print(module)
    #
    
    '''
    # get documentation
    print(root_name + "." + module_name)
    module = pydoc.safeimport(root_name + "." + module_name)#str(Path(fname)))
    html = doc.document(module)
    
    # write file
    destination_dir = Path(DOC_DIR) / root_dir
    destination_dir.mkdir(parents=True, exist_ok=True)
    
    destination_file = destination_dir / (module_dir + ".html")
    print(destination_file)
    
    with open(destination_file, "w") as file:
        file.write(html)
    '''