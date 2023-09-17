# Imports
from utils.get_audio_file import get_audio_file
from utils.get_transcription import get_transcription
from utils.get_quiz_array import get_quiz_array
import streamlit as st

def next():
    if st.session_state.index < len(st.session_state.questions)-1:
        st.session_state.index += 1
        print(st.session_state.index)

def main():

    st.set_page_config(page_title="Lumina", page_icon="🎓")

    st.header("Lumina 🎓")
    st.markdown("Turn educational video lectures into engaging MCQ based quizzes and automatic assessment. Learning has never been this fun!")
    st.divider()

    # st.session_state.quiz_started = False

    # if st.session_state.quiz_started == False:
    #     url_container = st.empty()
    #     url_content_container = url_container.container()
    #     url = url_content_container.text_input('URL of Lecture Video', 'https://www.youtube.com/watch?v=rs9AFEebHsk')
    #     generate_button = url_content_container.button("Generate Quiz", type="primary")

    # if generate_button:
        # st.session_state.quiz_started = True
        # url_container.empty()

        # url = "https://www.youtube.com/watch?v=rs9AFEebHsk"
        # get_audio_file(url)

        # text = get_transcription()

        # quiz_array = get_quiz_array(text)

    quiz_array = """[[1, "What carries information from the body to the brain?", "Afferent nerves", "Efferent nerves", "Axons", "Dendrites", 1], 
    [2, "What part of the nervous system controls voluntary movements?", "Autonomic system", "Somatic system", "Sympathetic system", "Parasympathetic system", 2], 
    [3, "What part of the peripheral nervous system is responsible for arousal?", "Somatic system", "Autonomic system", "Sympathetic system", "Parasympathetic system", 3], 
    [4, "Which cells in the nervous system provides support and nutrition?", "Glial cells", "Neurons", "Myelin", "Axons", 1], 
    [5, "What happens when a neuron reaches threshold of excitation?", "It fires", "It stays at resting potential", "It dies", "It slows down", 1], 
    [6, "What do the terminal buttons of a neuron do?", "Release neurotransmitters", "Receive neurotransmitters", "Insulate the neuron", "Speed up transmission", 1], 
    [7, "What is the space between two neurons called?", "Terminal button", "Synaptic gap", "Receptor site", "Dendrite", 2], 
    [8, "What are the dendrites\ncovered in?", "Glial cells", "Myelin", "Receptor sites", "Neurotransmitters", 3], 
    [9, "What is the function of myelin in a neuron?", "Increase speed of information", "Release neurotransmitters", "Receive neurotransmitters", "Convert electrical impulse into a chemical signal", 1], 
    [10, "Which part of a neuron converts electrical impulses into chemical signals?", "Cell body", "Axon", "Terminal buttons", "Dendrites", 3]]"""

    # Replace any escape sequences
    quiz_array = quiz_array.replace("\n", "")
    quiz_array = quiz_array.replace("\t", "")
    quiz_array = quiz_array.replace("\r", "")
    quiz_array = quiz_array.replace("\b", "")
    quiz_array = quiz_array.replace("\f", "")
    quiz_array = quiz_array.replace("\\", "")
    quiz_array = quiz_array.replace("\'", "")

    # Convert the string to a list
    quiz_list = eval(quiz_array)

    if "index" not in st.session_state:
        st.session_state.index = 0    
        st.session_state.questions = [item[1] for item in quiz_list]    
        st.session_state.options = [[item[2], item[3], item[4], item[5]] for item in quiz_list]

    index = st.session_state.index
    length = len(quiz_list)

    st.markdown(''' ## Quiz ''')

    question = st.session_state.questions[index]
    options = st.session_state.options[index]

    # answer = quiz_list[index][6]

    temp_string = f"#### Question {index+1} out of {length}:"
    st.markdown(temp_string)
    st.markdown(question)

    user_answer = st.radio(
        question,
        options,
        label_visibility="collapsed",
        key=index,
        )

    # Need to log the answers and then match and calculate the correct and incorrect answers

    next_button = st.button("Next Question", type="primary", key=f'button{index}', on_click=next)


if __name__ == '__main__':
    main()