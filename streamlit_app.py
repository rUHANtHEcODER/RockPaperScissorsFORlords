import streamlit as st
import random

# Initialize session state variables
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'round_count' not in st.session_state:
    st.session_state.round_count = 1
if 'message' not in st.session_state:
    st.session_state.message = "Welcome to Rock, Paper, Scissors! Click a button to start playing."

choices = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win!!!"
    else:
        return "Computer wins."

def play_round(user_choice):
    computer_choice = random.choice(list(choices.keys()))
    result = determine_winner(user_choice, computer_choice)

    if result == "You win!!!":
        st.session_state.user_score += 1
    elif result == "Computer wins.":
        st.session_state.computer_score += 1

    st.session_state.message = f"You chose {choices[user_choice]}. Computer chose {choices[computer_choice]}. {result}"

    if st.session_state.round_count >= 10:
        if st.session_state.user_score > st.session_state.computer_score:
            st.session_state.message += "\nYou won the match!"
        elif st.session_state.user_score < st.session_state.computer_score:
            st.session_state.message += "\nComputer won the match!"
        else:
            st.session_state.message += "\nThe match is a tie!"

        # Show final message and reset
        st.write(st.session_state.message)

        # Reset scores and round count
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        st.session_state.round_count = 1
        st.session_state.message = "Welcome to Rock, Paper, Scissors! Click a button to start playing."
    else:
        st.session_state.round_count += 1

# Streamlit app layout
st.title("Rock, Paper, Scissors")

st.write(f"Round: {st.session_state.round_count}/10")
st.write(f"Score: You {st.session_state.user_score} - {st.session_state.computer_score} Computer")
st.write(st.session_state.message)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Rock'):
        play_round('r')
with col2:
    if st.button('Paper'):
        play_round('p')
with col3:
    if st.button('Scissors'):
        play_round('s')

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True
)
