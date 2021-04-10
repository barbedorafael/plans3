# Plans3

Here we go!ok 

# input files
## `aoi_basin.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Boolean raster map of the area of AOI (Area Of Interest) basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: boolean (1.0 and 0.0).
*  Cells must be 1.0 where the the area is TRUE and 0.0 where the area is FALSE.


## `aoi_catcha.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of catchment area (also known as flow accumulation) of the AOI basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: squared meters.


## `aoi_dem.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of Digital Elevation Model (DEM) of the AOI basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.


## `aoi_lulc_param.txt`
**IO:** input.

**File type:** csv data frame.

**Description:**
Data frame of LULC classes for the AOI basin.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `Id`: unique integer number of LULC class index.
*  `LULC`: one-word name of LULC class.
*  `f_Canopy`:  positive real number of factor of maximal effective canopy storage capacity in any units.
*  `f_RootDepth`: positive real number of fator of maximal effective root zone depth in any units.
*  `f_Depression`: positive real number of maximal effective surface depression storage capacity in any units.


**Example:**
```
 Id;      LULC; f_Canopy; f_RootDepth; f_Depression;
  1;    Forest;     1100;        15.1;         15.5;
  2;     Urban;      180;         3.5;          0.1;
  3;     Water;      0.0;         0.0;        103.0;
  4;     Crops;      320;         2.8;         20.1;
  5;   Pasture;      500;         4.4;         25.0;
```


## `aoi_lulc_series_input.txt`
**IO:** input.

**File type:** csv data frame.

**Description:**
Yearly time series of input file paths to LULC .asc raster maps of the AOI basin in the observation period.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record (month and day can be arbitrary).
*  `File`: file path to input LULC .asc raster map. Ex: `C:/mydata/lulc_map_01.asc`


**Example:**
```
        Date;                 File;
  2015-01-01;   C:/data/lulc01.asc;
  2016-01-01;   C:/data/lulc02.asc;
           …;                    …;
  2018-01-01;   C:/data/lulc04.asc;
  2019-01-01;   C:/data/lulc05.asc;
```


## `aoi_series.txt`
**IO:** input.

**File type:** csv time series.

**Description:**
Long term daily time series of climatic data for the AOI basin.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `Prec`: daily accumulated precipitation in mm.
*  `Temp`: mean daily temperature in Celsius.


**Example:**
```
        Date;   Prec;   Temp;
  1985-01-01;    0.0;   25.2;
  1986-01-01;   12.1;   23.0;
          … ;     … ;     … ;
  1988-01-01;    0.0;   21.0;
  1989-01-01;    5.0;   22.8;
```


## `aoi_soils.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of soils for the AOI (Area Of Interest) basin. Each soil class receives an index number defined in the soils_calib_param file.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: class index.


## `aoi_soils_param.txt`
**IO:** input.

**File type:** csv data frame.

**Description:**
Data frame of soil classes for the AOI basin.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period  `.`.
*  Mandatory fields:
*  `Id`: unique integer number of soil class index.
*  `SoilClass`: one-word name of soil class.
*  `f_Ksat`:  positive real number of factor of maximal effective saturated hydraulic conductivity in any units.
*  `Porosity`: positive real number of soil porosity.


**Example:**
```
 Id; SoilClass; f_Ksat; Porosity;
  1;    Soil_A;    110;     0.12;
  2;    Soil_B;     98;     0.10;
  3;    Soil_C;     74;     0.08;
  4;    Soil_D;     32;     0.05;
  5;    Soil_E;      5;     0.04;
```


## `aoi_twi.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of the Topographic Wetness Index (TWI) for the AOI basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: TWI units.


## `calib_basin.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Boolean raster map of the area of calibration basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: boolean (1.0 and 0.0).
*  Cells must be 1.0 where the the area is TRUE and 0.0 where the area is FALSE.


## `calib_catcha.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of catchment area (also known as flow accumulation) of the calibration basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: squared meters.


## `calib_dem.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of Digital Elevation Model (DEM) of the calibration basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.


## `calib_etpat.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of ET-proxy pattern for the calibratio basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: any units.


## `calib_lulc.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of LULC (land use and land cover) for the calibration basin and calibration period. Each LULC class receives an index number defined in the lulc_calib_param file

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: class index.


## `calib_lulc_param.txt`
**IO:** input.

**File type:** csv data frame.

