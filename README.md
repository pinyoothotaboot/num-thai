# Number to Thai text

The tool is a convert number to thai text : **Python 3.6+**.

# Features
- Convert number integer or float to Thai text.

# Setup
- Check version Python and PIP
![](https://github.com/pinyoothotaboot/num-thai/blob/master/docs/images/check_version.png?raw=true)

- Install lib : num-thai
![](https://github.com/pinyoothotaboot/num-thai/blob/master/docs/images/install_numthai.png?raw=true)

- Test lib in python shell
![](https://github.com/pinyoothotaboot/num-thai/blob/master/docs/images/example_numthai.png?raw=true)


# Example

```python

from num_thai.thainumbers import NumThai

num = NumThai()
text = num.NumberToTextThai(1111111111111111)

print(text)

```

# About

- Support digit length 1 - 16 digit.
- Support minus digit.
- Support integer or float number.

