# SMT Breakout Boards

This repository contains a set of breakout boards to allow the use of surface mount components on a breadboard. The boards are designed to be as generic as possible so they can be used with a range of components. The schematic and PCB layout files are in [DesignSpark PCB](http://www.rs-online.com/designspark/electronics/eng/page/designspark-pcb-home-page) format, each directory contains a *gerbers.zip* file that holds the gerber files necessary to send the boards for fabrication (these are the files I sent to [Seeed Fusion](https://www.seeedstudio.com/fusion_pcb.html) and the results were fine).

The current set of boards include:

| Board    | Gerbers                          | Description |
|----------|----------------------------------|-------------|
|dfn065    |[Download](dfn065/gerbers.zip)    |DFN8 to DIP8, 0.65mm pitch.|
|dfn100    |[Download](dfn100/gerbers.zip)    |DFN8 to DIP8, 1.00mm pitch.|
|greenpak12|[Download](greenpak12/gerbers.zip)|[GreenPak](http://www.silego.com/products/greenpak3.html) STQFN12 to DIP12.|
|greenpak20|[Download](greenpak20/gerbers.zip)|[GreenPak](http://www.silego.com/products/greenpak3.html) STQFN20 to DIP20.|
|multibob  |[Download](multibob/gerbers.zip)  |The [MultiBOB](http://thegaragelab.com/multibob/) general purpose board.|
|soic      |[Download](soic/gerbers.zip)      |SOIC20 to DIP20.|
|tssop20   |[Download](tssop20/gerbers.zip)   |TSSOP20 to DIP20.|

The boards can be used with devices with fewer pins as well, for example a SOIC8 on the SOIC board. If you have suggestions for changes or new boards please raise and issue or discuss them on [The Garage Lab space](https://goo.gl/spaces/Jya8RZ54SVnX8B8U7).