**Description:**
Data frame of LULC classes for the calibration basin.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `Id`: unique integer number of LULC class index.
*  `LULC`: one-word name of LULC class.
*  `f_Canopy`:  positive real number of factor of maximal effective canopy storage capacity in any units.
*  `f_RootDepth`: positive real number of fator of maximal effective root zone depth in any units.
*  `f_Depression`: positive real number of maximal effective surface depression storage capacity in any units.


**Example:**
```
 Id;      LULC; f_Canopy; f_RootDepth; f_Depression;
  1;    Forest;     1100;        15.1;         15.5;
  2;     Urban;      180;         3.5;          0.1;
  3;     Water;      0.0;         0.0;        103.0;
  4;     Crops;      320;         2.8;         20.1;
  5;   Pasture;      500;         4.4;         25.0;
```


## `calib_series.txt`
**IO:** input.

**File type:** csv time series.

**Description:**
Daily time series of climatic and hydrologic data for the calibration basin in the calibration period.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `Prec`: daily accumulated precipitation in mm.
*  `Temp`: mean daily temperature in Celsius.
*  `Q`: mean daily specific flow in mm/day (Note: Q = 86400 [s/day] * Flow [m3/s] / BasinArea [m2]).
*  Optional fields:
*  `Flow`: mean daily flow in m3/s.


**Example:**
```
        Date;   Prec;   Temp;        Q;   Flow;
  1985-01-01;    0.0;   25.2;    0.051;   2.43;
  1986-01-01;   12.1;   23.0;    0.050;   2.38;
          … ;     … ;     … ;        …;      …;
  1988-01-01;    0.0;   21.0;    0.047;   2.21;
  1989-01-01;    5.0;   22.8;    0.046;   2.17;
```


## `calib_soils.asc`
**IO:** input.

**File type:** raster map.

**Description:**
Raster map of soils for the calibration basin. Each soil class receives an index number defined in the soils_calib_param file.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: class index.


## `calib_soils_param.txt`
**IO:** input.

**File type:** csv data frame.

**Description:**
Data frame of soil classes for the calibration basin.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period  `.`.
*  Mandatory fields:
*  `Id`: unique integer number of soil class index.
*  `SoilClass`: one-word name of soil class.
*  `f_Ksat`:  positive real number of factor of maximal effective saturated hydraulic conductivity in any units.
*  `Porosity`: positive real number of soil porosity.


**Example:**
```
 Id; SoilClass; f_Ksat; Porosity;
  1;    Soil_A;    110;     0.12;
  2;    Soil_B;     98;     0.10;
  3;    Soil_C;     74;     0.08;
  4;    Soil_D;     32;     0.05;
  5;    Soil_E;      5;     0.04;
```


## `hydro_param.txt`
**IO:** input.

**File type:** csv data frame.

**Description:**
 Data frame of hydrology parameter set and ranges. 
 Parameters are: 
 1) `m` - positive real value of effective transmissivity decay coefficient in mm; 
 2) `qo` -positive real value of maximal baseflow when D=0 in mm/d;  
 3) `cpmax` - positive real value of effective maximal canopy water storage capacity in mm; 
 4) `dpmax` - positive real value of effective maximal depression water storage capacity in mm;  
 5) `rtmax` - positive real value of effective maximal root zone depth in mm.  
 6) `ksat` - positive real value of effective maximal saturated hydraulic conductivity in mm/d; 
 7) `c` - positive real value of scaling parameter for PET model in Celcius;
 8) `lat` - real value of latitude in degrees for PET model;
 9) `k` - positive real value of Nash Cascade residence time in days; 
 10) `n` - positive real value of equivalent number of reservoirs in Nash Cascade;



**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period  `.`.
*  Mandatory fields:
*  `Parameter`: parameter standard names: `m`, `qo`, `cpmax`,  `dpmax`, `rtmax`, `ksat`, `c`,`lat`, `k`, `n`.
*  `Set`: positive real number of parameter set (updated by calibration).
*  `Min`: positive real number of lower bound of parameter space.
*  `Max`: positive real number of upper bound of parameter space.


**Example:**
```
Parameter;     Set;    Min;    Max;
        m;    1.25;    0.1;     10;
       qo;    6.87;    0.1;    100;
    cpmax;    10.1;    0.1;    500;
    dpmax;    50.2;    0.1;    500;
    rtmax;     611;    0.1;    500;
     ksat;    5.24;    0.1;    100;
        c;    98.5;    0.1;    120;
      lat;     -30;    -30;    -30;
        k;     2.4;    0.1;     10;
        n;     5.9;    0.1;     20;
```


# derived files
## `aoi_lulc_YYYY.asc`
**IO:** derived.

**File type:** raster map.

