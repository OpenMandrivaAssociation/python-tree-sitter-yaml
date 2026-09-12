Name:		python-tree-sitter-yaml
Version:	0.7.2
Release:	1
Summary:	Tree-sitter yaml grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-yaml
Source0:	https://files.pythonhosted.org/packages/57/b6/941d356ac70c90b9d2927375259e3a4204f38f7499ec6e7e8a95b9664689/tree_sitter_yaml-0.7.2.tar.gz
# PyPI sdist omits scanner.c and schema.*.c
Source1:	tree-sitter-yaml-extra-src.tar.xz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for yaml, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_yaml-0.7.2
tar -C src -xf %{SOURCE1}

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_yaml*
