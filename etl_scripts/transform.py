import pandas as pd
from geopy.distance import geodesic

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: f'{x:,.2f}')  #show large numbers without scientific notation


def profile_data(df):

    print("\n" + "=" * 14)
    print("DATA PROFILING")
    print("=" * 14)

    print("\nDataset Shape:")
    print(df.shape)

    duplicate_count = df.duplicated().sum()

    print(f"\nDuplicate Rows: {duplicate_count}")

    print("\nMissing Values:")
    print(df.isnull().sum())

    return df



def clean_missing_values(df):

    print("\n" + "=" * 22)
    print("MISSING VALUE CLEANING")
    print("=" * 22)

    df["Ancillary_Revenue"] = df["Ancillary_Revenue"].fillna(0)
    df["Catering_Cost"] = df["Catering_Cost"].fillna(0)
    df["Handling_Cost"] = df["Handling_Cost"].fillna(0)

    print("\nRemaining Missing Values:")

    print(df.isnull().sum())
    
    return df
    


def validate_data(df):

    print("\n" + "=" * 23)
    print("DATA QUALITY VALIDATION")
    print("=" * 23)

    critical_columns = [
        "Route",
        "Aircraft_Type",
        "Total_Revenue",
        "Total_Cost",
        "Profit"
    ]

    quality_score = (
        1 -
        (
            df[critical_columns]
            .isnull()
            .sum()
            .sum()
            /
            (len(df) * len(critical_columns))
        )
    ) * 100

    print(f"\nData Quality Score: {quality_score:.2f}%")

    route_validity = (
        df["Route"] ==
        df["Origin"] + "-" + df["Destination"]
    )

    route_accuracy = route_validity.mean() * 100
    print(f"Route Accuracy: {route_accuracy:.2f}%")

    capacity_validity = (
        df["Passengers"] <= df["Aircraft_Capacity"]
    )

    capacity_accuracy = capacity_validity.mean() * 100
    print(f"Capacity Validation: {capacity_accuracy:.2f}%")


airport_coords = {
    "DXB": (25.2532, 55.3657),
    "DOH": (25.2731, 51.6081),
    "MCT": (23.5933, 58.2844),
    "KWI": (29.2266, 47.9689),
    "BAH": (26.2708, 50.6336),
    "RUH": (24.9576, 46.6988),
    "JED": (21.6702, 39.1525),
    "CAI": (30.1219, 31.4056),
    "AMM": (31.7226, 35.9932),
    "BOM": (19.0896, 72.8656),
    "DEL": (28.5562, 77.1000),
    "IST": (41.2753, 28.7519),
    "LHR": (51.4700, -0.4543),
    "BLR": (13.1986, 77.7066),
    "HYD": (17.2403, 78.4294),
    "MAA": (12.9900, 80.1693),
    "KHI": (24.9065, 67.1608),
    "LHE": (31.5216, 74.4036),
    "CMB": (7.1808, 79.8841),
    "JFK": (40.6413, -73.7781),
    "SYD": (-33.9399, 151.1753),
    "MEL": (-37.6690, 144.8410),
    "SIN": (1.3644, 103.9915),
    "HKG": (22.3080, 113.9185),
    "BKK": (13.6900, 100.7501),
    "KUL": (2.7456, 101.7072),
    "CDG": (49.0097, 2.5479),
    "FRA": (50.0379, 8.5622),
    "LAX": (33.9416, -118.4085),
    "SFO": (37.6213, -122.3790),
    "ORD": (41.9742, -87.9073)
}

def add_distance(df):

    print("\n" + "=" * 28)
    print("Distance in kilometers added")
    print("=" * 28)

    def calculate_distance(origin, destination):

        return round(
            geodesic(
                airport_coords[origin],
                airport_coords[destination]
            ).kilometers,
            0
        )

    df["Distance_KM"] = df.apply(
        lambda row:
        calculate_distance(
            row["Origin"],
            row["Destination"]
        ),
        axis=1
    )
    
    return df



def create_business_metrics(df):

    print("\n" + "=" * 23)
    print("Business metrics added")
    print("=" * 23)

    df["Revenue_Per_Passenger"] = (
        df["Total_Revenue"] /
        df["Passengers"]
    )

    df["Cost_Per_Passenger"] = (
        df["Total_Cost"] /
        df["Passengers"]
    )

    df["Profit_Per_Passenger"] = (
        df["Profit"] /
        df["Passengers"]
    )
    
    return df
    

def create_kpis(df):
    
    print("\n" + "=" * 10)
    print("KPIs added")
    print("=" * 10)

    df["RPK"] = (
        df["Passengers"] *
        df["Distance_KM"]
    )

    df["ASK"] = (
        df["Aircraft_Capacity"] *
        df["Distance_KM"]
    )

    df["RASK"] = (
        df["Total_Revenue"] /
        df["ASK"]
    )

    df["CASK"] = (
        df["Total_Cost"] /
        df["ASK"]
    )

    df["Yield"] = (
        df["Total_Revenue"] /
        df["RPK"]
    )
    
    return df


def transform_data(df):

    profile_data(df)

    df = clean_missing_values(df)

    validate_data(df)

    df = add_distance(df)

    df = create_business_metrics(df)

    df = create_kpis(df)
    
    return df
    

if __name__ == "__main__":

    from extract import extract_data

    df = extract_data()

    transformed_df = transform_data(df)

    print("\n" + "=" * 50)
    print("\nTransformation Complete")
    print("=" * 50)

    print(transformed_df.head())