#!/bin/bash

if [ ! -d ../meta ]
then 
	echo "Error. Make sure the folder meta is in the same directory and rerun this script"
	exit 1
fi

echo "MeTA Found"

if [ ! -f ../meta/src/index/tools/relevance-judgements.cpp ] || [ ! -f ../meta/src/index/tools/ranking-experiment.cpp ]
then
	echo "Error. Make sure you have installed Assignment 1."
	exit 1
fi

echo "Copying Assignment 2 files to MeTA"

\cp -f competition.cpp new-judgements.cpp CMakeLists.txt ../meta/src/index/tools/
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Data/moocs-judging-queries.txt Data/moocs-qrels.txt Data/moocs-queries.txt ../meta/data/moocs/
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f config.toml ../meta/build/config.toml
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -rf Assignment2 ../meta/build/
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/ir_eval.cpp ../meta/src/index/eval/ir_eval.cpp
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

echo "Files copied successfully!"
exit 0
