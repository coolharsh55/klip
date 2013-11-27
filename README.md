#### klip

parser module for the amazon kindle's clippings.txt file.

#### usage

clippings.txt
```
﻿The Mythical Man Month (Frederick P. Brooks)
- Your Highlight Location 181-182 | Added on Tuesday, November 19, 2013 1:23:50 PM

Good cooking takes time.
==========
Code Complete, Second Edition (Steve McConnell)
- Your Highlight on page 73 | Location 1105-1106 | Added on Wednesday, November 27, 2013 11:10:25 AM

Make sure everyone knows the cost of requirements
==========

```

```python
>>> from klip import load

>>> clippings = open('clippings.txt').read()
>>> load(clippings)

>>> # you can use load_file("clippings.txt") if you prefer.

```


```javascript
[{
    'content': 'Good cooking takes time.',
    'meta': {
        'type': 'Highlight',
        'page': None,
        'location': '181-182'
    },
    'author': 'Frederick P. Brooks',
    'added_on': datetime.datetime(2013, 11, 19, 13, 23, 50),
    'title': 'The Mythical Man Month'
}, {
    'content': 'Make sure everyone knows the cost of requirements',
    'meta': {
        'type': 'Highlight',
        'page': None,
        'location': None
    },
    'author': 'Steve McConnell',
    'added_on': datetime.datetime(2013, 11, 27, 11, 10, 25),
    'title': 'Code Complete, Second Edition'
}]
```
