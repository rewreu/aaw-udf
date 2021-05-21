from kinetica_proc import ProcData
proc_data = ProcData()

df = proc_data.to_df()

df["BMI"] = df["weightKg"]/df["heightM"]

output_table = proc_data.output_data[0]

output_table.size = df.shape[0]
proc_data.from_df(df, output_table)