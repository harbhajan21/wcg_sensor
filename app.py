# Importing packages

import streamlit as st
from PIL import Image

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

## Image Opening
image = Image.open('Unlocked.png')
st.sidebar.header("Wheelchair Guardian")
st.sidebar.header("Gardien en fauteuil roulant")
st.sidebar.image(image, caption='', use_column_width=True)

# Number input example
sim_val = st.number_input('Enter the value for the sensor/Entrez la valeur du capteur :', min_value=12.0, max_value=14.0, step=1e-6,)

if st.checkbox("Value of Sensors/Valeur des capteurs"):
    ## Image Opening
    image = Image.open('sensor_with_wheelchair.png')
    image = image.resize((300, 300))
    st.image(image, caption='', use_column_width=False)
    st.write('The distance between the sensor and the wheel of the wheelchair is/La distance entre le capteur et la roue du fauteuil roulant est :', sim_val)
    simulator_val = sim_val
    
    if simulator_val == 13.0:
        st.success("The condition of the wheel of the wheelchair is good!/L'état de la roue du fauteuil roulant est bon !")
        
    elif simulator_val != 13.0:
        st.error("The condition of the wheel of the wheelchair is not good. There are chances to break or damage the wheel./L'état de la roue du fauteuil roulant n'est pas bon. Il y a des chances de casser ou d'endommager la roue.")
        
    st.subheader("Position and status of Wheelchair/Position et statut du fauteuil roulant")
    
    st.subheader("Position of Wheelchair/Position du fauteuil roulant")
    
    if st.checkbox("Toggle/Basculer"):
        ## Image Opening
        image = Image.open('Toggle2.png')
        image = image.resize((400, 300))
        st.image(image, caption='', use_column_width=True)
        
    if st.checkbox("Tilt/Inclinaison"):
        ## Image Opening
        image = Image.open('Toggle1.png')
        image = image.resize((400, 300))
        st.image(image, caption='', use_column_width=True)
     
    st.subheader("Status of the Wheel of the Wheelchair/Statut de la roue du fauteuil roulant")
       
    if st.checkbox("Broken wheel/Roue cassée"):
        ## Image Opening
        image = Image.open('Broken_wheel.png')
        image = image.resize((400, 300))
        st.image(image, caption='', use_column_width=True)
        
        #frequency = 2500  # Set Frequency To 2500 Hertz
        #duration = 1000  # Set Duration To 1000 ms == 1 second
        #winsound.Beep(frequency, duration)
        
        
    if st.checkbox("Misaligned Wheel/Roue mal alignée"):
        ## Image Opening
        image = Image.open('Misaligned_wheel.png')
        image = image.resize((400, 300))
        st.image(image, caption='', use_column_width=True)

    st.subheader("Locked and Unlocked Wheelchair/Fauteuil roulant verrouillé et déverrouillé")
    
    if st.checkbox("Locked Wheelchair/Fauteuil roulant verrouillé"):
        ## Image Opening
        image = Image.open('Locked.png')
        image = image.resize((400, 300))
        st.image(image, caption='', use_column_width=True)
        
    if st.checkbox("Unlocked Wheelchair/Fauteuil roulant déverrouillé"):
        ## Image Opening
        image = Image.open('Unlocked.png')
        image = image.resize((400, 300))
        st.image(image, caption='', use_column_width=True)

