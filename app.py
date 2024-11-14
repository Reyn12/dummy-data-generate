import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
from io import BytesIO

# Updated constants for dummy data
movie_titles = [
    "Avengers: Endgame",
    "Joker",
    "Frozen II",
    "Toy Story 4",
    "The Lion King",
    "Spider-Man: Far From Home",
    "Aladdin",
    "It Chapter Two",
    "Star Wars: The Rise of Skywalker",
    "Ford v Ferrari",
    "Shazam!",
    "Aquaman",
    "The Matrix Resurrections",
    "Black Panther",
    "Doctor Strange",
    "Wonder Woman",
    "Guardians of the Galaxy",
    "Captain Marvel",
    "Inception",
    "The Dark Knight",
    "Tenet",
    "Parasite",
    "The Witcher",
    "Dune",
    "The Hunger Games",
    "Twilight",
    "Transformers: The Last Knight",
    "John Wick 3",
]

genres = [
    "Action",
    "Drama",
    "Animation",
    "Adventure",
    "Horror",
    "Comedy",
    "Thriller",
    "Sci-Fi",
    "Romance",
    "Fantasy",
]
locations = [
    "Jakarta",
    "Bandung",
    "Surabaya",
    "Medan",
    "Denpasar",
    "Yogyakarta",
    "Makassar",
    "Semarang",
    "Balikpapan",
    "Malang",
]
time_slots = ["12:00", "14:00", "15:30", "17:00", "18:30", "20:00", "21:30"]
ticket_prices = [50000, 60000, 75000, 100000, 120000, 150000, 200000]
payment_methods = ["Cash", "Credit Card", "E-Wallet", "Debit Card"]
seat_types = ["Regular", "Premium", "VIP"]


# Function to generate the dataset
def generate_data(num_records):
    data = []
    start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")

    for _ in range(num_records):
        date = start_date + timedelta(
            days=random.randint(0, 364)
        )  # Random date in 2024
        movie_title = random.choice(movie_titles)
        genre = random.choice(genres)
        location = random.choice(locations)
        time_slot = random.choice(time_slots)
        ticket_price = random.choice(ticket_prices)
        tickets_sold = random.randint(1, 10)  # Number of tickets sold per transaction
        total_revenue = ticket_price * tickets_sold
        payment_method = random.choice(payment_methods)
        seat_type = random.choice(seat_types)

        data.append(
            {
                "Date": date.strftime("%Y-%m-%d"),
                "Movie_Title": movie_title,
                "Genre": genre,
                "Location": location,
                "Time_Slot": time_slot,
                "Ticket_Price": ticket_price,
                "Tickets_Sold": tickets_sold,
                "Total_Revenue": total_revenue,
                "Payment_Method": payment_method,
                "Seat_Type": seat_type,
            }
        )

    # Create a DataFrame
    df = pd.DataFrame(data)
    return df


# Function to convert the dataframe to a downloadable Excel file
def to_excel(df):
    # Create a BytesIO buffer
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sales Data")
    # Get the value of the buffer
    output.seek(0)
    return output


# Streamlit UI
st.title("Dummy Cinema Ticket Sales Dashboard")
st.write("Program Buat Dumy Dataset Tiket Bioskop - Dinamis")

# Input for the number of records
num_records = st.number_input(
    "Input jumlah data yang mau dibuat:",
    min_value=1,
    max_value=10000,  # Adjust the max number as needed
    value=2000,  # Default value
    step=500,  # Step size
)

# Generate data button
if st.button("Generate Data"):
    df = generate_data(num_records)

    # Show the entire DataFrame
    st.write(f"### Data Generated ({num_records} records)")
    st.dataframe(df)  # Display the entire data frame

    # Provide the download button for Excel file
    st.write("### Download the generated dataset")
    excel_file = to_excel(df)
    st.download_button(
        label="Download Data as Excel",
        data=excel_file,
        file_name=f"dummy_cinema_ticket_sales_{num_records}_records.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
