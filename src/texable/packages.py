from typing import Iterable, Optional, Set


class Package:
    """
    Represents a LaTeX package to be included in the document preamble.
    """

    def __init__(self, name: str, options: Optional[Iterable[str]] = None):
        self.name = name
        self.options: Set[str] = set(options) if options else set()

    def __str__(self) -> str:
        if self.options:
            return f"\\usepackage[{','.join(self.options)}]{{{self.name}}}"
        else:
            return f"\\usepackage{{{self.name}}}"

    def __eq__(self, other):
        if not isinstance(other, Package):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        # Only the name is used for hashing so packages are unique by name
        return hash(self.name)

    def add_options(self, new_options: Iterable[str]) -> None:
        # Add only options not already present
        for option in new_options:
            self.options.add(option)


required_packages: Set[Package] = set()


def require_package(name: str, options: Optional[Iterable[str]] = None) -> None:
    """
    Marks a LaTeX package as required for the document.

    Args:
        name (str): The name of the package.
        options (Optional[Sequence[str]]): Optional list of options for the package.
    """
    new_pkg = Package(name, options)
    if new_pkg in required_packages:
        if options:
            # Find the existing package and update its options
            for pkg in required_packages:
                if pkg == new_pkg:
                    pkg.add_options(options)
                    break
    else:
        required_packages.add(new_pkg)
