# Import python packages
# Written By Raghunath

import streamlit as st

st.title('CRM :blue[Test File] Generation')
st.subheader('Please give input carefully; Check CCM details')

#Input Box
def create_input(header,value, hinttext=''):
    userInput = st.text_input(header, value)
    st.write(hinttext)
    return userInput

gaCode = create_input('GA Code', 'Placeholder', '')
segmentName = create_input('Segment name', 'Placeholder', '')
templateId = create_input('Template Id', 'Placeholder', '')
fileFormat = create_input('File Format', 'Placeholder', '')
sendTime = create_input('Send Time', 'Placeholder', '')

option = st.selectbox(
    'Please select channel',('EM', 'SMS', 'OB', 'DM')
)
channel = st.write('You selected option:', option)

option = st.selectbox(
    'Please select file format',('Marketing v3', 'Regs-Reneawal')
)
fileFormat = st.write('You selected:', option)

#-------------------------------------------
#Test table creation
def create_test_table():
    # Initialize connection.
    #conn = st.experimental_connection('snowpark')
    # Perform query.
    #df = conn.query(
    #       'SELECT * from T4083_CRM_CONTRACT_COPY'
    #       , ttl=600
    #   )
    # Print results.
    #for row in df.itertuples():
    #    st.write(f"{row.NAME} has a :{row.PET}:")
    st.success('This is a success message!', icon="✅")

#-------------------------------------------
# Main calculation
def click_button():
        create_test_table()
        

st.button('Generate Test File', on_click=click_button)
