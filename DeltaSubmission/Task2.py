import pandas as pd

def get_latest_flight_status(file_path):
    """
    Reads an Excel file with flight data, auto-detects the header row since Delta Metadata contained above,
    combines date and time into a proper datetime, drops carrier_code,
    and returns the most recent status for each flightkey.

    Parameters:
        file_path (str): Path to the Excel file.

    Returns:
        pd.DataFrame: Table with the most recent flight status for each flightkey.
    """
    # Read Excel without header
    df = pd.read_excel(file_path, header=None)

    # Detect header row by looking for 'flightkey'
    header_row = df.apply(lambda row: row.astype(str).str.lower().eq('flightkey').any(), axis=1).idxmax()

    if pd.isna(header_row):
        raise ValueError("Could not find the header row in the file.")

    # Assign column names from header row
    df.columns = df.iloc[header_row]

    # Keep only rows below the header
    df = df.iloc[header_row + 1:].reset_index(drop=True)

    # Drop carrier_code if present (case-insensitive)
    carrier_cols = [col for col in df.columns if str(col).strip().lower() in ["carrier code", "carrier_code"]]
    if carrier_cols:
        df = df.drop(columns=carrier_cols)

    # Ensure flight_dt is date and combine with lastupdt
    df['flight_dt'] = pd.to_datetime(df['flight_dt'], errors='coerce').dt.date
    df['lastupdt'] = pd.to_datetime(
        df['flight_dt'].astype(str) + " " + df['lastupdt'].astype(str),
        errors='coerce'
    )

    # Sort so most recent lastupdt is first per flightkey
    df = df.sort_values(by=['flightkey', 'lastupdt'], ascending=[True, False])

    # Deduplicate: keep only the most recent entry per flightkey
    latest_df = df.groupby('flightkey', as_index=False).first()

    return latest_df
