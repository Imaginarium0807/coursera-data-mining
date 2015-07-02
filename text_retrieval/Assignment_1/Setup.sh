#!/bin/bash

if [ ! -d ../meta ]
then 
	echo "Error. Make sure the folder meta is in the same directory and rerun this script"
	exit 1
fi

echo "MeTA Found"

if [ ! -f ../meta/src/tools/profile.cpp ] && [ ! -f ../meta/src/index/tools/CMakeLists.txt ] && [ ! -f ../meta/build/config.toml ]
then
	echo "Error. Make sure you installed MeTA correctly."
	exit 1
fi

echo "Copying assignment 1 files to MeTA"

\cp -f ranking-experiment.cpp relevance-judgements.cpp CMakeLists.txt ../meta/src/index/tools/
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -rf moocs ../meta/data/
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -rf perceptron-tagger ../meta/data/
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f profile.cpp ../meta/src/tools/profile.cpp
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f config.toml ../meta/build/config.toml
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -rf Assignment1 ../meta/build/
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi


### PATCH ###
\cp -f Patch/sgd.h ../meta/include/classify/classifier/sgd.h
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/linear_model.h ../meta/include/classify/models/linear_model.h
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/linear_model.tcc ../meta/include/classify/models/linear_model.tcc
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/transition.h ../meta/include/parser/transition.h
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/lda_cvb.h ../meta/include/topics/lda_cvb.h
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/lda_gibbs.h ../meta/include/topics/lda_gibbs.h
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/depth_featurizer.cpp ../meta/src/parser/analyzers/featurizers/depth_featurizer.cpp
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/parser_train.cpp ../meta/src/parser/tools/parser_train.cpp
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/transition_map.cpp ../meta/src/parser/transition_map.cpp
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi

\cp -f Patch/sequence_analyzer.cpp ../meta/src/sequence/sequence_analyzer.cpp
if [ ! $? -eq 0 ]; then echo "Error. Make sure the script has enough writing privileges"; exit 1; fi
### END OF PATCH ###

echo "Files copied successfully!"
exit 0
