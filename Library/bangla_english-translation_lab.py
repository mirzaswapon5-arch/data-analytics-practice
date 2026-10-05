import streamlit as st
import random

# ============================================================
# বাংলা ↔ ENGLISH TRANSLATION LEARNING APP
# Streamlit app — no external API required
# ============================================================

st.set_page_config(
    page_title="Bangla ↔ English Translation Lab",
    page_icon="📘",
    layout="wide"
)

# ----------------------------
# CSS
# ----------------------------
st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 4px;
}
.subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 20px;
}
.card {
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #ddd;
    margin-bottom: 14px;
}
.answer-box {
    padding: 14px;
    border-radius: 10px;
    background: #f3f7ff;
    border: 1px solid #d8e5ff;
}
.tip-box {
    padding: 14px;
    border-radius: 10px;
    background: #fff9e8;
    border: 1px solid #f1df9a;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA
# ============================================================

LESSONS = {
    "Be Verb (am/is/are)": {
        "rule": "Be verb সাধারণত am, is, are দিয়ে পরিচয়, অবস্থা, বয়স, পেশা ইত্যাদি প্রকাশ করে।",
        "patterns": [
            "I am + noun/adjective.",
            "He/She/It is + noun/adjective.",
            "You/We/They are + noun/adjective.",
            "বাংলা: আমি/সে/তারা ... → context অনুযায়ী am/is/are ব্যবহার।"
        ],
        "examples": [
            ("আমি একজন ছাত্র।", "I am a student."),
            ("সে খুব ব্যস্ত।", "He is very busy."),
            ("তারা খুশি।", "They are happy."),
            ("তুমি কি প্রস্তুত?", "Are you ready?"),
            ("আমি অলস নই।", "I am not lazy."),
        ]
    },

    "Have Verb (have/has)": {
        "rule": "Have/has সাধারণত মালিকানা, অধিকার বা কোনো কিছু থাকা বোঝাতে ব্যবহৃত হয়।",
        "patterns": [
            "I/You/We/They have + object.",
            "He/She/It has + object.",
            "Negative: do not have / does not have.",
            "Question: Do/Does + subject + have ...?"
        ],
        "examples": [
            ("আমার একটি বই আছে।", "I have a book."),
            ("তার একটি গাড়ি আছে।", "He has a car."),
            ("তাদের সময় নেই।", "They do not have time."),
            ("তোমার কি একটি কলম আছে?", "Do you have a pen?"),
            ("তার কি একটি ভাই আছে?", "Does she have a brother?"),
        ]
    },

    "Main Verb": {
        "rule": "Main verb হলো বাক্যের প্রধান কাজের verb—যেমন eat, go, read, write, play, work।",
        "patterns": [
            "Present: Subject + V1/V1+s/es.",
            "Past: Subject + V2.",
            "Future: Subject + will + V1.",
            "Negative/Question-এ do/does/did ব্যবহার হতে পারে।"
        ],
        "examples": [
            ("আমি প্রতিদিন ইংরেজি পড়ি।", "I read English every day."),
            ("সে স্কুলে যায়।", "He goes to school."),
            ("তারা ক্রিকেট খেলেছিল।", "They played cricket."),
            ("তুমি কি বইটি পড়ো?", "Do you read the book?"),
            ("আমি গতকাল বাজারে যাইনি।", "I did not go to the market yesterday."),
        ]
    },

    "There (There is/are)": {
        "rule": "কোনো জায়গায় কিছু আছে/আছে না বোঝাতে There is / There are ব্যবহৃত হয়।",
        "patterns": [
            "There is + singular noun.",
            "There are + plural noun.",
            "There was/were → past.",
            "Question: Is/Are there ...?"
        ],
        "examples": [
            ("টেবিলের উপর একটি বই আছে।", "There is a book on the table."),
            ("ঘরে তিনটি চেয়ার আছে।", "There are three chairs in the room."),
            ("বাগানে কোনো ফুল নেই।", "There are no flowers in the garden."),
            ("এখানে কি কোনো সমস্যা আছে?", "Is there any problem here?"),
            ("গ্রামে একটি নদী ছিল।", "There was a river in the village."),
        ]
    },

    "Mixed Translation": {
        "rule": "Be verb, Have verb, Main verb এবং There—সব একসাথে অনুশীলন করো।",
        "patterns": [
            "প্রথমে subject শনাক্ত করো।",
            "তারপর বাক্যটি পরিচয়/অবস্থা, মালিকানা, কাজ, নাকি existence বোঝাচ্ছে তা নির্ণয় করো।",
            "Tense ও singular/plural দেখে verb নির্বাচন করো।"
        ],
        "examples": [
            ("আমি একজন শিক্ষক।", "I am a teacher."),
            ("তার একটি লাল গাড়ি আছে।", "He has a red car."),
            ("রহিম প্রতিদিন স্কুলে যায়।", "Rahim goes to school every day."),
            ("ক্লাসে অনেক ছাত্র আছে।", "There are many students in the class."),
            ("তারা গতকাল ব্যস্ত ছিল।", "They were busy yesterday."),
        ]
    }
}


# ============================================================
# EXTRA PRACTICE DATA
# ============================================================

QUESTIONS = {
    "Be Verb (am/is/are)": [
        ("আমি একজন ডাক্তার।", "I am a doctor."),
        ("সে একজন ভালো ছেলে।", "He is a good boy."),
        ("তারা খুব ব্যস্ত।", "They are very busy."),
        ("তুমি কি প্রস্তুত?", "Are you ready?"),
        ("আমরা দুঃখিত নই।", "We are not sad."),
        ("সে কি অসুস্থ?", "Is she sick?"),
        ("আমি ক্লান্ত।", "I am tired."),
        ("তোমরা কি ছাত্র?", "Are you students?"),
    ],
    "Have Verb (have/has)": [
        ("আমার একটি মোবাইল আছে।", "I have a mobile phone."),
        ("তার একটি বোন আছে।", "She has a sister."),
        ("তাদের কোনো টাকা নেই।", "They do not have any money."),
        ("তোমার কি একটি ছাতা আছে?", "Do you have an umbrella?"),
        ("তার কি একটি গাড়ি আছে?", "Does he have a car?"),
        ("আমাদের একটি বাড়ি আছে।", "We have a house."),
        ("রহিমের একটি সাইকেল আছে।", "Rahim has a bicycle."),
    ],
    "Main Verb": [
        ("আমি ভাত খাই।", "I eat rice."),
        ("সে প্রতিদিন স্কুলে যায়।", "He goes to school every day."),
        ("তারা ফুটবল খেলে।", "They play football."),
        ("আমি গতকাল বইটি পড়েছিলাম।", "I read the book yesterday."),
        ("সে ইংরেজি শিখছে।", "She is learning English."),
        ("তুমি কি আমাকে চেনো?", "Do you know me?"),
        ("আমি গতকাল বাজারে যাইনি।", "I did not go to the market yesterday."),
    ],
    "There (There is/are)": [
        ("টেবিলের উপর একটি কলম আছে।", "There is a pen on the table."),
        ("ঘরে দুটি জানালা আছে।", "There are two windows in the room."),
        ("বাগানে অনেক ফুল আছে।", "There are many flowers in the garden."),
        ("এখানে কোনো চেয়ার নেই।", "There is no chair here."),
        ("এখানে কি কোনো হাসপাতাল আছে?", "Is there a hospital here?"),
        ("ক্লাসে অনেক ছাত্র ছিল।", "There were many students in the class."),
        ("গ্রামে একটি বড় পুকুর ছিল।", "There was a big pond in the village."),
    ],
    "Mixed Translation": [
        ("আমি একজন ছাত্র এবং আমার একটি বই আছে।", "I am a student and I have a book."),
        ("সে প্রতিদিন স্কুলে যায়।", "He goes to school every day."),
        ("ঘরে একটি টেবিল আছে।", "There is a table in the room."),
        ("তারা খুব খুশি।", "They are very happy."),
        ("আমাদের একটি সমস্যা আছে।", "We have a problem."),
        ("বাগানে অনেক গাছ আছে।", "There are many trees in the garden."),
        ("আমি গতকাল ব্যস্ত ছিলাম।", "I was busy yesterday."),
    ]
}


# ============================================================
# HELPERS
# ============================================================

def normalize(text):
    text = text.strip().lower()
    text = text.replace(".", "").replace("?", "").replace("!", "")
    text = " ".join(text.split())
    return text


def is_correct(user_answer, correct_answer):
    return normalize(user_answer) == normalize(correct_answer)


def get_question(direction, category):
    pair = random.choice(QUESTIONS[category])
    if direction == "Bangla → English":
        return pair[0], pair[1]
    return pair[1], pair[0]


def show_explanation(category, source, answer):
    lesson = LESSONS[category]

    st.markdown("### 🔎 কেন এই উত্তর?")
    st.info(lesson["rule"])

    if category == "Be Verb (am/is/are)":
        st.write("**Verb নির্বাচন:** subject অনুযায়ী am / is / are।")
    elif category == "Have Verb (have/has)":
        st.write("**Verb নির্বাচন:** I/you/we/they → have; he/she/it → has।")
    elif category == "Main Verb":
        st.write("**Verb নির্বাচন:** subject ও tense দেখে main verb-এর form নির্বাচন করতে হয়।")
    elif category == "There (There is/are)":
        st.write("**Verb নির্বাচন:** একবচন → There is; বহুবচন → There are।")
    else:
        st.write("প্রথমে বাক্যের ধরন শনাক্ত করে তারপর উপযুক্ত verb নির্বাচন করতে হবে।")

    st.markdown(f"**সঠিক উত্তর:** `{answer}`")


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "score": 0,
    "total": 0,
    "question": None,
    "answer": None,
    "source": None,
    "feedback": None,
    "last_category": "Mixed Translation",
    "last_direction": "Bangla → English",
    "streak": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📘 বাংলা ↔ English Translation Lab</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Be Verb • Have Verb • Main Verb • There • Mixed Practice</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.header("⚙️ Practice Settings")

    category = st.selectbox(
        "Verb / Topic নির্বাচন করুন",
        list(LESSONS.keys())
    )

    direction = st.radio(
        "অনুবাদের দিক",
        ["Bangla → English", "English → Bangla"]
    )

    st.divider()

    st.metric("Score", st.session_state.score)
    st.metric("Questions", st.session_state.total)
    st.metric("Streak", st.session_state.streak)

    st.divider()

    if st.button("🔄 Reset Score", use_container_width=True):
        st.session_state.score = 0
        st.session_state.total = 0
        st.session_state.streak = 0
        st.session_state.question = None
        st.session_state.feedback = None
        st.rerun()


# ============================================================
# TOP TABS
# ============================================================

tab_learn, tab_practice, tab_reference = st.tabs(
    ["📖 শেখা", "🎯 অনুশীলন", "📚 Grammar Reference"]
)


# ============================================================
# LEARN TAB
# ============================================================

with tab_learn:

    st.header(f"📖 {category}")

    lesson = LESSONS[category]

    st.markdown(
        f'<div class="card"><b>মূল নিয়ম:</b><br>{lesson["rule"]}</div>',
        unsafe_allow_html=True
    )

    st.subheader("🧩 Sentence Patterns")

    for pattern in lesson["patterns"]:
        st.markdown(f"- {pattern}")

    st.subheader("✍️ উদাহরণ")

    for bn, en in lesson["examples"]:
        c1, c2 = st.columns([1, 1])

        with c1:
            st.write(f"🇧🇩 **{bn}**")

        with c2:
            st.write(f"🇬🇧 **{en}**")

    st.divider()

    st.subheader("💡 Translation Strategy")

    st.markdown("""
1. **Subject** খুঁজে বের করো।
2. বাক্যটি **Be / Have / Main Verb / There** কোন ধরনের তা বোঝো।
3. **Tense** শনাক্ত করো।
4. Singular/Plural অনুযায়ী verb বেছে নাও।
5. শেষে বাক্যের word order মিলিয়ে নাও।
""")


# ============================================================
# PRACTICE TAB
# ============================================================

with tab_practice:

    st.header("🎯 Translation Practice")

    st.write(
        f"**Mode:** {category}  |  **Direction:** {direction}"
    )

    # New question
    if st.button("🆕 নতুন প্রশ্ন", type="primary", use_container_width=True):

        source, answer = get_question(direction, category)

        st.session_state.question = source
        st.session_state.answer = answer
        st.session_state.source = source
        st.session_state.feedback = None
        st.session_state.last_category = category
        st.session_state.last_direction = direction

    if st.session_state.question is None:

        st.info("শুরু করতে **🆕 নতুন প্রশ্ন** চাপুন।")

    else:

        st.markdown("### প্রশ্ন")

        st.markdown(
            f'<div class="card"><h3>{st.session_state.question}</h3></div>',
            unsafe_allow_html=True
        )

        user_answer = st.text_area(
            "তোমার উত্তর লিখো:",
            height=130,
            key=f"answer_box_{st.session_state.total}_{st.session_state.question}"
        )

        c1, c2 = st.columns(2)

        with c1:
            check = st.button(
                "✅ উত্তর যাচাই",
                use_container_width=True
            )

        with c2:
            reveal = st.button(
                "👁️ উত্তর দেখাও",
                use_container_width=True
            )

        if check:

            if not user_answer.strip():

                st.warning("আগে তোমার উত্তর লিখো।")

            else:

                st.session_state.total += 1

                if is_correct(
                    user_answer,
                    st.session_state.answer
                ):

                    st.session_state.score += 1
                    st.session_state.streak += 1

                    st.success("🎉 Correct! খুব ভালো!")

                else:

                    st.session_state.streak = 0

                    st.error("❌ পুরোপুরি মেলেনি।")

                    st.markdown(
                        f'<div class="answer-box"><b>সঠিক উত্তর:</b><br>{st.session_state.answer}</div>',
                        unsafe_allow_html=True
                    )

                show_explanation(
                    category,
                    st.session_state.question,
                    st.session_state.answer
                )

        if reveal:

            st.markdown(
                f'<div class="answer-box"><b>সঠিক উত্তর:</b><br>{st.session_state.answer}</div>',
                unsafe_allow_html=True
            )

            show_explanation(
                category,
                st.session_state.question,
                st.session_state.answer
            )


# ============================================================
# REFERENCE TAB
# ============================================================

with tab_reference:

    st.header("📚 Quick Grammar Reference")

    st.subheader("1️⃣ Be Verb")

    st.markdown("""
| Subject | Be Verb |
|---|---|
| I | am |
| He / She / It | is |
| You / We / They | are |
""")

    st.subheader("2️⃣ Have Verb")

    st.markdown("""
| Subject | Verb |
|---|---|
| I / You / We / They | have |
| He / She / It | has |
""")

    st.subheader("3️⃣ Main Verb")

    st.markdown("""
**Present:** I play. / He plays.

**Past:** I played.

**Future:** I will play.

**Negative:** I do not play. / He does not play.

**Past Negative:** I did not play.
""")

    st.subheader("4️⃣ There")

    st.markdown("""
- There is a book.
- There are two books.
- There was a book.
- There were two books.
- Is there a book?
- Are there two books?
""")

    st.markdown(
        '<div class="tip-box"><b>⭐ মনে রাখবে:</b> Translation শুধু শব্দ বদলানো নয়। '
        'প্রথমে বাক্যের ধরন, subject, tense এবং verb-এর কাজ বুঝে তারপর English sentence তৈরি করতে হবে।</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "📘 Bangla ↔ English Translation Lab | শেখো → অনুবাদ করো → উত্তর দাও → ভুল ধরো"
)
