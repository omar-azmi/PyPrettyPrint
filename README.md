# PyPrettyPrint
Pretty print class attributes in tables

## About
This simple python script allows you to print class and object attributes and their desired properties in tabular form. You might find it useful as a debugging tool if you're building a large classes with multiple inheritances.
Features:

- Modify the width of the output tables
- Choose your own set of properties (AKA attributes of attributes) that you want to lookup
- Run your object's attributes through your own string outputing function

## Examples
### Case 1:

> Print the name, representation, type, and memory location of a class's attributes:

**Script:**
```python
from PrettyClassPrint.PrettyClassPrint import PrettyClassPrint as PCP
pp = PCP.pretty_print	#Aliasing the pretty print function for quick access
pp(bool)		#Prints the attributes and methods of the bool built in class in a table
```

**Output:**
![Console output 1](./examples/console%20output/readme%20example%201.png)

### Case 2:
> Customize the output to:
> - Show the `__name__`, `type()`, `__sizeof__`, and `hex(id())` of its attributes.
> - Set the respective column widths to `10%`, `40%`, `25%`, `25%`
> - Set the vertical table separator to `" |$| "`
> - Set the horizontal table separator to `"+\u2014+"`

**Script:**
```python
from PrettyClassPrint.PrettyClassPrint import PrettyClassPrint as PCP

class CustomPrint(PCP):			#The PrettyClassPrint must be inherited as a base class
	#Overwriting some of the default PrettyClassPrint class attributes to serve our needs
	display_properties = ["__name__", type, "__sizeof__", lambda x: hex(id(x))];
	display_portions = [0.10, 0.40, 0.25, 0.25];
	display_vertical_separator = " |$| ";
	display_horizontal_separator = "+\u2014+";

cpp = CustomPrint.pretty_print		#Aliasing our custom the pretty print function for quick access
cpp(bool)				#Custom printing
```

**Output:**
![Console output 1](./examples/console%20output/readme%20example%202.png)

## Installation
In your project's root directory, create a new `./PrettyClassPrint/` folder.

Download the PrettyClassPrint.py and place it in the folder you just made.

To import the PrettyClassPrint class, use `from PrettyClassPrint.PrettyClassPrint import PrettyClassPrint`

## Planned improvements
- Add derived class tree printing
- Develop ktinker based GUI preview of attributes and derivation trees

