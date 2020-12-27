#!/bin/bash
# docker build --no-cache --tag scitran/freesurfer-recon-all `pwd`
GEAR=garikoitz/anatrois
docker build --tag $GEAR:$1 .
