# ansiColor

## *Library for outputting colorful text*

### Supports 16 foreground and 16 background colors

---

![Color table](https://i.stack.imgur.com/9UVnC.png)

*Table from [Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)*

---

## QuickStart

Use: `pip install -i https://test.pypi.org/simple/ ansiColor` to install the module.
### Imports
```py
import ansiColor
from ansiColor import colors # Imports class full of colors to choose from
from ansiColor import decorations # Imports class full of decorations
from ansiColor import cursor # Imports class for cursor movement
```

### Testing the installation

```py
import ansiColor
print( ansiColor.test() ) # This will print the project logo
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
import ansiColor
from ansiColor import colors

print( ansiColor.color("Hello world!", colors.foreground.red) )
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
import ansiColor
from ansiColor import colors

print( ansiColor.colorNoReset("Hello world!", colors.foreground.red) )
```

Returns string

---

### **formatting()**

Function used for formatting text.

Arguments:

- String
- Formatting type

**Example:**

```py
import ansiColor
from ansiColor import decorations

print( ansiColor.formatting("Hello world!", decorations.bold) )
```

Returns string

---

### **formattingNoReset()**

Function used for formatting text, does not set the color back to default (continues to decorate any future output).

Arguments:

- String
- Formatting type

**Example:**

```py
import ansiColor
from ansiColor import decorations

print( ansiColor.formatting("Hello world!", decorations.bold) )
```

Returns string

---

### **reset()**

Function used for resetting the color after using colorNoReset()

Arguments:

- None

**Example:**

```py
import ansiColor

print( ansiColor.reset() )
```

Returns string

---

### **test()**

Function for testing the installation of the package, returns the project logo.

Arguments:

- None

**Example:**

```py
import ansiColor

print( ansiColor.test() )
```

Returns string

---

## Codes

### **Colors**

#### **Foreground**

*colors.foreground.*

```md
red
black
green
yellow
blue
magenta
cyan
white
brightBlack
brightRed
brightGreen
brightYellow
brightBlue
brightMagenta
brightCyan
brightWhite
```

#### **Background**

*colors.background.*

```md
red
black
green
yellow
blue
magenta
cyan
white
brightBlack
brightRed
brightGreen
brightYellow
brightBlue
brightMagenta
brightCyan
brightWhite
```

### **Decorations**

*decorations.*

```md
bold
underline
reverse
```

### **Cursor**

*cursor.*

```md
up
down
right
left
```

## Exceptions

### NotAColor

Exception for when the argument given is not an ANSI code.

Example of code that would trigger this Exception:

```py
import ansiColor
from ansiColor import colors

print( ansiColor.color("Hello world!", "red") ) # This is an example of bad code, do not use this, it will not work.
```

correct code:

```py
import ansiColor
from ansiColor import colors

print( ansiColor.color("Hello world!", colors.foreground.red) )
```
