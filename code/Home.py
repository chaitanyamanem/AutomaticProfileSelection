import streamlit as st
import pandas as pd

# DataFrame for job applications
@st.cache_data
def applications_data():
    df = pd.read_csv(r"data/applications.csv")
    df = df.loc[:,["application_id","position_applid","applicant_name","email_id","short_summary","score"]]
    return df
# data = {
#     'Applicant Name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
#     'Position Applied': ['Software Engineer', 'Data Scientist', 'Marketing Specialist'],
#     'Experience (years)': [5, 3, 7],
#     'Status': ['Under Review', 'Rejected', 'Shortlisted']
# }



# Company Logo URL
company_logo_url = 'images/logo.png'  # Replace with the actual URL of the company logo

# Streamlit App
def main():
    st.set_page_config(
        page_title="Swaayatt Robots Recruitment",
        page_icon=":briefcase:",
        layout="wide"
    )

    # Company Logo and Title
    st.image(company_logo_url, width=200)
    st.title("Swaayatt Robots Internal Recruitment Portal")

    # Description
    st.markdown(
        "Welcome to the internal recruitment portal of Swaayatt Robots. This page provides an overview of job applications."
    )

    # Data

    job_applications_df = applications_data()

    # Dropdown for filtering by Position Applied
    selected_position = st.selectbox("Filter by Position Applied", ['All'] + job_applications_df['position_applid'].unique().tolist())

    # Filter DataFrame based on selected Position Applied
    if selected_position != 'All':
        filtered_df = job_applications_df[job_applications_df['position_applid'] == selected_position]
        st.subheader(f"Job Applications for {selected_position}")
        st.dataframe(filtered_df, hide_index=True)
    else:
        st.subheader("All Job Applications")
        st.dataframe(job_applications_df, hide_index=True)

    # Styling
    st.markdown(
        """
        <style>
            div[data-testid="stSidebar"][aria-expanded="true"] {
                width: 300px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Run the Streamlit app
if __name__ == "__main__":
    main()
