# randomPythonProjects
A set of Python scripts and projects I've made for various reasons.

## Status:
eventually will continue, college has got me burnt out, next goal is with `controller-support.py`, making that fully fledged and a drag`n`drop codebase.

# Current Goals:
- Make an interactive UI/GUI purely within Python.
   > Aim for a launcher-type program.
   > Must be semi-customizable, similar to how Steam is with Game Art.
   > Must allow for adding/removing items on the fly.
   > Order of items must be sortable.
- Finish `controller-support.py`.
   > Add a language key like system for buttons.
   > Each controller should have a dictionary attached, this stores 2 main lists, controller attributes and buttons.
      > Make sure to use generic names like `Face_UP‘ and `Left Bumper`.
      > Remember to account for controller specific things; EX: Analog vs. Variable Triggers
   > Make a toggle where it creates visuals, this will be done on a uniquely named `Surface` so you can `blit()` it onto other `Surfaces` like an overlay.
   > *Note: Not all features for controllers will be supported. This is mainly meant for the common controllers you'd see.*
      > This includes: XBOX 1 / Series S/X Controllers, DualShock 4 / DualSense 5, and Nintendo Switch 1 Pro Controller / Joycons.