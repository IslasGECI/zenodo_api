<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# Zenodo API
[![codecov](https://codecov.io/gh/IslasGECI/zenodo_api/graph/badge.svg?token=RY807ST1T1)](https://codecov.io/gh/IslasGECI/zenodo_api)
![example branch
parameter](https://github.com/IslasGECI/zenodo_api/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/zenodo_api)
![languages](https://img.shields.io/github/languages/top/IslasGECI/zenodo_api)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/zenodo_api)
![PyPI - Version](https://img.shields.io/pypi/v/zenodo_api)

Para usar este repo como plantilla debemos hacer lo siguiente:

1. Presiona el botón verde que dice _Use this template_
1. Selecciona como dueño a la organización IslasGECI
1. Agrega el nombre del nuevo módulo de python
1. Presiona el botón _Create repository from template_
1. Reemplaza `zenodo_api` por el nombre del nuevo módulo en:
    - `Makefile`
    - `pyproject.toml`
    - `tests\test_transformations.py`
1. Renombra el archivo `zenodo_api\transformations.py` al nombre del primer archivo del
   nuevo módulo
1. Cambia la descripción del archivo `zenodo_api\__init__.py`
1. Renombra el directorio `zenodo_api` al nombre del nuevo módulo
1. Cambia el `codecov_token` del archivo `Makefile`

Los archivos del nuevo módulo los agregarás en la carpeta que antes se llamaba
`zenodo_api` y las pruebas en la carpeta `tests`.
