# Data Product Canvas

## Domain

## Data Product Name

## Input Ports

**Input ports define the format and protocol in which data can be read (database, file, API, visualizations)**

This data product uses statistical population data provided
by [Amt für Statistik Berlin-Brandenburg](https://www.statistik-berlin-brandenburg.de/) available under the following
URLs

- [SB_E02-01-00_2023m11_BE.xlsx](https://download.statistik-berlin-brandenburg.de/20783b8df599495b/2c00c21bcd09/SB_E02-01-00_2023m11_BE.xlsx)
- [SB_E02-01-00_2023m10_BE.xlsx](https://download.statistik-berlin-brandenburg.de/c53a4dcdccef9639/b5b47e839d2d/SB_E02-01-00_2023m10_BE.xlsx)
- [SB_E02-01-00_2023m09_BE.xlsx](https://download.statistik-berlin-brandenburg.de/2e39d3d762df4fa4/b1adc18f0aff/SB_E02-01-00_2023m09_BE.xlsx)
- [SB_E02-01-00_2023m08_BE.xlsx](https://download.statistik-berlin-brandenburg.de/53ec0fa704233f35/e2ae7ebd4063/SB_E02-01-00_2023m08_BE.xlsx)
- [SB_E02-01-00_2023m07_BE.xlsx](https://download.statistik-berlin-brandenburg.de/8bafa3d7c09d3d78/59da6995d8db/SB_E02-01-00_2023m07_BE.xlsx)
- [SB_E02-01-00_2023m06_BE.xlsx](https://download.statistik-berlin-brandenburg.de/dc3b560eac941472/fc85ce1e4692/SB_E02-01-00_2023m06_BE.xlsx)
- [SB_E02-01-00_2023m05_BE.xlsx](https://download.statistik-berlin-brandenburg.de/7883d7658ad90e53/1ff05f83da14/SB_E02-01-00_2023m05_BE.xlsx)
- [SB_E02-01-00_2023m04_BE.xlsx](https://download.statistik-berlin-brandenburg.de/c9da9c2763b0d047/dff773321533/SB_E02-01-00_2023m04_BE.xlsx)
- [SB_E02-01-00_2023m03_BE.xlsx](https://download.statistik-berlin-brandenburg.de/213069e3cc0b97dc/389d16cddf60/SB_E02-01-00_2023m03_BE.xlsx)
- [SB_E02-01-00_2023m02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/0ec4658066474458/31cf3c930bff/SB_E02-01-00_2023m02_BE.xlsx)
- [SB_E02-01-00_2023m01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/b37d64f7bbc9f7ea/766b0970a03b/SB_E02-01-00_2023m01_BE.xlsx)
- [SB_E02-01-00_2022m12_BE.xlsx](https://download.statistik-berlin-brandenburg.de/1134506b8c880793/898da831d16a/SB_E02-01-00_2022m12_BE.xlsx)
- [SB_E02-01-00_2022m11_BE.xlsx](https://download.statistik-berlin-brandenburg.de/45a413a894d7c88d/6a3d88ba61e9/SB_E02-01-00_2022m11_BE.xlsx)
- [SB_E02-01-00_2022m10_BE.xlsx](https://download.statistik-berlin-brandenburg.de/06f6c759c88dbde2/bd0efc6b39c8/SB_E02-01-00_2022m10_BE.xlsx)
- [SB_E02-01-00_2022m09_BE.xlsx](https://download.statistik-berlin-brandenburg.de/ab39b057381ac735/f89b803a1611/SB_E02-01-00_2022m09_BE.xlsx)
- [SB_E02-01-00_2022m08_BE.xlsx](https://download.statistik-berlin-brandenburg.de/334613816622833c/e6601aed2490/SB_E02-01-00_2022m08_BE.xlsx)
- [SB_E02-01-00_2022m07_BE.xlsx](https://download.statistik-berlin-brandenburg.de/77668c5f215fe43a/531c9a185b5f/SB_E02-01-00_2022m07_BE.xlsx)
- [SB_E02-01-00_2022m06_BE.xlsx](https://download.statistik-berlin-brandenburg.de/1392b49e4b702cfc/4e9cd908694f/SB_E02-01-00_2022m06_BE.xlsx)
- [SB_E02-01-00_2022m05_BE.xlsx](https://download.statistik-berlin-brandenburg.de/a8991968a9e5e5aa/da07bc7a9252/SB_E02-01-00_2022m05_BE.xlsx)
- [SB_E02-01-00_2022m04_BE.xlsx](https://download.statistik-berlin-brandenburg.de/8c116bed462a8cb1/bf228b7b3805/SB_E02-01-00_2022m04_BE.xlsx)
- [SB_E02-01-00_2022m03_BE.xlsx](https://download.statistik-berlin-brandenburg.de/9dcc61cd117f0963/b852e673c60b/SB_E02-01-00_2022m03_BE.xlsx)
- [SB_E02-01-00_2022m02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/451f5ba35a97c17b/aee11fcad659/SB_E02-01-00_2022m02_BE.xlsx)
- [SB_E02-01-00_2022m01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/999b83359a4776dc/93781a6d25f1/SB_E02-01-00_2022m01_BE.xlsx)

## Data Product Design

**Describe everything you need to design a data product on a conceptual level.**
**Ingestion, storage, transport, wrangling, cleaning, transformations, enrichment, augmentation, analytics, SQL
statements, or used data platform services.**

This data product

* [converts Excel data into csv](../lib/transform/data_csv_converter.py)

## Output Port

**Output ports define the format and protocol in which data can be exposed (db, file, API, visualizations)**

The data of this data product is available under the following URLs

- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-2-working-hours.csv)
- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-3-revenue.csv)
- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-4-order-intake.csv)
- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-5-order-backlog.csv)
- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-6-key-figures.csv)
- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-01/berlin-building-industry-2022-01-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-01/berlin-building-industry-2022-01-8-key-figures-extension.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-2-working-hours.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-3-revenue.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-4-order-intake.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-5-order-backlog.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-6-key-figures.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-02/berlin-building-industry-2022-02-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-02/berlin-building-industry-2022-02-8-key-figures-extension.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-2-working-hours.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-3-revenue.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-4-order-intake.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-5-order-backlog.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-6-key-figures.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-03/berlin-building-industry-2022-03-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-03/berlin-building-industry-2022-03-8-key-figures-extension.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-2-working-hours.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-3-revenue.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-4-order-intake.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-5-order-backlog.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-6-key-figures.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-04/berlin-building-industry-2022-04-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-04/berlin-building-industry-2022-04-8-key-figures-extension.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-2-working-hours.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-3-revenue.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-4-order-intake.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-5-order-backlog.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-6-key-figures.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-05/berlin-building-industry-2022-05-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-05/berlin-building-industry-2022-05-8-key-figures-extension.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-2-working-hours.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-3-revenue.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-4-order-intake.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-5-order-backlog.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-6-key-figures.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-06/berlin-building-industry-2022-06-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-06/berlin-building-industry-2022-06-8-key-figures-extension.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-2-working-hours.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-3-revenue.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-4-order-intake.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-5-order-backlog.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-6-key-figures.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-07/berlin-building-industry-2022-07-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-07/berlin-building-industry-2022-07-8-key-figures-extension.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-2-working-hours.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-3-revenue.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-4-order-intake.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-5-order-backlog.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-6-key-figures.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-08/berlin-building-industry-2022-08-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-08/berlin-building-industry-2022-08-8-key-figures-extension.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-2-working-hours.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-3-revenue.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-4-order-intake.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-5-order-backlog.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-6-key-figures.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-09/berlin-building-industry-2022-09-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-09/berlin-building-industry-2022-09-8-key-figures-extension.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-2-working-hours.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-3-revenue.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-4-order-intake.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-5-order-backlog.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-6-key-figures.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-10/berlin-building-industry-2022-10-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-10/berlin-building-industry-2022-10-8-key-figures-extension.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-2-working-hours.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-3-revenue.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-4-order-intake.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-5-order-backlog.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-6-key-figures.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-11/berlin-building-industry-2022-11-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-11/berlin-building-industry-2022-11-8-key-figures-extension.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-1-companies-employees-salaries.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-2-working-hours.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-3-revenue.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-4-order-intake.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-5-order-backlog.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-6-key-figures.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2022-12/berlin-building-industry-2022-12-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2022-12/berlin-building-industry-2022-12-8-key-figures-extension.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-2-working-hours.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-3-revenue.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-4-order-intake.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-5-order-backlog.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-6-key-figures.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-01/berlin-building-industry-2023-01-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-01/berlin-building-industry-2023-01-8-key-figures-extension.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-2-working-hours.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-3-revenue.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-4-order-intake.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-5-order-backlog.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-6-key-figures.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-02/berlin-building-industry-2023-02-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-02/berlin-building-industry-2023-02-8-key-figures-extension.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-2-working-hours.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-3-revenue.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-4-order-intake.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-5-order-backlog.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-6-key-figures.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-03/berlin-building-industry-2023-03-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-03/berlin-building-industry-2023-03-8-key-figures-extension.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-2-working-hours.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-3-revenue.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-4-order-intake.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-5-order-backlog.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-6-key-figures.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-04/berlin-building-industry-2023-04-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-04/berlin-building-industry-2023-04-8-key-figures-extension.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-2-working-hours.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-3-revenue.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-4-order-intake.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-5-order-backlog.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-6-key-figures.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-05/berlin-building-industry-2023-05-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-05/berlin-building-industry-2023-05-8-key-figures-extension.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-2-working-hours.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-3-revenue.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-4-order-intake.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-5-order-backlog.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-6-key-figures.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-06/berlin-building-industry-2023-06-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-06/berlin-building-industry-2023-06-8-key-figures-extension.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-2-working-hours.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-3-revenue.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-4-order-intake.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-5-order-backlog.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-6-key-figures.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-07/berlin-building-industry-2023-07-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-07/berlin-building-industry-2023-07-8-key-figures-extension.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-2-working-hours.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-3-revenue.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-4-order-intake.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-5-order-backlog.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-6-key-figures.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-08/berlin-building-industry-2023-08-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-08/berlin-building-industry-2023-08-8-key-figures-extension.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-2-working-hours.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-3-revenue.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-4-order-intake.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-5-order-backlog.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-6-key-figures.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-09/berlin-building-industry-2023-09-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-09/berlin-building-industry-2023-09-8-key-figures-extension.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-2-working-hours.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-3-revenue.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-4-order-intake.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-5-order-backlog.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-6-key-figures.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-10/berlin-building-industry-2023-10-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-10/berlin-building-industry-2023-10-8-key-figures-extension.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-1-companies-employees-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-1-companies-employees-salaries.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-2-working-hours.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-2-working-hours.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-3-revenue.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-3-revenue.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-4-order-intake.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-4-order-intake.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-5-order-backlog.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-5-order-backlog.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-6-key-figures.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-6-key-figures.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-7-companies-employees-working-hours-salaries.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-7-companies-employees-working-hours-salaries.csv)
- [berlin-building-industry-2023-11/berlin-building-industry-2023-11-8-key-figures-extension.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-building-industry-source-aligned/main/data/berlin-building-industry-2023-11/berlin-building-industry-2023-11-8-key-figures-extension.csv)

## Metadata

### Ownership

**Domain, data product owner, organizational unit, license, version and expiration date**

### Schema

**Attributes, data types, constraints, and relationships to other elements**

#### 1 companies, employees and salaries

- `companies`: number of companies
- `employees`: number of employees
- `salaries`: salaries in 1000 Euros

#### 2 working hours

- `working_days`: number of working days
- `working_hours_total`: number of working hours in 1000 h
- `building_construction`: number of working hours in building construction in 1000 h
- `residential`: number of working hours in residential buildings 1000 h
- `commercial_and_industrial`: number of working hours in commercial and industrial buildings in 1000 h
- `public`: number of working hours in public buildings in 1000 h
- `underground_construction`: number of working hours in underground construction in 1000 h
- `commercial_and_industrial_underground_construction`: number of working hours in commercial and industrial underground
  construction in 1000 h
- `road_construction`: number of working hours in road construction in 1000 h
- `other_underground_construction`: number of working hours in other underground construction in 1000 h

#### 3 revenue

- `total_revenue`: total revenue in 1000 Euros
- `construction_industry_revenue`: revenue in construction industry in 1000 Euros
- `building_construction`: revenue in building construction in 1000 Euros
- `residential`: revenue in residential buildings 1000 Euros
- `commercial_and_industrial`: revenue in commercial and industrial buildings in 1000 Euros
- `public`: revenue in public buildings in 1000 Euros
- `underground_construction`: revenue in underground construction in 1000 Euros
- `commercial_and_industrial_underground_construction`: revenue in commercial and industrial underground construction in
  1000 Euros
- `road_construction`: revenue in road construction in 1000 Euros
- `other_underground_construction`: revenue in other underground construction in 1000 Euros

#### 4 order intake

- `total`: total order intake
- `building_construction`: building construction
- `residential`: residential buildings
- `commercial_and_industrial`: commercial and industrial buildings
- `public`: public buildings
- `underground_construction`: underground construction
- `commercial_and_industrial_underground_construction`: commercial and industrial underground construction
- `road_construction`: road construction
- `other_underground_construction`: other underground construction

#### 5 order backlog

- `total`: total order backlog
- `building_construction`: building construction
- `residential`: residential buildings
- `commercial_and_industrial`: commercial and industrial buildings
- `public`: public bildings
- `underground_construction`: underground construction
- `commercial_and_industrial_underground_construction`: commercial and industrial underground construction
- `road_construction`: road construction
- `other_underground_construction`: other underground construction

#### 6 key figures

- `id`: ID
- `branch`: branch
- `companies`: number of companies
- `employees`: number of employees
- `working_hours`: number of working hours in 1000h
- `salaries`: salaries in 1000 Euros
- `construction_industry_revenue`: construction_industry_revenue in 1000 Euros

#### 7 companies, employees, working hours and salaries

- `companies`: number of companies
- `employees`: number of employees
- `working_hours`: number of working hours in 1000h
- `salaries`: salaries in 1000 Euros
- `total_revenue`: total revenue in 1000 Euros
- `construction_industry_revenue`: construction industry revenue in 1000 Euros

#### 8 key figures extension

- `id`: ID
- `branch`: branch
- `companies`: number of companies
- `employees`: number of employees
- `working_hours`: number of working hours in 1000h
- `salaries`: salaries in 1000 Euros
- `construction_industry_revenue`: construction_industry_revenue in 1000 Euros

### Semantics

**Description, logical model**

### Security

**Security rules applied to the data product usage e.g. public org, internal, personally identifiable information (PII)
attributes**

## Observability

### Quality metrics

**Requirements and metrics such as accuracy, completeness, integrity, or compliance to Data Governance policies**

### Operational metrics

**Interval of change, freshness, usage statistics, availability, number of users, data versioning, etc.**

### SLOs

**Thresholds for service level objectives to up alerting**

## Consumer

**Who is the consumer of the Data Product?**

## Use Case

**We believe that ...**
**We help achieving ...**
**We know, we are getting there based on ..., ..., ...**

We believe that this data product can be used to derive any kind of data based product.

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

This data product is source-aligned since the contained csv files represent the source data.

## Ubiquitous Language

**Context-specific domain terminology (relevant for Data Product), Data Product polysemes which are used to create the
current Data Product**

---
This data product canvas uses the template
of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).
