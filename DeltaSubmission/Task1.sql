WITH RankedFlights AS (
    SELECT
        flightkey,       -- Unique identifier for each flight leg
        flightnum,       -- Flight number
        flight_dt,       -- Date of the flight
        orig_arpt,       -- Origin airport code
        dest_arpt,       -- Destination airport code
        flightstatus,    -- Current status of the flight
        lastupdt,        -- Timestamp of the last update for this flight record
        -- Assigning a row number to each flight partitioned by date, number, origin, and destination
        ROW_NUMBER() OVER (
            PARTITION BY flight_dt, flightnum, orig_arpt, dest_arpt  -- group flights by key identifiers, should not be more than 1 flight num at airport in same day
            ORDER BY lastupdt DESC, flightkey ASC                   -- rank most recent updates first; tie-break by flightkey
        ) AS rn
    FROM my_table --Assuming a postgres database has already been defined, change to Delta specific Tablename
)
-- Not selecting Carrier code as example showed, since all DL
-- Step 2: Select only the top-ranked record per flight group
-- Formatting similar to example output
SELECT
    flightkey,       -- Return the unique flight identifier
    flightnum,       -- Flight number
    flight_dt,       -- Flight date
    orig_arpt,       -- Origin airport
    dest_arpt,       -- Destination airport
    flightstatus,    -- Most recent flight status
    lastupdt         -- Most recent update timestamp
FROM RankedFlights
WHERE rn = 1;        -- Keep only the most recent record per flight (deduplicated)
