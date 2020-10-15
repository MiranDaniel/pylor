# MDansi

## *Library for outputting colorful text*

### Supports 16 foreground and 16 background colors

---

![Color table](https://i.stack.imgur.com/9UVnC.png)

*Table from [Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)*

---

## QuickStart

Place this module in your modules folder. (PYPI not supported yet.)

```py
import MDansi
from MDansi import colors # Imports class full of colors to choose from
```

---

## Functions

### **color()**

The color function is used to create colored strings.

Arguments:

- String
- Foreground color
- Background color *[Optional]*

**Example:**

```py
import MDansi
from MDansi import colors

print( MDansi.color("Hello world!", colors.foreground.red) )
```

Returns string

---

### **colorNoReset()**

The color function is used to create colored strings, does not set the color back to default (continues to color any future output).

Arguments:

- String
- Foreground color
- Background color *[Optional]*

**Example:**

```py
import MDansi
from MDansi import colors

print( MDansi.colorNoReset("Hello world!", colors.foreground.red) )
```

Returns string

---

### **reset()**

Function used for resetting the color after using colorNoReset()
**Example:**

```py
import MDansi
from MDansi import colors

print( MDansi.reset() )
```

Returns string

---
