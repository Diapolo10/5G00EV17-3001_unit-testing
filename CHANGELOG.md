
# 5G00EV17-3001 Unit testing Changelog

All notable changes to this project will be documented in this file.

The format is based on [CHANGELOG.md][CHANGELOG.md]
and this project adheres to [Semantic Versioning][Semantic Versioning].

<!-- 
TEMPLATE

## [major.minor.patch] - yyyy-mm-dd

A message that notes the main changes in the update.

### Added

### Changed

### Deprecated

### Fixed

### Removed

### Security

_______________________________________________________________________________
 
 -->

<!--
EXAMPLE

## [0.2.0] - 2021-06-02

Lorem Ipsum dolor sit amet.

### Added

- Cat pictures hidden in the library
- Added beeswax to the gears

### Changed

- Updated localisation files

-->

<!--
_______________________________________________________________________________

## [1.0.4] - 2023-11-02

Updated dependencies, and updated Tox configuration to fix coverage
report generation.

### Changed

- Updated dependencies
- Updated localisation files

### Fixed

- Coverage report generation via Tox was broken, this update
  fixes that by changing how Tox is configured.

-->

_______________________________________________________________________________

## [1.0.4] - 2023-11-02

Updated dependencies, and updated Tox configuration to fix coverage
report generation.

### Changed

- Updated dependencies
- Updated localisation files

### Fixed

- Coverage report generation via Tox was broken, this update
  fixes that by changing how Tox is configured.

_______________________________________________________________________________

## [1.0.3] - 2023-10-03

Updated dependencies, moved source code to `src`, made Ruff rules stricter,
and fixed outdated `Makefile`.

### Added

- Added new rules for Ruff
- Added hash support for the `Date` class

### Changed

- Moved the source code files under `src` to better match accepted best
  practices
- Updated outdated links in `CHANGELOG.md`
- Updated dependencies
- Updated localisation files

### Fixed

- Fixed `Makefile`'s linting (it was still using `pyproject-flake8`
  instead of Ruff)
- Various linter fixes
- `README.md` had an old version number for Python, this is now fixed

_______________________________________________________________________________

## [1.0.2] - 2023-02-24

This update adds a missing `py.typed` file, and updates dependencies.

### Added

- `py.typed`

### Changed

- Fixed some wording in `README.md`
- Updated dependencies
- Updated localisation files

_______________________________________________________________________________

## [1.0.1] - 2022-04-12

This update adds some additional test cases for corner cases, improves
type hinting, and adds missing docstrings

### Added

- More docstrings
- More test cases
- Documentation is now linked in `README.md`

### Changed

- Improved type hinting
- Updated localisation files

_______________________________________________________________________________

## [1.0.0] - 2022-03-30

This is the initial version of the project.

### Added

- Example project featuring a Date class
- Unit tests
- Coverage reports
- Documentation for installation and unit tests

### Changed

- Updated `README.md` to contain more useful information
- Updated localisation files

### Fixed

- Linter errors

### Removed

- Dread

### Security

- Project has Snyk scanning enabled

[CHANGELOG.md]: https://keepachangelog.com/en/1.1.0/
[Semantic Versioning]: http://semver.org/

<!-- markdownlint-configure-file {
    "MD022": false,
    "MD024": false,
    "MD030": false,
    "MD032": false
} -->
<!--
    MD022: Blanks around headings
    MD024: No duplicate headings
    MD030: Spaces after list markers
    MD032: Blanks around lists
-->
