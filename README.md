# One-way OS-independent folder synchronizer

## Description

Once launched, the app should be configured with:
* the path of a source and a replica folder
* the path of a log file where the file operations will be recorded
* a synchronization time interval (in seconds).

## Scripts

* `make build`: launch the folder synchronization app in the console
* `make test`: launch Pytest suite(s) - set the specific test variables first (inside test modules)

## Design choices

* detecting file content alterations by hashing it with SHA-256
*  it does NOT follow the principle that a renamed file is a new file
* consequently, it obtains faster sync times for e.g. file renaming
  

