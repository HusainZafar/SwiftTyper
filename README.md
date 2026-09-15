# Swift Typer:

SwiftTyper tests your typing speed in real time, displaying other stats like words per minute and accuracy. The final result is displayed at the end.
The program was created using PyQt and Qt designer.

Instructions to run the program:

```
python3 type.py
```
Dependencies:
- PyQt5
 ```
 pip install PyQt5
 ```

Note for WSL2 users: if the app crashes when clicking maximize on a popup, run it with `QT_QPA_PLATFORM=xcb python3 type.py` instead. That's a WSL2/Wayland-specific issue, not a bug in the app itself.
