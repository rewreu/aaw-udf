0. make sure UDF is on, set `enable_procs = true` in configure.
1. ssh to kinetica instance
2. on kinetica instance switch user to gpudb 
    ```
    sudo su gpudb
    ```
3. download the bmi.py 
    ```
    wget -P /opt/gpudb/persist/udf_files/ https://raw.githubusercontent.com/rewreu/aaw-udf/main/udf/example/bmi.py
    ```
4. Create tables:
    ```sql
    CREATE OR REPLACE TABLE "ki_home"."health"
        (
        "weightKg" DOUBLE NOT NULL,
        "heightM" DOUBLE NOT NULL
        );
    CREATE OR REPLACE TABLE "ki_home"."BMI"
        (
        "weightKg" DOUBLE NOT NULL,
        "heightM" DOUBLE NOT NULL,
        "BMI" DOUBLE NOT NULL
        );
    INSERT INTO "ki_home"."health" ("weightKg", "heightM")
    VALUES
    (70, 1.75)
    (52, 1.64)
    (8, 0.64)
    ```
4. run the following SQL to register udf
    ```sql
    CREATE OR REPLACE FUNCTION UDF_copy
    RETURNS TABLE (weightKg DOUBLE NOT NULL, heightM DOUBLE NOT NULL, BMI DOUBLE NOT NULL)
    MODE = 'distributed'
    RUN_COMMAND = 'python'
    RUN_COMMAND_ARGS = '/opt/gpudb/persist/udf_files/bmi.py'
    FILE PATHS '/opt/gpudb/persist/udf_files/bmi.py'
    ```
------------------------------------------------------------

5. Execute UDF in 2 ways:
    

    1). run on subquery, write to output table
    ```sql
    EXECUTE FUNCTION UDF_copy
    (   INPUT_TABLE_NAMES =>(select weightKg, heightM from ki_home.health where heightM>1),
        OUTPUT_TABLE_NAMES =>OUTPUT_TABLES('ki_home.BMI')
    );
    ```

    2). run on subquery, return result for query
    ```sql
    SELECT *, BMI/703 as BMI_in_lb_in FROM 
    TABLE (UDF_copy
    (INPUT_TABLE_NAMEs => INPUT_TABLE(select weightKg, heightM from ki_home.health where heightM>1))
    );
    ```