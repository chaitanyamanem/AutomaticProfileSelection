import streamlit as st
import pandas as pd

# DataFrame for job applications
@st.cache_data
def applications_data():
    df = pd.read_csv(r"data/applications.csv")    
    return df

job_applications_df = applications_data()

# Streamlit App
def display_application_details_page():
    st.subheader("Application Details")

    # Dropdown for selecting Application ID
    selected_application_id = st.selectbox("Select Application ID", [None] + job_applications_df['application_id'].tolist())

    # Display details only when an Application ID is selected
    if selected_application_id:
        selected_row = job_applications_df[job_applications_df['application_id'] == selected_application_id].iloc[0]

        # Display details
        st.markdown(f"#### Candidate Name: {selected_row['applicant_name']}")
        st.markdown(f"#### Mail ID: {selected_row['email_id']}")
        st.markdown(f"#### Candidate Score: {round(selected_row['score'],2)}")
        st.markdown(f"#### Short Summary:\n{selected_row['short_summary']}")
        st.markdown(f"#### Summary:\n{selected_row['consise_summary']}")
    else:
        st.info("Select an Application ID to view details.")

# Run the Streamlit app
if __name__ == "__main__":
    display_application_details_page()
