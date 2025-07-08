# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Removed

### Fixed


## [1.0.0] - 2025-07-08
### Changed
- CLI command `download-from-geci-zenodo` now retrieve all files in record.

## [0.3.0] - 2025-07-08

### Added
- CLI command `download-from-geci-zenodo` now can retrieve restricted files


## [0.2.2] - 2025-06-04

### Fixed
- all functions in `upload_files.py` and `new_version.py` that use urls for responses now require the `is_sandbox` boolean parameter

## [0.2.1] - 2025-05-21

### Fixed
- `upload_metadata` now includes publication date

## [0.2.0] - 2025-05-07

### Added
- `publish-new-version`

## [0.1.0] - 2024-11-21

### Added
- `download-from-geci-zenodo`


[unreleased]: https://github.com/IslasGECI/zenodo_api/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/IslasGECI/zenodo_api/releases/tag/v0.2.0..v0.1.0
[0.1.0]: https://github.com/IslasGECI/zenodo_api/releases/tag/v0.1.0
