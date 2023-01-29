#!/usr/bin/env bash
python -m venv $HOME/.code-venv
PATH="$HOME/.code-venv/bin:$PATH" VIRTUAL_ENV="$HOME/.code-venv" poetry install
	