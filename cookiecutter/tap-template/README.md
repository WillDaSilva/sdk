_**NOTE:** This framework is still in early exploration and development phases. For more
information and to be updated on this project, please feel free to subscribe to our
[original Meltano thread](https://gitlab.com/meltano/meltano/-/issues/2401) and the
[initial PR for the underlying framework](https://gitlab.com/meltano/tap-base/-/merge_requests/1)._

--------------------------------

# Singer SDK Tap Template

To use this cookie cutter template:

```bash
pip3 install pipx
pipx ensurepath
# You may need to reopen your shell at this point
pipx install cookiecutter
```

Initialize Cookiecutter template directly from Git:

```bash
cookiecutter https://gitlab.com/meltano/singer-sdk --directory="cookiecutter/tap-template"
```

Or locally from an already-cloned `singer-sdk` repo:

```bash
cookiecutter ./singer-sdk/cookiecutter/tap-template
```

See the [dev guide](../../docs/dev_guide.md).