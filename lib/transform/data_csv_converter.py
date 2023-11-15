import os

import pandas as pd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_to_csv(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):
        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for file_name in [file_name for file_name in sorted(files)
                          if not file_name.startswith(f"~") and
                             (file_name.endswith(".xlsx") or file_name.endswith(".xls"))]:
            source_file_path = os.path.join(source_path, subdir, file_name)

            convert_file_to_csv_companies_employees_salaries(source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_working_hours(source_file_path, clean=clean, quiet=quiet)


def convert_file_to_csv_companies_employees_salaries(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-1-companies-employees-salaries.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab1"
        skiprows = 5
        names = ["year_month", "companies", "employees", "salaries"]
        drop_columns = ["year_month"]

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .replace("... ", None) \
            .assign(year_month=lambda df: df["year_month"].astype(str)) \
            .dropna()

        dataframe = dataframe[~dataframe["year_month"].str.contains("Vormonat")]
        dataframe = dataframe[~dataframe["year_month"].str.contains("Vorjahresmonat")]
        dataframe = dataframe.drop(columns=drop_columns, errors="ignore").tail(1)

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_working_hours(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-2-working-hours.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab2"
        skiprows = 5
        names = ["year_month", "working_days", "working_hours_total", "building_construction", "residential",
                 "commercial_and_industrial", "public", "underground_construction",
                 "commercial_and_industrial_underground_construction", "road_construction",
                 "other_underground_construction"]
        drop_columns = ["year_month"]

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .replace("... ", None) \
            .assign(year_month=lambda df: df["year_month"].astype(str)) \
            .dropna()

        dataframe = dataframe[~dataframe["year_month"].str.contains("Vormonat")]
        dataframe = dataframe[~dataframe["year_month"].str.contains("Vorjahresmonat")]
        dataframe = dataframe.drop(columns=drop_columns, errors="ignore").tail(1)

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


#
# Helpers
#

def build_engine(source_file_extension):
    return "openpyxl" if source_file_extension == ".xlsx" else None


def write_csv_file(dataframe, file_path, quiet):
    if dataframe.shape[0] > 0:
        dataframe.to_csv(file_path, index=False)
        if not quiet:
            print(f"✓ Convert {os.path.basename(file_path)}")
    else:
        if not quiet:
            print(dataframe.head())
            print(f"✗️ Empty {os.path.basename(file_path)}")
