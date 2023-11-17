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
            convert_file_to_csv_revenue(source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_order_intake(source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_order_backlog(source_file_path, clean=clean, quiet=quiet)
            convert_file_to_csv_key_figures(source_file_path, clean=clean, quiet=quiet)


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


def convert_file_to_csv_revenue(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-3-revenue.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab3"
        skiprows = 5
        names = ["year_month", "total_revenue", "construction_industry_revenue", "building_construction", "residential",
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


def convert_file_to_csv_order_intake(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-4-order-intake.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab4"
        skiprows = 5
        names = ["year_month", "total", "building_construction", "residential",
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


def convert_file_to_csv_order_backlog(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-5-order-backlog.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab5"
        skiprows = 5
        names = ["year_month", "total", "building_construction", "residential",
                 "commercial_and_industrial", "public", "underground_construction",
                 "commercial_and_industrial_underground_construction", "road_construction",
                 "other_underground_construction"]
        drop_columns = ["year_month"]

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .replace("... ", None) \
            .assign(year_month=lambda df: df["year_month"].astype(str)) \
            .dropna() \
            .assign(total=lambda df: df["total"].astype(int)) \
            .assign(building_construction=lambda df: df["building_construction"].astype(int)) \
            .assign(residential=lambda df: df["residential"].astype(int)) \
            .assign(commercial_and_industrial=lambda df: df["commercial_and_industrial"].astype(int)) \
            .assign(public=lambda df: df["public"].astype(int)) \
            .assign(underground_construction=lambda df: df["underground_construction"].astype(int)) \
            .assign(commercial_and_industrial_underground_construction=lambda df: df[
            "commercial_and_industrial_underground_construction"].astype(int)) \
            .assign(road_construction=lambda df: df["road_construction"].astype(int)) \
            .assign(other_underground_construction=lambda df: df["other_underground_construction"].astype(int))

        dataframe = dataframe[~dataframe["year_month"].str.contains("Vorquartal")]
        dataframe = dataframe[~dataframe["year_month"].str.contains("Vorjahresquartal")]
        dataframe = dataframe.drop(columns=drop_columns, errors="ignore").tail(1)

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


def convert_file_to_csv_key_figures(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name}-6-key-figures.csv"

    # Check if result needs to be generated
    if not clean and os.path.exists(file_path_csv):
        if not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
        return

    # Determine engine
    engine = build_engine(source_file_extension)

    try:
        # Iterate over sheets
        sheet = "Tab6"
        skiprows = 5
        names = ["id", "branch", "companies", "employees", "working_hours", "salaries", "construction_industry_revenue"]
        drop_columns = []

        dataframe = pd.read_excel(source_file_path, engine=engine, sheet_name=sheet, skiprows=skiprows, names=names,
                                  index_col=False) \
            .replace("•", 0) \
            .replace("–", 0) \
            .dropna() \
            .assign(branch=lambda df: df["branch"].apply(lambda row: build_branch_name(row)))

        dataframe.reset_index(drop=True, inplace=True)
        dataframe = dataframe.assign(type_index=lambda df: df.index) \
            .assign(type_parent_index=lambda df: df.apply(lambda row: build_type_parent_index_6(row), axis=1)) \
            .fillna(-1) \
            .assign(type_parent_index=lambda df: df["type_parent_index"].astype(int))
        dataframe.insert(0, "type_index", dataframe.pop("type_index"))
        dataframe.insert(1, "type_parent_index", dataframe.pop("type_parent_index"))

        dataframe.replace("\n41.2/42\n43.1/43.9", "41.2 / 42 / 43.1 / 43.9", inplace=True)

        # Write csv file
        write_csv_file(dataframe, file_path_csv, quiet)
    except Exception as e:
        print(f"✗️ Exception: {str(e)}")


#
# Transformers
#

def build_branch_name(value):
    value = str(value).lstrip().rstrip()

    if value == "Bauhauptgewerbe insgesamt":
        return "construction_industry_total"
    elif value == "Bau von Gebäuden":
        return "buildings"
    elif value == "Bau von Gebäuden (ohne Fertigteilbau)":
        return "buildings_excluding_prefabricated_construction"
    elif value == "Errichtung von Fertigteilbauten":
        return "prefabricated_buildings"
    elif value == "Tiefbau":
        return "underground_construction"
    elif value == "Bau von Straßen und  Bahnverkehrsstrecken":
        return "roads_and_railways"
    elif value == "Bau von Straßen":
        return "roads"
    elif value == "Bau von Bahnverkehrsstrecken":
        return "railways"
    elif value == "Brücken- und Tunnelbau":
        return "bridges_and_tunnels"
    elif value == "Leitungstiefbau und Kläranlagenbau":
        return "pipeline_and_sewage_plant_construction"
    elif value == "Rohrleitungstiefbau, Brunnen- und Kläranlagenbau":
        return "pipeline_well_and_sewage_plant_construction"
    elif value == "Kabelnetzleitungstiefbau":
        return "cable_network_construction"
    elif value == "Sonstiger Tiefbau":
        return "other_underground_construction"
    elif value == "Wasserbau":
        return "hydraulic_construction"
    elif value == "Sonstiger Tiefbau a.n.g.":
        return "still_other_underground_construction"
    elif value == "Abbrucharbeiten und \nvorbereitende Baustellenarbeiten":
        return "demolition_and_preprartory_site_work"
    elif value == "Abbrucharbeiten":
        return "demolition_work"
    elif value == "Vorbereitende Baustellenarbeiten":
        return "preprartory_site_work"
    elif value == "Test- und Suchbohrung":
        return "test_and_search_drilling"
    elif value == "Sonstige spezialisierte Bautätigkeiten":
        return "other_specialized_construction_work"
    elif value == "Dachdeckerei und Zimmerei":
        return "roofing_and_carpentry"
    elif value == "Dachdeckerei und Bauspenglerei":
        return "roofing_and_plumbing"
    elif value == "Zimmerei und Ingenieurholzbau":
        return "carpentry_and_timber_engineering"
    elif value == "Sonstige spezialisierte Bautätigkeiten a.n.g.":
        return "still_other_specialized_construction_work"
    elif value == "Gerüstbau":
        return "scaffolding"
    elif value == "Schornstein-, Feuerungs- und Industrieofenbau":
        return "chimney_and_furnace_construction"
    elif value == "Baugewerbe a.n.g.":
        return "other_building_industry"

    return value


def build_type_parent_index_6(row):
    row_index = row.name

    if row_index == 0:
        return -1
    elif row_index == 1:
        return 0
    elif row_index == 2:
        return 1
    elif row_index == 3:
        return 1
    elif row_index == 4:
        return 0
    elif row_index == 5:
        return 4
    elif row_index == 6:
        return 5
    elif row_index == 7:
        return 5
    elif row_index == 8:
        return 5
    elif row_index == 9:
        return 4
    elif row_index == 10:
        return 9
    elif row_index == 11:
        return 9
    elif row_index == 12:
        return 4
    elif row_index == 13:
        return 12
    elif row_index == 14:
        return 12
    elif row_index == 15:
        return 0
    elif row_index == 16:
        return 15
    elif row_index == 17:
        return 15
    elif row_index == 18:
        return 15
    elif row_index == 19:
        return 0
    elif row_index == 20:
        return 19
    elif row_index == 21:
        return 20
    elif row_index == 22:
        return 20
    elif row_index == 23:
        return 19
    elif row_index == 24:
        return 23
    elif row_index == 25:
        return 23
    elif row_index == 26:
        return 23


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
