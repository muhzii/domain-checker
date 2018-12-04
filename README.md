Quick WHOIS reolver for checking domain info and availability

## INSTALLATION
```
pip install domain-checker
```

## Example usage

```
from domain-checker import whois

domain = whois('google.com')
avail = domain.available
name = domain.name
summary = domain.stringify()
```