**Description:**
Raster map of LULC of AOI basin in year YYYY.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: class index.


## `aoi_lulc_series.txt`
**IO:** derived.

**File type:** csv data frame.

**Description:**
Yearly time series of project file paths to LULC .asc raster maps of the AOI basin in the observation period.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record (month and day can be arbitrary).
*  `File`: file path to input LULC .asc raster map. Ex: `C:/mydata/lulc_map_01.asc`


**Example:**
```
        Date;                         File;
  2015-01-01;   C:/ … /lulc_2015-01-01.asc;
  2016-01-01;   C:/ … /lulc_2016-01-01.asc;
           …;                           … ;
  2018-01-01;   C:/ … /lulc_2017-01-01.asc;
  2019-01-01;   C:/ … /lulc_2018-01-01.asc;
```


## `aoi_shru_YYYY.asc`
**IO:** derived.

**File type:** raster map.

**Description:**
Raster map of SHRU of AOI basin in year YYYY.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: class index.


## `aoi_shru_param.txt`
**IO:** derived.

**File type:** csv data frame.

**Description:**
Data frame of Surface Hydrologic Response Units (SHRU) classes for the AOI basin.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `Id`: unique integer number of SHRU class index;
*  `SHRU`: one-word name of SHRU class.
*  `f_Ksat`:  positive real number of factor of maximal effective saturated hydraulic conductivity in any units.
*  `Porosity`: positive real number of soil porosity.
*  `f_Canopy`:  positive real number of factor of maximal effective canopy storage capacity in any units.
*  `f_RootDepth`: positive real number of fator of maximal effective root zone depth in any units.
*  `f_Depression`: positive real number of maximal effective surface depression storage capacity in any units.


**Example:**
```
 Id;             SHRU; f_Ksat; Porosity; f_Canopy; f_RootDepth; f_Depression;
  1;    Forest_Soil_A;    110;     0.12;     1100;        15.1;         15.5;
  2;    Forest_Soil_B;     98;     0.10;     1100;        15.1;         15.5;
  3;    Forest_Soil_C;     74;     0.08;     1100;        15.1;         15.5;
  4;     Urban_Soil_B;     98;     0.10;      180;         3.5;          0.1;
  5;     Water_Soil_C;     74;     0.08;      0.0;         0.0;        103.0;
  6;     Crops_Soil_A;    110;     0.12;      320;         2.8;         20.1;
  7;   Pasture_Soil_D;     32;     0.05;      500;         4.4;         25.0;
```


## `aoi_shru_series.txt`
**IO:** derived.

**File type:** csv data frame.

**Description:**
Yearly time series of project file paths to SHRU .asc raster maps of the AOI basin in the observation period.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record (month and day can be arbitrary).
*  `File`: file path to SHRU .asc raster maps.


**Example:**
```
        Date;                         File;
  2015-01-01;   C:/ … /shru_2015-01-01.asc;
  2016-01-01;   C:/ … /shru_2016-01-01.asc;
           …;                           … ;
  2018-01-01;   C:/ … /shru_2017-01-01.asc;
  2019-01-01;   C:/ … /shru_2018-01-01.asc;
```


## `aoi_slope.asc`
**IO:** derived.

**File type:** raster map.

**Description:**
Raster map of terrain slope for the AOI basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: degrees.


## `calib_shru.asc`
**IO:** derived.

**File type:** raster map.

**Description:**
Raster map of Surface Hydrologic Response Units (SHRU) for the calibration basin. Each SHRU class receives an index number defined in the shru_calib_param file.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: class index.


## `calib_shru_param.txt`
**IO:** derived.

**File type:** csv data frame.

**Description:**
Data frame of Surface Hydrologic Response Units (SHRU) classes for the calibration basin.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `Id`: unique integer number of SHRU class index;
*  `SHRU`: one-word name of SHRU class.
*  `f_Ksat`:  positive real number of factor of maximal effective saturated hydraulic conductivity in any units.
*  `Porosity`: positive real number of soil porosity.
*  `f_Canopy`:  positive real number of factor of maximal effective canopy storage capacity in any units.
*  `f_RootDepth`: positive real number of fator of maximal effective root zone depth in any units.
*  `f_Depression`: positive real number of maximal effective surface depression storage capacity in any units.


