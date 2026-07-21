# Shared make variables. Included from the root makefile (and, in the
# full-stack template, from src/experiments/makefile via RELATIVE_PATH=../../).

# Get the absolute path of the current Makefile
MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
CURRENT_DIR := $(dir $(MKFILE_PATH))

# Virtual environment. The MSYS2 UCRT64 venv this project uses has the
# Unix layout (bin/, not Scripts/), so we detect which directory the
# interpreter lives in. Override VENV on the command line if you have
# a venv at a different path: `make VENV=.venv env`.
VENV := $(RELATIVE_PATH).venv-ucrt64
ARGS ?= -u
VENV_BIN := $(if $(wildcard $(VENV)/Scripts/python.exe),Scripts,bin)
PYTHON = "$(VENV)/$(VENV_BIN)/python" $(ARGS)
PIP = "$(VENV)/$(VENV_BIN)/pip"

# Build directories.
#   .build/  disposable working area (pdflatex intermediates + PDF).
#   .stage/  durable per-version archive; survives `make clean`.
# Both are dot-prefixed so they sort out of the way and match the
# repo's on-disk layout; .gitignore must ignore both.
build_dir := $(RELATIVE_PATH).build
stage_dir := $(RELATIVE_PATH).stage
data_dir := $(RELATIVE_PATH)data
figures_dir := $(RELATIVE_PATH)figures

# pdflatex flags: bail on first error, give file:line errors.
PDFLATEX = pdflatex -interaction=nonstopmode -halt-on-error -file-line-error
BIBTEX = bibtex

# For substituting spaces in file names, if needed.
nullstring :=
space := $(nullstring) $(nullstring)
