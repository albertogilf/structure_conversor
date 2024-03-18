Certainly! Here's the README.md format for your project:

```markdown
# Structure Conversor

Structure Conversor is a Python tool for converting chemical structures between different representations such as SMILES, InChI, and InChIKey. It leverages the ChemSpider web service to perform these conversions.

## Installation

To install Structure Conversor, you can use pip:

```
pip install structure-conversor
```

## Usage

```python
from structure_conversor import convert_to_inchi

smiles = "C(C(=O)O)N"
inchi = convert_to_inchi(smiles)
print("InChI:", inchi)
```

## Features

- Convert SMILES to InChI
- Convert InChI to SMILES
- Convert InChI to InChIKey
- Convert InChIKey to InChI

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can copy this markdown content directly into your README.md file in your GitHub repository. Feel free to customize it further to better fit your project's needs.