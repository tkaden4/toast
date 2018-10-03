# toast

An extremely simple cross-platform library for showing toast notifications.

# Installation
Until I upload to `pypi`, you can install via `setup.py`:

```bash
> pip3 install -r setup.requirements.txt && python3 setup.py install
```

# TODO
- Cross platform icon support
- Test on older (win7) systems

# Example
```Python
import toast


# show a notification
toast.notify(
    title="Hello, World!",
    description="Some descriptive text here"
)

```