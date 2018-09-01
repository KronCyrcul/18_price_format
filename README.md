# Price Formatter

The script takes a string in the format ```1234567.000``` and prints it like ```1 234 567```. If the output contains letters, punctuation, or more than one fot, it returns None

# Usage Example

Python 3 should be already installed. Example of script launch on Linux, Python 3.5:

```
$ python format_price.py 8716521362.1800725
8 716 521 362.1800725
```

You can also import format_price function in other module:

``` python
from format_price import format_price
print(format_price("2345.2312"))
```
Output:
```
2 345.2312
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
