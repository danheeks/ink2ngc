# ink2ngc
Inkscape extension to save .ngc file for milling machine.

GPL license.

This was hacked from a "unicorn" inkscape extension which made g-code for a 3d printer.

My version is initially just to make simple g-code from inkscape, for my engraving machine which is running bCNC and is only using the z height to activate the solenoid on the spindle.


## Credits

   Copied and hacked from this project https://github.com/martymcguire/inkscape-unicorn

## Install
   Copy the contents of src/ to your Inkscape extensions/ folder, which you can find in Inkscape menu Edit->Preferences->System

## Usage
    Size and locate your image appropriately:
        0,0 is at the bottom left
    Convert all text to paths:
        Select all text objects.
        Choose Path | Object to Path.
    Save as G-Code:
        File | Save a Copy.
        Select bCNC G-Code (*.ngc).
        Save your file.
    Preview
        I load the g-code into HeeksCNC https://sites.google.com/site/heekscad/
    Cut
        Open bCNC on the engraving machine
        Open your .ngc file from bCNC.
        Use the move buttons in bCNC to position the cutter where you want the bottom left corner to be.
        Set X = 0 and Y = 0.
        Click the green run button!

