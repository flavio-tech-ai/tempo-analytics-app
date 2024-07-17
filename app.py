import streamlit as st
import mysql.connector

def fetch_data_from_mysql(db_connection, query):
    # query = "SELECT * FROM your_view_name;"
    cursor = db_connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

def main():

    db_connection = mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

    query = "SELECT ID, Name FROM Tempo.Clients;"
    
    st.title('Display MySQL View Data')
    
    data = fetch_data_from_mysql(db_connection, query)
    
    if data:
        st.write("Data from MySQL View:")
        st.table(data)
    else:
        st.write("No data available.")
    
if __name__ == "__main__":
    main()