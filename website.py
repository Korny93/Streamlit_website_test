import streamlit as st

def main():
    st.title("💖 দেখি কতটা চিনিস আমাকে? 💖")
    st.write("Let's see how many you can answer correctly 😊")
    
    questions = [
        {"question": "Where did we first meet? 🏫", "options": ["Gym 💪", "Colony 🌳", "Mall 🛍️", "Friend's Party 🎉"], "answer": "Gym 💪"},
        {"question": "What is my favorite food? 🍽️", "options": ["Rice 🍚", "Pokora 🍗", "মুড়ি", "তুই 😘"], "answer": "মুড়ি"},
        {"question": "Which movie is my all time favourite? 🎬", "options": ["Baishe Shrabon 🎥", "Seven 7️⃣", "Fast and Furious 3 🏎️ ", "Harry potter series 🧙"], "answer": "Baishe Shrabon 🎥"},
        {"question": "What is my favorite color? 🎨", "options": ["Blue 🔵", "Red 🔴", "Green 🟢", "Black ⚫"], "answer": "Red 🔴"},
        {"question": "What is my favourite time of the year? 📆", "options": ["January ❄️", "March 🌸", "December 🀩", "September 🍂"], "answer": "December 🀩"}
    ]
    
    score = 0
    for q in questions:
        user_answer = st.radio(q["question"], q["options"], index=None)
        if user_answer == q["answer"]:
            score += 1
    
    
    if st.button("Submit Answers 💌"):
        st.subheader(f"Your Score: {score}/{len(questions)}")
        if score == len(questions):
            st.success("Wow! You know me so well! You're the best! 💖")
            st.balloons()
        elif score > len(questions)//2:
            st.info("Good job! You know me pretty well! 😊")
            st.snow()
        else:
            st.warning("Hmm... we might need more date nights! 😜")
            st.markdown("""
                        <style>
                        .emoji {
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                            font-size: 200px;
                            z-index: -1;
                        }
                        body {
                            background-color: #f0f0f0;
                        }
                        </style>
                        <div class="emoji">😉</div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
