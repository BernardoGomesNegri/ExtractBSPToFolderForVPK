# ExtractBSPToFolderForVPK
This is a script made to work around a bug in Source Engine which does not allow it to read assets embedded in .bsp files when they are inside a .vpk

## Running it
Change the file paths to match where are your folders.

* OutputDirStr: Should be an empty folder where the result of the process is. You can drag this folder directly to VPK.exe
* InputFolderStr: The folder where you downloaded the maps where that you want to extract. Should have at least a maps/ subfolder.

After running the program, use VPK.exe to transform it to a vpk file (instructions [here](https://developer.valvesoftware.com/wiki/VPK)). If the filesize of the output folder is more than 200MB, run VPK.exe in multichunk mode (described in the website).

## Why?
There is currently a bug in Source Engine (which I know exists in Team Fortress 2, don't know about other games) that prevents the game from loading asset files embedded in a map file (.bsp file) while the map file is inside a .vpk file.

## What does the script do?
It grabs all the asset files inside the map files (the assets which wouldn't be read if the map was in a vpk) and puts them directly in its appropriate folder so that the game can read it even if the map is in a vpk.
For example, it transforms this folder structure:

* Root dir
  * maps
    * cp_example
      * materials
        * texture.vmt (this file wouldn't be read if this was a vpk)

Into this:

* Root dir
  * maps
    * cp_example
      * materials
        * texture.vmt (this file still wouldn't be read if this was a vpk)
  * materials
    * texture.vmt (this file would be read by the game and the map would use it)
