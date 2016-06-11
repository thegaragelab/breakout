# MultiBOB Layout Generator

This directory contains a small Python script that generates a SVG (and optionally, PNG) image of the board layout for a specific circuit.

> To generate the PNG version of the layout you will need to install ImageMagick. On Windows I used [this version](http://www.imagemagick.org/download/binaries/ImageMagick-6.9.4-7-Q16-x86-dll.exe) (6.9.4.7) that worked well with my 32 bit Python 2.x installation. Make sure you select the *Install Development Headers and Libraries for C and C++* option during setup.

The circuit is defined in a JSON file that specifies what pads are populated and allows you to add some additional documentation. A sample file (for the 3.3V regulator) looks like this:

```
{
  "title": "3.3V LDO Regulator",
  "jumpers": [ 3, 4, 5 ],
  "components": {
    "comp1": [ "U1", "MCP1702 (3.3V)" ],
    "comp3": [ "C1", "1uF" ],
    "comp4": [ "C2", "1uF" ]
    },
  "pins": [
    "Gnd",
    "Vout",
    "Vin"
    ]
}
```

The available components are 'comp1' (the SOT-23 pads), 'comp2' (the SOT-223 pads) and 'comp3' through 'comp7' for the 0805 discretes. Jumpers 1 & 2 allow connection to the ground plane and jumpers 3, 4 & 5 allow you to bypass the 0805 pads on the bottom of the board. Play around with the various values until you get the results you want.
