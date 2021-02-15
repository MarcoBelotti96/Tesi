#!/bin/bash

latexmk  -pdf -pdflatex="pdflatex" -bibtex $(grep -l documentclass *tex)
evince *pdf &
