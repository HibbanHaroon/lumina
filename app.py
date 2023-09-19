# Imports
from utils.get_audio_file import get_audio_file
from utils.get_transcription import get_transcription
from utils.get_quiz_array import get_quiz_array
import streamlit as st

def get_information():
    url_container = st.empty()
    url_content_container = url_container.container()
    url = url_content_container.text_input('URL of Lecture Video', 'https://www.youtube.com/watch?v=rs9AFEebHsk')
    generate_button = url_content_container.button("Generate Quiz", type="primary")
    if generate_button:
        st.session_state.quiz_started = True
        url_container.empty()

        with st.spinner('Converting Video File to Audio...'):
            get_audio_file(url)

        with st.spinner('Converting Audio File to Text...'):
            text = get_transcription()

        with st.spinner('Generating Quiz...'):
            quiz_array = get_quiz_array(text)
            st.session_state.quiz_array = quiz_array

        # quiz_array = """[[1, "What are the two pathways that carry information in the nervous system?", "Afferent and Efferent", "Central and Peripheral", "Autonomic and Somatic", "Sympathetic and Parasympathetic", "Afferent and Efferent"],
        # [2, "What does the Central Nervous System consist of?", "Brain and Spinal Cord", "Heart and Lungs", "Eyes and Ears", "Arms and Legs", "Brain and Spinal Cord"],
        # [3, "Which system controls our voluntary movements?", "Autonomic System", "Somatic System", "Sympathetic System", "Central System", "Somatic System"],
        # [4, "What is the arousing system in our body?", "Parasympathetic System", "Peripheral System", "Sympathetic System", "Central System", "Sympathetic System"],
        # [5, "What type of cells in our nervous system provides support and nutrition?", "Neurons", "Mitochondria", "Glial Cells", "Ribosomes", "Glial Cells"],
        # [6, "What part of neuron carries the information away from the cell body?", "Dendrites", "Axon", "Myelin", "Terminal Buttons", "Axon"],
        # [7, "What is the space between two neurons called?", "Axon", "Synapse", "Dendrite", "Myelin", "Synapse"],
        # [8, "What does an action potential operate by?", "All or None Principle", "First Come First Serve Principle", "Last Come First Serve Principle", "None of the Above", "All or None Principle"],
        # [9, "What happens in the reuptake process ?", "Transmission of neurotransmitter to another neuron", "Reabsorption of neurotransmitter back into the vesicle", "Neuron firing", "Creation of a new neurotransmitter", "Reabsorption of neurotransmitter back into the vesicle"],
        # [10, "Which of the following aids in speeding up the transmission in neurons?", "Dendrites", "Axon", "Synapse", "Myelin", "Myelin"]]"""

        # st.session_state.quiz_array = quiz_array
        show_quiz()

def show_quiz():
    quiz_array = st.session_state.quiz_array
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

    # Initializing session states
    if "index" not in st.session_state:
        st.session_state.index = 0    
        st.session_state.questions = [item[1] for item in quiz_list]
        st.session_state.options = [[item[2], item[3], item[4], item[5]] for item in quiz_list]
        st.session_state.answers = [item[6] for item in quiz_list]
        st.session_state.latest_answer = ""
        st.session_state.user_answers = []
        st.session_state.no_of_correct_answers = 0
        st.session_state.no_of_incorrect_answers = 0
        st.session_state.quiz_submitted = False

    index = st.session_state.index
    length = len(quiz_list)
    question = st.session_state.questions[index]
    options = st.session_state.options[index]
    answer = st.session_state.answers[index]

    st.markdown("## Quiz")

    if st.session_state.quiz_submitted == True:
        st.markdown(f"### You scored: {st.session_state.no_of_correct_answers}/{len(st.session_state.questions)}")
        user_answer = st.session_state.user_answers[index]
        if answer == user_answer:
            st.success(f"The correct answer is {answer}.", icon="✔️")
        else:
            st.error(f"{user_answer} is incorrect! The correct answer is {answer}.", icon="❌")


    temp_string = f"#### Question {index+1} out of {length}:"
    st.markdown(temp_string)
    st.markdown(question)

    if st.session_state.quiz_submitted == True:
        user_answer = st.session_state.user_answers[index]
        st.radio(
            question,
            options,
            label_visibility = "collapsed",
            key = index,
            index = options.index(user_answer)
        )
    else:
        user_answer = st.radio(
            question,
            options,
            label_visibility = "collapsed",
            key = index,
        )

    st.session_state.latest_answer = user_answer

    button = st.empty()

    if st.session_state.quiz_submitted == False:
        if st.session_state.index < len(st.session_state.questions)-1:
            next_button = st.button("Next Question", type="primary", on_click=next)
        elif st.session_state.index == len(st.session_state.questions)-1:
            button.button("Submit", type="primary", on_click=next)
    else:
        if st.session_state.index < len(st.session_state.questions)-1:
            next_button = st.button("Next Question", type="primary", on_click=next)
        elif st.session_state.index == len(st.session_state.questions)-1:
            button.button("Return to Home", type="primary", on_click=return_to_home)

def next():
    if st.session_state.index < len(st.session_state.questions)-1:
        st.session_state.index += 1
        # Appending answers that the user inputs
        st.session_state.user_answers.append(st.session_state.latest_answer)
    elif st.session_state.index == len(st.session_state.questions)-1:
        # Appending the last answer too that the user inputs
        st.session_state.user_answers.append(st.session_state.latest_answer)
        compare()
        
def compare():
    answers = st.session_state.answers
    user_answers = st.session_state.user_answers

    # Check if the lists have the same length
    if len(answers) != len(user_answers):
        print("The lists have different lengths, so they are not equal.")
    else:
        # Use a loop to compare the values at each index
        for i in range(len(answers)):
            if answers[i] == user_answers[i]:
                st.session_state.no_of_correct_answers += 1
            else:
                st.session_state.no_of_incorrect_answers += 1
    
    st.session_state.quiz_submitted = True
    st.session_state.index = 0

def return_to_home():
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]

def main():

    st.set_page_config(page_title="Lumina", page_icon="🎓")

    st.header("Lumina 🎓")
    st.markdown("Turn educational video lectures into engaging MCQ based quizzes and automatic assessment. Learning has never been this fun!")
    st.divider()

    # Initializing session states
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.quiz_array = ""

    if st.session_state.quiz_started == False:
        get_information()
    else: 
        show_quiz()


if __name__ == '__main__':
    main()