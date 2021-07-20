1. create udf function with following:
CREATE OR REPLACE FUNCTION UDF_h3
RETURNS TABLE (x DOUBLE NOT NULL, y DOUBLE NOT NULL,res INT NOT NULL, h3 VARCHAR(16) NOT NULL)
MODE = 'distributed'
RUN_COMMAND = '/opt/gpudb/miniconda/bin/python3'
RUN_COMMAND_ARGS = '/opt/gpudb/persist/udf_files/h3udf.py'
FILE PATHS '/opt/gpudb/persist/udf_files/h3udf.py';

2. Execute udf
SELECT distinct(h3) FROM 
TABLE (UDF_h3
(INPUT_TABLE_NAMEs => INPUT_TABLE(select dropoff_latitude as x, dropoff_longitude as y, 5 as res from demo.nyctaxi))
);

