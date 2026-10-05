import streamlit as st

st.set_page_config(page_title="Poetry Lab - For English Dept", page_icon="📚", layout="wide")

# Custom CSS to increase font size across the app
st.markdown("""
    <style>
    /* Main body text and questions font size */
    p, li, .stMarkdown {
        font-size: 18px !important;
    }
    /* Headers font size */
    h1 {
        font-size: 38px !important;
    }
    h2 {
        font-size: 30px !important;
    }
    h3 {
        font-size: 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

poems = {
    "Echo - Christina Rossetti": {
        "poet": "Christina Rossetti (1830-1894)",
        "original": """Come to me in the silence of the night;
Come in the speaking silence of a dream;
Come with soft rounded cheeks and eyes as bright
As sunlight on a stream;
Come back in tears,
O memory, hope, love of finished years.

O dream how sweet, too sweet, too bitter sweet,
Whose wakening should have been in Paradise,
Where souls brimfull of love abide and meet;
Where thirsting longing eyes
Watch the slow door
That opening, letting in, lets out no more.

Yet come to me in dreams, that I may live
My very life again though cold in death:
Come back to me in dreams, that I may give
Pulse for pulse, breath for breath:
Speak low, lean low,
As long ago, my love, how long ago.""",
        "translation_bn": """রাতের নীরবতায় তুমি আমার কাছে এসো;
স্বপ্নের মুখরিত নীরবতায় এসো;
নদীর স্রোতে রোদের মতো উজ্জ্বল চোখ আর
নরম ফোলা গাল নিয়ে এসো;
অশ্রুতে ফিরে এসো,
হে স্মৃতি, আশা, ও অতীতের ফুরিয়ে যাওয়া ভালোবাসা।

ও স্বপ্ন কী যে মধুর, বড্ড মধুর, বড্ড কড়া-মধুর,
যার ঘুম ভাঙা উচিত ছিল স্বর্গে,
যেখানে ভালোবাসায় ভরপুর আত্মারা বসবাস করে ও মিলিত হয়;
যেখানে তৃষ্ণার্ত ব্যাকুল চোখগুলো
ধীরে খোলা দরজার দিকে চেয়ে থাকে
যা একবার খুললে আর কাউকে বের হতে দেয় না।

তবুও স্বপ্নে আমার কাছে এসো, যেন আমি বাঁচতে পারি
আমার আসল জীবন আবার যদিও মৃত্যুর হিমশীতলতায়:
স্বপ্নে আমার কাছে ফিরে এসো, যেন আমি দিতে পারি
স্পন্দনের বিনিময়ে স্পন্দন, নিশ্বাসের বিনিময়ে নিশ্বাস:
ধীরে কথা বলো, ঝুঁকে পড়ো কাছে,
অনেক দিন আগে যেমন ছিলে, আমার ভালোবাসা, কত দিন আগে।""",
        "summary_bn": "ক্রিস্টিনা রোসেটির লেখা 'Echo' কবিতাটিতে কবি তাঁর হারিয়ে যাওয়া ভালোবাসার স্মৃতি এবং প্রিয়জনকে স্বপ্নে ফিরে পাওয়ার আকুল আবেদন জানিয়েছেন।",
        "theme": "Loss, Memory, Longing, Death and Dream",
        "devices": ["Apostrophe", "Repetition", "Alliteration", "Imagery"],
        "analysis": "কবিতাটিতে মোট তিনটি স্তবক রয়েছে এবং এর ছন্দ বিন্যাস AABCBC।",
        "questions": [
            {
                "set": "Set A",
                "q1": "(a) What is the significance of the title 'Echo'?",
                "q2": "(b) How does the stanzaic structure reflect the sorrowful tone?",
                "q3": "(c) How are unfulfilled love and pain portrayed?"
            }
        ]
    },
    "Stopping by Woods on a Snowy Evening - Robert Frost": {
        "poet": "Robert Frost (1874-1963)",
        "original": """Whose woods these are I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound's the sweep
Of easy wind and downy flake.

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.""",
        "translation_bn": """এই বন কার, তা আমি জানি বলে মনে হয়।
তবে তার বাড়ি তো গ্রামে;
সে আমাকে এখানে থেমে থাকতে দেখবে না
তার বনে বরফ জমতে দেখার জন্য।

আমার ছোট ঘোড়াটি নিশ্চয়ই অদ্ভুত মনে করছে
কাছাকাছি কোনো ফার্মহাউস না থাকা সত্ত্বেও থেমে থাকাকে
বন এবং জমে যাওয়া হ্রদের মাঝখানে—
বছরের সবচেয়ে অন্ধকার সন্ধ্যায়।

সে তার জিনের ঘণ্টা নাড়িয়ে দেয়
কোনো ভুল হলো কি না তা জিজ্ঞেস করার জন্য।
অন্য যে শব্দটুকু আছে তা হলো মৃদু বাতাস
আর তুলোর মতো নরম বরফ পড়ার শব্দ।

বনগুলো সুন্দর, অন্ধকার আর গভীর,
কিন্তু আমার কিছু প্রতিশ্রুতি রাখার আছে,
আর ঘুমানোর আগে আমাকে আরও অনেক পথ যেতে হবে,
আর ঘুমানোর আগে আমাকে আরও অনেক পথ যেতে হবে।""",
        "summary_bn": "রবার্ট ফ্রস্টের লেখা এই কবিতাটিতে প্রকৃতির সৌন্দর্য ও মানুষের সামাজিক দায়িত্ব এবং কর্তব্যের মধ্যকার দ্বন্দ্ব ফুটে উঠেছে।",
        "theme": "Nature vs. Duty, Temptation vs. Responsibility",
        "devices": ["Alliteration", "Imagery", "Repetition", "Personification"],
        "analysis": "প্রকৃতির সৌন্দর্য মানুষকে যেভাবে মন্ত্রমুগ্ধ করে এবং তার দায়িত্ববোধকে ভুলিয়ে দিতে চায়, তার এক চমৎকার রূপায়ন এখানে রয়েছে।",
        "questions": [
            {
                "set": "Standard Set",
                "q1": "(a) What is the central theme of the poem?",
                "q2": "(b) What do the woods and the horse symbolize?",
                "q3": "(c) Explain the significance of the last stanza."
            }
        ]
    },
    "To Helen - Edgar Allan Poe": {
        "poet": "Edgar Allan Poe (1809-1849)",
        "original": """Helen, thy beauty is to me
Like those Nicean barks of yore,
That gently, o'er a perfumed sea,
The weary, way-worn wanderer bore
To his own native shore.""",
        "translation_bn": "হেলেন, তোমার সৌন্দর্য আমার কাছে...",
        "summary_bn": "Helen এর সৌন্দর্য ক্লান্ত নাবিককে যেমন ঘরে ফেরায়...",
        "theme": "Ideal Beauty, Classical Allusion",
        "devices": ["Simile", "Allusion"],
        "analysis": "১৫ লাইনের ৩টি stanza...",
        "questions": [
            {
                "set": "Standard Set",
                "q1": "Why compare Helen to Nicean barks?",
                "q2": "Explain 'the glory that was Greece...'",
                "q3": "Function of classical allusions?"
            }
        ]
    },
    "The Collar - George Herbert": {
        "poet": "George Herbert (1593-1633)",
        "original": "I struck the board, and cried, No more...",
        "translation_bn": "আমি টেবিলে আঘাত করলাম...",
        "summary_bn": "কবি ঈশ্বরের প্রতি বিদ্রোহ করে স্বাধীন হতে চান...",
        "theme": "Spiritual Rebellion vs Submission",
        "devices": ["Metaphor", "Pun"],
        "analysis": "৩৬ লাইন, irregular rhyme...",
        "questions": [
            {
                "set": "Standard Set",
                "q1": "What does 'Collar' symbolize?",
                "q2": "Is this a spiritual autobiography?",
                "q3": "Explain 'rope of sands'"
            }
        ]
    },
    "The Solitary Reaper - William Wordsworth": {
        "poet": "William Wordsworth (1770-1850)",
        "original": "Behold her, single in the field...",
        "translation_bn": "তাকে দেখো, মাঠে একা দাঁড়িয়ে আছে...",
        "summary_bn": "স্কটল্যান্ডের পাহাড়ে একা এক মেয়েকে ফসল কাটতে দেখেন...",
        "theme": "Beauty of Solitude, Music and Memory",
        "devices": ["Simile", "Alliteration"],
        "analysis": "৪টি stanza, Ballad form...",
        "questions": [
            {
                "set": "Standard Set",
                "q1": "How does Wordsworth romanticize the reaper?",
                "q2": "Why music stays long after?",
                "q3": "Discuss as Romantic poem."
            }
        ]
    }
}

literary_terms = {
    "Simile": "Like, as diye tulona.",
    "Metaphor": "Shorasori tulona.",
    "Alliteration": "Ek-i sound er punarabritti.",
    "Allusion": "Itihas/puraner reference.",
    "Conceit": "Chomotprod tulona.",
    "Imagery": "Chitrakalpo"
}

st.title("📚 Poetry Lab - English Literature App")
st.caption("For your syllabus | Made by Swapon")

with st.sidebar:
    st.header("📖 Select Poem")
    choice = st.selectbox("Choose:", list(poems.keys()))
    st.divider()
    st.header("🔍 Literary Terms")
    term = st.selectbox("Quick Dictionary:", ["Select"] + list(literary_terms.keys()))
    if term != "Select":
        st.info(f"**{term}:** {literary_terms[term]}")

data = poems[choice]
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(choice)
    st.write(f"**Poet:** {data['poet']}")
    
    tab1, tab2 = st.tabs(["📜 Original Poem", "🇧🇩 Bangla Translation"])
    with tab1:
        st.text_area("Original Text", data["original"], height=250, key="orig")
    with tab2:
        st.text_area("বাংলা অনুবাদ", data["translation_bn"], height=250, key="trans")
        
    st.markdown(f"**🇧🇩 বাংলায় সারমর্ম:**\n\n{data['summary_bn']}")
    st.markdown(f"**💡 Analysis:** {data['analysis']}")
    
    if choice == "Echo - Christina Rossetti":
        st.divider()
        st.markdown("### 📝 Important Q&A")
        st.markdown("""
**What is the significance of the title 'Echo'?**
In Christina Rossetti's poem 'Echo', the title carries a deep symbolic meaning representing lost love and unfulfilled longing.
        """)
    elif choice == "Stopping by Woods on a Snowy Evening - Robert Frost":
        st.divider()
        st.markdown("### 📝 Important Q&A")
        st.markdown("""
**What is the central theme of the poem?**
The central theme is the conflict between the pull of nature's beauty and the burden of human responsibilities and duties.
        """)

with col2:
    st.success(f"**Theme:** {data['theme']}")
    st.write("**Literary Devices:**")
    for d in data["devices"]:
        st.write(f"- {d}")
    
    st.warning("**Exam Questions:**")
    for item in data["questions"]:
        if isinstance(item, dict):
            st.markdown(f"**{item['set']}**")
            st.markdown(item['q1'])
            st.markdown(item['q2'])
            st.markdown(item['q3'])
            st.divider()

st.divider()
st.subheader("🎯 Quick Quiz")
q = st.radio("Which poem ends with 'My Lord' as submission?", ["Echo", "The Collar", "The Solitary Reaper", "To Helen", "Stopping by Woods on a Snowy Evening"], index=None)
if q:
    if q == "The Collar":
        st.balloons()
        st.success("Correct!")
    else:
        st.error("Try again!")
