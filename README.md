# klip

A simple parser for Amazon Kindle

## clippings.txt

Kindle annotations are stored in a file called `clippings.txt` inside the `documents` folder.
This module acts on this file and extracts the annotations. You need to know which kindle
version you are using, and use the corresponding parser.

## installation
```bash
pip install klip
```

## usage

### identifying device version

In your kindle settings, or about menu, find the kindle version displayed. For e.g., if it says
*Kindle v4.x.x*, then the version is 4. Use the following table corresponding to the file
`devices.py` to identify the string to use for your version.

* Kindle Paperwhite: `Paperwhite`
* Kindle Touch: `Touch`
* Kindle 4: `Kindle4`
* Kindle 1-3+: `OldGenKindle`

### load from file

```python
import klip
data = klip.load_from_file('clippings.txt', 'Kindle4')
```

### load

```python
with open('clippings.txt', 'r') as f:
	data = klip.load(f.read())
```

### data format of clippings

```json
[
	{
		"content": "Good cooking takes time.",
		"meta": {
			"type": "Highlight",
			"page": None,
			"location": "181-182"
		},
		"author": "Frederick P. Brooks",
		"added_on": datetime.datetime(2013, 11, 19, 13, 23, 50),
		"title": "The Mythical Man Month"
	}
]
```
