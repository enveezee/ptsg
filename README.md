# ptsg
Python Turtle Simple GUI

William Shakespere had said "What's in a name?" and under most circumstances, I'd agree... however when it comes to coding FOSS everyone knows you need to have a clever name for everything. I was sitting here with some crappy turtle code trying to test some things for something I'm writing, and my test jig kept falling short and modifying the code endlessly was causing me to develop PTSD, so... I wrote this to hopefully solve that problem... I introduce to you a case of PTSG.

The aim here is to create some code you can use to test turtle and PySimpleGUI that you can take and just run as a standalone module with a lot of default features to make use of, and use as example code to reference how to accomplish some things, yet it aims to be flexible enough to customize without dipping into the code itself allowing you to merely specify the changes you want to make. 

Much further development is needed to make something truely meeting this goal, however, I'm sure what I've done so far will be a good start that could save people some time and frustration. Features included in this are a PySimpleGUI with status information, GUI controls for turtle, a primitive but functional command line with output, and early stages of keyboard/mouse bindings currently.

Consider this free software in every regard to use as you like for any purpose with asbolutely no warranty or claim of fitness for any purpose what-so-ever, and I disclaim all liabilities of any kind. I would however appreciate it if you fork this on github and share modifications so we can further develop it to be more useful. I would also appreciate any feedback on use, though I can't make any promises about future development, only that interest in the code by other people would be more motivation to further develop it. I think what I got here more than meets my current needs and I learned quite a few things in writing it.

Screnshots:
![PTSG](ptsg.png?raw=true "PTSG")

![PTSG run from terminal](ptsg-terminal.png?raw=true "PTSG run from the terminal")

## Instaling requirements

´pip install -r requirements.txt´