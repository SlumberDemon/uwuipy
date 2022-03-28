# uwuipy

A python library that uwu-ifies your text. Example:

- Input Text: `they're merely looking into it. there is no concrete deal that has been made yet, and there have been other companies that have expressed interest`
- Output Text: `they'we mewely looking into it. thewe is no concwete deal that (・´ω´・) has x3 been made yet, and thewe ;;w;; have been othew companies that have expwessed intewest`

## Instalation

```
pip install git+https://github.com/SlumberDemon/uwuipy
```

## Example Usage

You can uwu-ify a string of text using the `Uwufier.uwu` method

```py
from uwuipy import Uwuifier

uwuifier = Uwuifier()
print(uwuifier.uwu("This library is not on pip as of right now.")) # returns "This libwawy is (・`ω´・) not on pip as of wight n-now."
```

### Acknowledgements

The structure of this project was heavily inspired by [Schotsl's implementation](https://github.com/Schotsl/Uwuifier-node) of an uwu-ifier in node.js & typescript
