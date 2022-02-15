# Sploitus
Command line search tool for sploitus.com. Think searchsploit, but with more POCs. Sploitus provides a tonne of pocs for a lot of vulnerabilities in a lot of services, scraped from all over the internet!

# Installation
## Automatic
```bash
python -m pip install git+http://github.com/watchdog2000/sploitus
```
## Manual
```bash
  $ git clone https://github.com/watchdog2000/sploitus
  $ cd sploitus
  $ python setup.py install
```
# Usage
```bash
# Search exploits via title
$ sploitus wordpress
$ sploitus wordpress 1.9.3

# Search through exploit code also, not just relying on titles of exploits
$ sploitus wordpress -v
```