**Example:**
```
 Id;             SHRU; f_Ksat; Porosity; f_Canopy; f_RootDepth; f_Depression;
  1;    Forest_Soil_A;    110;     0.12;     1100;        15.1;         15.5;
  2;    Forest_Soil_B;     98;     0.10;     1100;        15.1;         15.5;
  3;    Forest_Soil_C;     74;     0.08;     1100;        15.1;         15.5;
  4;     Urban_Soil_B;     98;     0.10;      180;         3.5;          0.1;
  5;     Water_Soil_C;     74;     0.08;      0.0;         0.0;        103.0;
  6;     Crops_Soil_A;    110;     0.12;      320;         2.8;         20.1;
  7;   Pasture_Soil_D;     32;     0.05;      500;         4.4;         25.0;
```


## `calib_slope.asc`
**IO:** derived.

**File type:** raster map.

**Description:**
Raster map of terrain slope for the calibration basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: degrees.


## `calib_twi.asc`
**IO:** derived.

**File type:** raster map.

**Description:**
Raster map of the Topographic Wetness Index (TWI) for the calibration basin.

**Requirements:**
*  Must match the same size (rows and columns) of other related raster maps.
*  Grid cells must be squared.
*  Cells values units: TWI units.


# output files
## `map_Cpy_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Cpy values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_D_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Dps values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Dps_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Dps values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_ET_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of ET values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Evc_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Evc values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Evd_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Evd values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Inf_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Inf values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Qv_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Qv values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_R_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of R values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_TF_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of TF values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Tpgw_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Tpgw values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Tpun_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Tpun values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `map_Unz_YYYY-MM-DD.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of Unz values given TWI (rows) and SHRU index (columns) - the Zmap of the variable.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store the values of the mapped values in positive real numbers.


## `sim_histograms.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of histograms of TWI (rows) and SHRU index (columns). Values are in counted cells.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Mandatory fields:
*  `TWI\SHRU`: TWI positive real values of TWI histogram bins.
*  The `TWI\SHRU` field must be the first field.
*  The following fields after `TWI\SHRU` must be the index number values of each SHRU class and store positive integer values of the histogram of TWI within each SHRU.


## `sim_maps_Cpy.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Cpy.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_D.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Dps.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Dps.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Dps.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_ET.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of ET.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Evc.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Evc.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Evd.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Evd.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Inf.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Qv.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Qv.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_R.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of R.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_TF.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of TF.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Tpgw.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Tpgw.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Tpun.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Tpun.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_maps_Unz.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Daily time series of output file paths to the Z-maps of Unz.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `File`: file path to output Z-map .txt file.


## `sim_parameters.txt`
**IO:** output.

**File type:** csv data frame.

**Description:**
Data frame of hydrology parameters set used in simulation

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period  `.`.
*  Mandatory fields:
*  `Parameter`: parameter standard names: `m`, `ksat`, `qo`, `a`, `c`, `k`, `n`.
*  `Set`: positive real number of parameter set (updated by calibration).
*  `Min`: positive real number of lower bound of parameter space.
*  `Max`: positive real number of upper bound of parameter space.


## `sim_series.txt`
**IO:** output.

**File type:** csv time series.

**Description:**
Simulated daily time series of output hydrologic global variables.

**Requirements:**
*  Field separator: semicolon `;`.
*  Decimal separator: period `.`.
*  Date format: `YYYY-MM-DD`.
*  Mandatory fields:
*  `Date`: date of record.
*  `Prec`: daily accumulated precipitation in mm (from input).
*  `Temp`: mean daily temperature in Celsius (from input).
*  `PET`: Potential evapotranspiration water storage in mm.
*  `D`: Soil water storage deficit for full saturation by water table in mm.
*  `Cpy`: Canopy water storage in mm.
*  `TF`: Throughfall water flow in mm/d.
*  `Dps`: Surface depression water storage in mm.
*  `R`: Runoff water flow in mm/d.
*  `Inf`: Infiltration water flow in mm/d.
*  `Unz`: Unsaturated zone water storage in mm.
*  `Qv`: Recharge water flow in mm/d.
*  `Evc`: Evaporation from canopy water flow in mm/d.
*  `Evd`: Evaporation from surface depression water flow in mm/d.
*  `Tpun`: Plant transpiration from unsaturated zone water flow in mm/d.
*  `Tpgw`: Plant transpiration from groundwater water flow in mm/d.
*  `ET`: Evapotranspiartion water flow in mm/d.
*  `Qb`: basin baseflow in mm/d.
*  `Qs`: basin stormflow in mm/d.
*  `Q`: basin water flow in mm/d.
*  `Flow`: basin water flow in m3/s (note: Flow [m3/s]= Q [mm/d] * BasinArea [m2] / (86400 [s/d] * 1000 [mm/m])).



