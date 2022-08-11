# Mitre2Datatables

**Since the [Mitre Att&ck (c)](https://attack.mitre.org) matrix is not very convenient to embed in your own web project, I chose to build my own matrix based on [Datatables](https://datatables.net).**

**Mitre2Datatables** allows you to add search, sort, filter and add custom graphics to your [Mitre Att&ck (c)](https://attack.mitre.org) matrix without complicated things like Node 😁

This project only uses technique ID and technique names but it should be possible to have much more.

## Example

This project is born when working on Zircolite, so this exemple is taken from it : 

![](pics/gui-matrix.webp)

## Usage

You can install dependencies with : `pip3 install -r requirements.txt`

- `python3 Mitre2Datatables.py` will generate a JSON file that can be used with Datatables
- `Mitre2Datatables.html` is a very basic demo on how to use and interact with Mitre2Datatables in you web page

