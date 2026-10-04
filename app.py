import streamlit as st

st.set_page_config(page_title="Poetry Lab - For English Dept", page_icon="📚", layout="wide")

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
        "summary_bn": "এই কবিতায় কবি তার হারিয়ে যাওয়া ভালোবাসার স্মৃতিকে স্বপ্নে ফিরে আসার আহ্বান জানাচ্ছেন। 'Echo' মানে প্রতিধ্বনি - যা আছে কিন্তু ধরা যায় না।",
        "theme": "Loss, Memory, Longing, Death and Dream",
        "devices": ["Apostrophe", "Repetition (Come)", "Alliteration", "Paradox (too sweet, too bitter sweet)", "Imagery"],
        "analysis": "৩টি stanza, Rhyme: AABCBC। Elegiac tone। স্বপ্নই একমাত্র জায়গা যেখানে মৃত ভালোবাসা জীবিত হয়।",
        "questions": ["What is significance of title 'Echo'?", "How does Rossetti use dream as motif?", "Explain 'Pulse for pulse, breath for breath'"]
    },
    "To Helen - Edgar Allan Poe": {
        "poet": "Edgar Allan Poe (1809-1849)",
        "original": """Helen, thy beauty is to me
Like those Nicean barks of yore,
That gently, o'er a perfumed sea,
The weary, way-worn wanderer bore
To his own native shore.

On desperate seas long wont to roam,
Thy hyacinth hair, thy classic face,
Thy Naiad airs have brought me home
To the glory that was Greece,
And the grandeur that was Rome.

Lo! in yon brilliant window-niche
How statue-like I see thee stand,
The agate lamp within thy hand!
Ah, Psyche, from the regions which
Are Holy-Land!""",
        "summary_bn": "Helen এর সৌন্দর্য ক্লান্ত নাবিককে যেমন ঘরে ফেরায়, তেমনি কবিকেও অন্ধকার থেকে আলোয় ফিরিয়ে এনেছে।",
        "theme": "Ideal Beauty, Classical Allusion, Love as Salvation",
        "devices": ["Simile (Like Nicean barks)", "Allusion (Greece, Rome, Psyche)", "Alliteration (weary, way-worn)", "Metaphor"],
        "analysis": "১৫ লাইনের ৩টি stanza। Helen হলো Jane Stanard, যিনি Poe কে মাতৃস্নেহ দিয়েছিলেন। Neo-classical reference এ ভরা।",
        "questions": ["Why compare Helen to Nicean barks?", "Explain 'the glory that was Greece...'", "Function of classical allusions?"]
    },
    "The Collar - George Herbert": {
        "poet": "George Herbert (1593-1633) - Metaphysical Poet",
        "original": """I struck the board, and cried, No more.
I will abroad.
... (full text)
But as I rav'd and grew more fierce and wilde
At every word,
Methought I heard one calling, Child!
And I replied, My Lord.""",
        "summary_bn": "কবি ঈশ্বরের প্রতি বিদ্রোহ করে স্বাধীন হতে চান, কিন্তু শেষে 'Child!' ডাক শুনে 'My Lord' বলে আত্মসমর্পণ করেন। Collar মানে ধর্মের বন্ধন।",
        "theme": "Spiritual Rebellion vs Submission, Divine Love",
        "devices": ["Metaphor (Collar = restraint)", "Conceit (rope of sands)", "Dramatic Monologue", "Pun", "Biblical Allusion"],
        "analysis": "৩৬ লাইন, irregular rhyme। শেষ ২ লাইনে সব রাগ শান্ত। The Temple কাব্যগ্রন্থের কবিতা।",
        "questions": ["What does 'Collar' symbolize?", "Is this a spiritual autobiography?", "Explain 'rope of sands'"]
    },
    "The Solitary Reaper - William Wordsworth": {
        "poet": "William Wordsworth (1770-1850)",
        "original": """Behold her, single in the field,
Yon solitary Highland Lass!
Reaping and singing by herself;
Stop here, or gently pass!
...
The music in my heart I bore,
Long after it was heard no more.""",
        "summary_bn": "স্কটল্যান্ডের পাহাড়ে একা এক মেয়েকে ফসল কাটতে ও গান গাইতে দেখেন। গানের ভাষা না বুঝলেও সুর হৃদয়ে গেঁথে থাকে।",
        "theme": "Beauty of Solitude, Music and Memory, Nature",
        "devices": ["Simile (like Nightingale)", "Alliteration", "Romantic Imagery", "Hyperbole"],
        "analysis": "৪টি stanza, Ballad form, Rhyme: ABABCCDD। Wilkinson এর travelogue পড়ে লেখা।",
        "questions": ["How does Wordsworth romanticize the reaper?", "Why music stays long after?", "Discuss as Romantic poem."]
    }
}

literary_terms = {
    "Simile": "Like, as দিয়ে তুলনা। Ex: Like Nicean barks",
    "Metaphor": "সরাসরি তুলনা। Ex: That time of year...",
    "Alliteration": "একই sound এর পুনরাবৃত্তি। Ex: weary, way-worn",
    "Allusion": "ইতিহাস/পুরাণের reference। Ex: Greece, Rome",
    "Conceit": "চমকপ্রদ তুলনা। Ex: rope of sands",
    "Imagery": "চিত্রকল্প"
}

st.title("📚 Poetry Lab - English Literature App")
st.caption("For your syllabus | Made by Swapon")

with st.sidebar:
    st.header("📖 Select Poem")
    choice = st.selectbox("Choose:", list(poems.keys()))
    st.divider()
    st.header("🔍 Literary Terms")
    term = st.selectbox("Quick Dictionary:", ["Select"] + list(literary_terms.keys()))
    if term!= "Select":
        st.info(f"**{term}:** {literary_terms[term]}")

data = poems[choice]
col1, col2 = st.columns([2,1])

with col1:
    st.subheader(choice)
    st.write(f"**Poet:** {data['poet']}")
    st.text_area("Original Text", data["original"], height=250)
    st.markdown(f"**🇧🇩 বাংলায় সারমর্ম:** {data['summary_bn']}")
    st.markdown(f"**💡 Analysis:** {data['analysis']}")

with col2:
    st.success(f"**Theme:** {data['theme']}")
    st.write("**Literary Devices:**")
    for d in data["devices"]:
        st.write(f"- {d}")
    st.warning("**Exam Questions:**")
    for q in data["questions"]:
        st.write(f"• {q}")

st.divider()
st.subheader("🎯 Quick Quiz")
q = st.radio("Which poem ends with 'My Lord' as submission?", ["Echo", "The Collar", "The Solitary Reaper", "To Helen"], index=None)
if q:
    if q == "The Collar":
        st.balloons()
        st.success("Correct!")
    else:
        st.error("Try again!")
