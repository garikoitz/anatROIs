docker run -ti --rm  $4 \
	       -v $2/input:/flywheel/v0/input  \
   	       -v $2/output:/flywheel/v0/output  \
           -v $3:/flywheel/v0/config.json \
   	       garikoitz/anatrois:$1
