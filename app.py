
import streamlit as st

import time



# Dummy function to simulate device control (replace with actual IoT integration later)

def control_device(device_name, command, value):

    st.write(f"{device_name}: {command} {value} (simulated)")

    time.sleep(1)  # Simulate device response time

    st.success(f"{device_name} adjusted successfully!")



# Appliance control functions

def control_bed(level):

    # Simulate device control (replace with actual IoT integration later)

    st.write(f"Bed: Level set to {level} degrees")

    # Consider adding logic to handle invalid levels if needed

    st.success("Bed adjusted successfully!")



def control_light(brightness):

    control_device("Light", "Brightness set to", brightness)



def control_window(position):

    control_device("Window", "Position set to", position)



def control_temperature(temperature):

    control_device("AC", "Temperature set to", temperature)



# Image paths (update with correct paths)

bed_images = {0: "bed_0.jpeg", 15: "bed_1.jpeg", 30: "bed_2.jpeg", 45: "bed_3.jpeg"}

light_images = {0: "bright_1.jpeg", 50: "bright_2.jpeg", 100: "bright_3.jpeg"}

window_images = {0: "window_1.jpeg", 50: "window_2.jpeg", 100: "window_3.jpeg"}

temperature_images = {0: "temp_1.jpeg", 50: "temp_2.jpeg", 100: "temp_3.jpeg"}



# Patient information (update with actual data)

patient_name = "Khushi Mahawar"

vital_signs = {

    "Heart Rate": 72,

    "Blood Pressure": "120/80",

    "Oxygen Saturation": 98,

    "Temperature": 37.2,

}



# Main layout

st.title("Patient Room Control Panel")



# Columns for Medical LLM and Gemini AI outputs

col1, col2 = st.columns(2)



with col1:

    st.subheader("Medical LLM Output")

    medical_output = st.text_area("Medical LLM Output", height=100)  # Replace with actual output



with col2:

    st.subheader("Gemini AI Output")

    gemini_output = st.text_area("Gemini AI Output", height=100)  # Replace with actual output



# Sidebar for patient information

st.sidebar.header("Patient Information")

st.sidebar.text(f"Name: {patient_name}")

for sign, value in vital_signs.items():

    st.sidebar.metric(sign, value)



# Bed control

col3, col4 = st.columns(2)



with col3:

    bed_level_options = [0, 15, 30, 45]  # Available bed levels in degrees

    selected_level = st.slider("Bed Level", min_value=bed_level_options[0],

                               max_value=bed_level_options[-1],

                               step=bed_level_options[1] - bed_level_options[0],

                               value=bed_level_options[0])

    st.image(bed_images[selected_level], width=200)

    if st.button("Adjust Bed"):

        control_bed(selected_level)



# Light control

with col4:

    light_brightness_options = [0, 50, 100]  # Assign numerical values to options

    selected_brightness = st.slider("Light Brightness", min_value=light_brightness_options[0],

                                   max_value=light_brightness_options[-1],

                                   step=light_brightness_options[1] - light_brightness_options[0],

                                   value=light_brightness_options[1])

    st.image(light_images[selected_brightness], width=200)

    if st.button("Adjust Light"):

        control_light(selected_brightness)



# Window position, temperature level, and new features

col5, col6 = st.columns(2)



with col5:

    window_position_options = [0, 50, 100]  # Assign numerical values to options



    selected_position = st.slider("Window Position", min_value=window_position_options[0],



                             max_value=window_position_options[-1],



                             step=window_position_options[1] - window_position_options[0],



                             value=window_position_options[1])



    st.image(window_images[selected_position], width=200)



    if st.button("Adjust Window"):



        control_window(selected_position)



with col6:

    temperature_level_options = [0, 50, 100]  # Assign numerical values to options

    selected_temperature = st.slider("Temperature Level", min_value=temperature_level_options[0],

                                    max_value=temperature_level_options[-1],

                                    step=temperature_level_options[1] - temperature_level_options[0],

                                    value=temperature_level_options[1])

    st.image(temperature_images[selected_temperature], width=200)

    

    if st.button("Set Temperature"):

        control_temperature(selected_temperature)



# col7, col8 = st.columns(2) 

# with col7:

#     # Oxygen Level

#     st.subheader("Oxygen Level")



#     # Display an appropriate image for oxygen levels (if available)

#     if "oxygen_image.jpeg" in os.listdir():  # Check if image exists

#         st.image("oxygen_image.jpeg", width=200)



#     # Define custom labels for oxygen levels

#     oxygen_labels = {0: 'Low', 50: 'Normal', 100: 'High'}



#     oxygen_values = [0, 50, 100]  # Update values for your oxygen sensor



#     selected_oxygen = st.slider("Oxygen Level", min_value=oxygen_values[0],

#                                 max_value=oxygen_values[-1],

#                                 step=oxygen_values[1] - oxygen_values[0],

#                                 value=oxygen_values[1])

#     st.text(f"Selected Oxygen Level: {oxygen_labels[selected_oxygen]}")



#     # Add a button or other control to trigger actions based on oxygen level (if needed)



# with col8:

#     # Thermostat Level

#     st.subheader("Thermostat Level")



#     # Display an appropriate image for thermostat (if available)

#     if "thermostat_image.jpeg" in os.listdir():  # Check if image exists

#         st.image("thermostat_image.jpeg", width=200)



#     # Define custom labels for thermostat levels (if applicable)

#     thermostat_labels = {  # Replace with your actual labels

#         20: "Cool",

#         25: "Comfortable",

#         30: "Warm"

#     }



#     thermostat_values = [20, 25, 30]  # Update values for your thermostat



#     selected_thermostat = st.slider("Thermostat Level", min_value=thermostat_values[0],

#                                     max_value=thermostat_values[-1],

#                                     step=thermostat_values[1] - thermostat_values[0],

#                                     value=thermostat_values[1])

#     st.text(f"Selected Thermostat Level: {thermostat_labels[selected_thermostat]}")