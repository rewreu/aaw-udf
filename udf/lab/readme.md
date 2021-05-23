# UDF lab
Use the bmi example, now instead of one input table, we have two input tables for UDF, one for weight, one for height. 

1. You can use the following to create tables:

    ```sql
    CREATE OR REPLACE TABLE "ki_home"."height"
        (
        "id" INT NOT NULL,
        "heightM" DOUBLE NOT NULL
        );
    CREATE OR REPLACE TABLE "ki_home"."weight"
        (
        "id" INT NOT NULL,
        "weightKg" DOUBLE NOT NULL
        );
    CREATE OR REPLACE TABLE "ki_home"."BMI2"
        (
        "id" INT NOT NULL,
        "BMI_kg_m" DOUBLE NOT NULL,
        "BMI_lb_in" DOUBLE NOT NULL
        );
    INSERT INTO "ki_home"."height" ("id", "heightM")
    VALUES (1, 1.75) (2, 1.64) (3, 0.64) (4, 1.85) (5, 1.64) (6, 0.84) (7, 0.64) (8, 0.44);
    INSERT INTO "ki_home"."weight" ("id", "weightKg")
    VALUES (1, 78.9) (2, 76.4) (3, 8.4) (4, 1.75) (5, 65.9) (6, 9.4) (7, 7.96) (8, 8.42);  
    ```

2. Modify bmi.py to take two tables as input tables.
With multiple input tables, the `proc_data.to_df()` gives a pandas series instead of one dataframe. You can get dataframe by index, the 1st table in dataframe will be proc_data.to_df()[0], the 2nd table in dataframe will be proc_data.to_df()[1].
3. Let's add BMI in two units in the output table, BMI_kg_m, BMI_lb_in. BMI_lb_in = BMI_kg_m/703
4. When using SQL to execute UDF, you can pass two tables like following:
    ```sql
    INPUT_TABLES
    (
        (SELECT id, name FROM customer),
        (SELECT id, customer_id FROM order)
    )
    ```
    More info on SQL udf can be found at: https://docs.kinetica.com/7.1/concepts/sql/#user-defined-functions-udfs