
# End users are welcome to use any python-3.6 base container of their choice
FROM kinetica/ctnr-kml-base-cpu:revision01

RUN mkdir -p /opt/gpudb/kml
WORKDIR "/opt/gpudb/kml"

ADD spec.json  ./

# Install Required Libraries and Dependencies
ADD requirements.txt  ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Add Kinetica BlackBox SDK
ADD bb_runner.sh ./
ADD sdk ./sdk

# ADD bb_module_default.py ./
ADD bb_module_temperature.py ./
# ADD quantlib_opt_pricer_greeks.py ./

RUN ["chmod", "+x",  "bb_runner.sh"]
ENTRYPOINT ["/opt/gpudb/kml/bb_runner.sh"]