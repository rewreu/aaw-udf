# Run UDF in SQL

Before registering and executing UDF, use Kinetica Gadmin UI to set up nyctaix table. Then copy `h3udf.py` to `/opt/gpudb/persist/udf_files/h3udf.py`. Make sure the file's owner is gpudb. If the python env is not from Kinetica, then also copy [kinetica_proc.py](https://github.com/kineticadb/kinetica-udf-api-python/blob/master/kinetica_proc.py) file to same location and change ownership.
### Use UDF to calculate H3
1. Use the following statement create the UDF SQL function:
  ```sql
  CREATE OR REPLACE FUNCTION UDF_h3
  RETURNS TABLE (x DOUBLE NOT NULL, y DOUBLE NOT NULL,res INT NOT NULL, h3 VARCHAR(16) NOT NULL)
  MODE = 'distributed'
  RUN_COMMAND = '/opt/gpudb/miniconda/bin/python3'
  RUN_COMMAND_ARGS = '/opt/gpudb/persist/udf_files/h3udf.py'
  FILE PATHS '/opt/gpudb/persist/udf_files/h3udf.py'
  ```

2. Use the following to run the UDF and return to select statement:
  ```sql
  SELECT x,y,h3 FROM 
  TABLE (UDF_h3
  (INPUT_TABLE_NAMEs => (select dropoff_latitude as x, dropoff_longitude as y, 3 as res from demo.nyctaxi))
  ) limit 5;
  ```

3. Use the following to run the UDF and run a groupby:
  ```sql
  SELECT avg(x),avg(y),h3 FROM 
  TABLE (UDF_h3
  (INPUT_TABLE_NAMEs => (select dropoff_latitude as x, dropoff_longitude as y, 3 as res from demo.nyctaxi))
  )
  group by h3;
  ```


### Use UDF to calculate H3 and pass vendor_id
``` sql
CREATE OR REPLACE FUNCTION UDF_h3_2
RETURNS TABLE (x DOUBLE NOT NULL, y DOUBLE NOT NULL,res INT NOT NULL, h3 VARCHAR(16) NOT NULL, vendor_id VARCHAR(4) NOT NULL)
MODE = 'distributed'
RUN_COMMAND = '/opt/gpudb/miniconda/bin/python3'
RUN_COMMAND_ARGS = '/opt/gpudb/persist/udf_files/h3udf.py'
FILE PATHS '/opt/gpudb/persist/udf_files/h3udf.py'
```

```sql
SELECT x,y,h3,vendor_id FROM 
TABLE (UDF_h3_2
(INPUT_TABLE_NAMEs => (select dropoff_latitude as x, dropoff_longitude as y, 3 as res,vendor_id from demo.nyctaxi))
) limit 5;
```

```
SELECT avg(x),avg(y),h3,vendor_id FROM 
TABLE (UDF_h3_2
(INPUT_TABLE_NAMEs => (select dropoff_latitude as x, dropoff_longitude as y, 3 as res, vendor_id from demo.nyctaxi))
)
group by h3,vendor_id;
```
