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
        "summary_bn": """ক্রিস্টিনা রোসেটির (Christina Rossetti) লেখা 'Echo' কবিতাটিতে কবি তাঁর হারিয়ে যাওয়া ভালোবাসার স্মৃতি এবং প্রিয়জনকে স্বপ্নে ফিরে পাওয়ার আকুল আবেদন জানিয়েছেন। এই কবিতায় 'Echo' বা প্রতিধ্বনি একটি অত্যন্ত গভীর প্রতীকী অর্থ বহন করে। প্রতিধ্বনিকে যেমন দূর থেকে শোনা যায় কিন্তু কখনো হাত দিয়ে ধরে রাখা যায় না, ঠিক তেমনি আমাদের জীবন থেকে হারিয়ে যাওয়া স্মৃতি বা মানুষগুলোও তেমনি—তারা দূরত্বে থেকে যায়, তাদের কেবল অনুভূতি, শব্দ কিংবা ছায়া হিসেবেই অনুভব করা যায়, কিন্তু বাস্তবে তাদের আর কখনো কাছে পাওয়া সম্ভব নয়।

কবিতায় কবি রাতের গভীর নিঃসঙ্গতা কিংবা স্বপ্নের জগতে প্রিয়জনের ফিরে আসার জন্য আকুল প্রার্থনা করেছেন। মানুষের অবচেতন মনে স্বপ্ন যেন এমন একটি জাদুকরী মাধ্যম হয়ে ওঠে, যেখানে হারিয়ে যাওয়া বা মৃত্যুর কোলে ঢোলে পড়া মানুষগুলো আবার জীবন্ত হয়ে ফিরে আসে। কবিতার প্রতিটি লাইনে প্রকাশ পেয়েছে এক অদ্ভুত মানসিক ব্যাকুলতা, গভীর দীর্ঘশ্বাস, বিরহ এবং তীব্র স্মৃতিকাতরতা।

এখানে 'Echo' শব্দটিকে একই সাথে আশা এবং নিরাশার এক অপূর্ব প্রতীক হিসেবে ফুটিয়ে তোলা হয়েছে। কারণ স্বপ্ন ভেঙে যখন চোখের সামনে নির্মম বাস্তব ভেসে ওঠে, তখন ঠিক প্রতিধ্বনির মতোই সব সুখের আবেশ মিলিয়ে যায়, কেবল হৃদয়ে থেকে যায় তার দীর্ঘস্থায়ী এক সুতীব্র অনুভূতি। এই অমর কবিতার মধ্য দিয়ে মূলত মানবমনের চিরন্তন প্রিয়জন হারানোর বেদনা, না পাওয়ার দীর্ঘশ্বাস এবং ভালোবাসার অবিনশ্বর রূপটি অত্যন্ত সুন্দর ও নিখুঁতভাবে চিত্রিত হয়েছে।""",
        "theme": "Loss, Memory, Longing, Death and Dream",
        "devices": ["Apostrophe", "Repetition (Come)", "Alliteration", "Paradox (too sweet, too bitter sweet)", "Imagery"],
       "analysis": """ক্রিস্টিনা রোসেটির (Christina Rossetti) বিখ্যাত 'Echo' কবিতাটি কাঠামোগত এবং ভাবগত উভয় দিক থেকেই অত্যন্ত সুনিপুণ ও গভীর একটি সাহিত্যকর্ম। কবিতাটিতে মোট তিনটি স্তবক (stanzas) রয়েছে এবং এর ছন্দ বিন্যাস বা রাইম স্কিম (Rhyme Scheme) হলো AABCBC, যা স্তবকগুলোকে এক ধরনের মৃদু, বিষণ্ণ ও শোকাবহ সুরের আবহে বেঁধে রাখে। কবিতার সামগ্রিক সুরটি স্পষ্টতই একটি 'Elegiac tone' বা শোকগাথার সুর, যেখানে প্রিয়জনকে চিরতরে হারিয়ে ফেলার তীব্র দীর্ঘশ্বাস প্রতিটি পংক্তিতে অনুভূত হয়। 

কবিতাটির মূল দর্শন আবর্তিত হয়েছে স্মৃতি, স্বপ্ন (Dreams) এবং বাস্তবতার এক অদ্ভুত মায়াজালে। কবি এমন এক অলীক জগতের সন্ধান করেছেন যা কেবল অবচেতন মনের স্বপ্নরাজ্যেই সম্ভব। বাস্তব জীবনের নির্মম মৃত্যু (Death) এবং দূরত্ব যেখানে ভালোবাসাকে হিমশীতল ও অসম্ভব করে তোলে, স্বপ্ন সেখানে একমাত্র জাদুকরী আশ্রয়স্থল হয়ে ওঠে যেখানে মৃত বা হারিয়ে যাওয়া ভালোবাসা পুনরায় জীবিত ও প্রাণবন্ত হয়ে উঠতে পারে। স্তবক থেকে স্তবকে কবির এই আকুলতা—যেমন 'Pulse for pulse, breath for breath'—মৃত্যুর দেয়াল ভেদ করে প্রিয়জনকে কাছে পাওয়ার এক চিরন্তন মানবিক আবেদন ফুটিয়ে তোলে। পরিশেষে, এই কবিতাটি কেবল দুঃখ বা শোককেই ফুটিয়ে তোলে না, বরং মানবমনের অবচেতন স্তরের অমর ভালোবাসার এক অসাধারণ মনস্তাত্ত্বিক রূপায়ণ এখানে ঘটিয়েছেন কবি।""",
       st.markdown(f"**💡 Analysis:** {data['analysis']}")
    
    st.divider()
    
    # প্রশ্ন ও উত্তর সেকশন
    st.markdown("### 📝 Important Q&A")
    st.markdown("""
**What is the significance of the title 'Echo' in the poem? / কবিতার নামের সঙ্গে 'Echo' বা প্রতিধ্বনির প্রতীকী বিষয়টি কীভাবে জড়িত? [3]**

In Christina Rossetti's poem 'Echo', the title carries a deep symbolic meaning. Just like a real echo can be heard from far away but can never be touched or held, the poet's lost loved one is also permanently gone and out of reach.

ক্রিস্টিনা রোসেটির 'Echo' কবিতায় 'Echo' বা প্রতিধ্বনি নামটি খুব গভীর একটি প্রতীক হিসেবে কাজ করেছে। বাস্তব জীবনে যেমন প্রতিধ্বনিকে দূর থেকে শোনা যায় কিন্তু কখনো হাত দিয়ে ধরে রাখা যায় না, ঠিক তেমনি কবির হারিয়ে যাওয়া প্রিয়জনও আজ মৃত্যু বা দূরত্বের কারণে চিরতরে দূরে চলে গেছে।

Just as an echo is only a faint reflection of an original sound, 'dreams' and 'memory' act as that echo in this poem. To escape the painful reality, the poet depends on her dreams, where her dead love comes back to life temporarily.

প্রতিধ্বনি যেমন আসল শব্দের একটি মৃদু ছায়া মাত্র, তেমনি এই কবিতায় 'স্বপ্ন' এবং 'স্মৃতি' হলো সেই প্রতিধ্বনি। বাস্তব জীবনের কষ্ট থেকে বাঁচতে কবি স্বপ্নের ওপর ভরসা করেন, যেখানে তাঁর মৃত ভালোবাসা সাময়িকভাবে আবার ফিরে আসে।

Even after a sound stops, its echo lingers for a while before fading away. Similarly, long after the loved one's death, the deep pain, sorrow, and endless sighs keep echoing inside the poet's heart.

কোথাও শব্দ থেমে যাওয়ার পরেও যেমন তার প্রতিধ্বনি অনেকক্ষণ ধরে বেজে চলে, ঠিক তেমনি প্রিয়জনের মৃত্যুর পরও তাঁর গভীর শোক, দীর্ঘশ্বাস এবং না পাওয়ার হাহাকার কবির হৃদয়ে সবসময় বেজে চলতে থাকে।
    """)
       "questions": [
            {
                "set": "Set A",
                "q1": "(a) What is the significance of the title 'Echo' in the poem? / কবিতার নামের সঙ্গে 'Echo' বা প্রতিধ্বনির প্রতীকী বিষয়টি কীভাবে জড়িত? [3]",
                "q2": "(b) How does the poem's stanzaic structure and rhythm reflect the sorrowful tone of the speaker? / কবিতার স্তবকের গঠন বা ছন্দ কীভাবে কবির মনের ভেতরের দুঃখের সুরটিকে ফুটিয়ে তোলে? [3]",
                "q3": "(c) How are unfulfilled love and the deep pain of losing a loved one portrayed in this poem? / অপূর্ণ ভালোবাসা এবং প্রিয়জনকে চিরতরে হারানোর বেদনা এই কবিতায় কীভাবে ফুটে উঠেছে? [4]"
            },
            {
                "set": "Set B",
                "q1": "(a) How does the line 'Pulse for pulse, breath for breath' express the deep desire to get back the lost loved one beyond life and death? / 'Pulse for pulse, breath for breath'— এই লাইনটির মাধ্যমে জীবন ও মৃত্যুর দেয়াল পেরিয়ে প্রিয়জনকে কাছে পাওয়ার আকুলতা কীভাবে প্রকাশ পেয়েছে? [3]",
                "q2": "(b) How does the poet use 'dreams' as a medium to bring back her lost loved one? / কবিতায় কবি প্রিয়জনকে ফিরে পাওয়ার জন্য 'স্বপ্ন' (dream)-কে একটি মাধ্যম হিসেবে কীভাবে ব্যবহার করেছেন? [3]",
                "q3": "(c) How does the paradox 'too sweet, too bitter sweet' reflect the speaker's complex psychological state? / কবিতায় ব্যবহৃত বিপরীতধর্মী কথা যেমন 'too sweet, too bitter sweet'— কবির জটিল মনস্তাত্ত্বিক অবস্থাকে কীভাবে তুলে ধরে? [4]"
            },
            {
                "set": "Set C",
                "q1": "(a) What is the overall tone of the poem, and what kind of feeling does it evoke in the reader? / পুরো কবিতাটির সামগ্রিক সুর বা ভাব কেমন এবং এটি পড়ার সময় পাঠকের মনে কেমন অনুভূতি জাগায়? [3]",
                "q2": "(b) Identify and explain any two literary devices used by the poet in the first stanza. / কবিতার প্রথম স্তবকে কবি যে কোনো দুটি গুরুত্বপূর্ণ অলংকার বা লিটারারি ডিভাইস ব্যবহার করেছেন, তা সহজ ভাষায় বুঝিয়ে লেখো। [3]",
                "q3": "(c) Discuss 'Echo' as a Victorian elegiac poem where memory and sighs are deeply explored. / একটি ভিক্টোরিয়ান যুগের বিরহের কবিতা বা Elegy হিসেবে 'Echo' কবিতায় স্মৃতি এবং দীর্ঘশ্বাসের বিষয়টি কতটা গভীরভাবে ফুটিয়ে তোলা হয়েছে? [4]"
            }
        ]
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
        "translation_bn": """হেলেন, তোমার সৌন্দর্য আমার কাছে
কালের সেই নাইসিয়ান তরণীর মতো,
যা সুবাসিত সমুদ্রের ওপর দিয়ে মৃদুভাবে,
ক্লান্ত, পথশ্রান্ত পর্যটককে বয়ে নিয়ে গিয়েছিল
তার নিজের জন্মভূমিতে

উদ্বেগজনক সমুদ্রে বহুদিন ঘুরে বেড়ানোর পর,
তোমার হায়াসিন্থের মতো চুল, তোমার ক্লাসিক মুখাবয়ব,
তোমার জলপরী সদৃশ চালচলন আমাকে ফিরিয়ে এনেছে ঘরে
গ্রিসের সেই প্রাচীন গৌরবে,
আর রোমের সেই মহিমায়।

দেখো! ঐ উজ্জ্বল জানালার কুলুঙ্গিতে
কীভাবে তোমাকে মূর্তির মতো দাঁড়িয়ে থাকতে দেখি,
তোমার হাতে রয়েছে অ্যাগেট পাথরের প্রদীপ!
আহ, সাইকি, সেই অঞ্চল থেকে তুমি এসেছ
যা পবিত্র ভূমি!""",
        "summary_bn": "Helen এর সৌন্দর্য ক্লান্ত নাবিককে যেমন ঘরে ফেরায়, তেমনি কবিকেও অন্ধকার থেকে আলোয় ফিরিয়ে এনেছে।",
        "theme": "Ideal Beauty, Classical Allusion, Love as Salvation",
        "devices": ["Simile (Like Nicean barks)", "Allusion (Greece, Rome, Psyche)", "Alliteration (weary, way-worn)", "Metaphor"],
        "analysis": "১৫ লাইনের ৩টি stanza। Helen হলো Jane Stanard, যিনি Poe কে মাতৃস্নেহ দিয়েছিলেন। Neo-classical reference এ ভরা।",
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
        "poet": "George Herbert (1593-1633) - Metaphysical Poet",
        "original": """I struck the board, and cried, No more.
I will abroad.
... (full text)
But as I rav'd and grew more fierce and wilde
At every word,
Methought I heard one calling, Child!
And I replied, My Lord.""",
        "translation_bn": """আমি টেবিলে আঘাত করলাম এবং চিৎকার করে বললাম, আর নয়।
আমি বাইরে চলে যাবো।
... (সম্পূর্ণ লেখা)
কিন্তু আমি যখন ক্ষিপ্ত হয়ে আরও হিংস্র ও বন্য হয়ে উঠছিলাম
প্রতিটি শব্দে,
মনে হলো আমি কাউকে ডাকতে শুনলাম, শিশু!
আর আমি জবাব দিলাম, আমার প্রভু।""",
        "summary_bn": "কবি ঈশ্বরের প্রতি বিদ্রোহ করে স্বাধীন হতে চান, কিন্তু শেষে 'Child!' ডাক শুনে 'My Lord' বলে আত্মসমর্পণ করেন। Collar মানে ধর্মের বন্ধন।",
        "theme": "Spiritual Rebellion vs Submission, Divine Love",
        "devices": ["Metaphor (Collar = restraint)", "Conceit (rope of sands)", "Dramatic Monologue", "Pun", "Biblical Allusion"],
        "analysis": "৩৬ লাইন, irregular rhyme। শেষ ২ লাইনে সব রাগ শান্ত। The Temple কাব্যগ্রন্থের কবিতা।",
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
        "original": """Behold her, single in the field,
Yon solitary Highland Lass!
Reaping and singing by herself;
Stop here, or gently pass!
...
The music in my heart I bore,
Long after it was heard no more.""",
        "translation_bn": """তাকে দেখো, মাঠে একা দাঁড়িয়ে আছে,
ঐ একাকী পাহাড়ি তরুণী!
একা একা ফসল কাটছে আর গান গাইছে;
এখানে থেমো, কিংবা মৃদু পায়ে চলে যাও!
...
সেই গান আমি আমার হৃদয়ে বহন করে চলেছি,
অনেক দিন পর যখন তা আর শোনা যায় না তারও বহু পরে।""",
        "summary_bn": "স্কটল্যান্ডের পাহাড়ে একা এক মেয়েকে ফসল কাটতে ও গান গাইতে দেখেন। গানের ভাষা না বুঝলেও সুর হৃদয়ে গেঁথে থাকে।",
        "theme": "Beauty of Solitude, Music and Memory, Nature",
        "devices": ["Simile (like Nightingale)", "Alliteration", "Romantic Imagery", "Hyperbole"],
        "analysis": "৪টি stanza, Ballad form, Rhyme: ABABCCDD। Wilkinson এর travelogue পড়ে লেখা।",
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

with col2:
    st.success(f"**Theme:** {data['theme']}")
    st.write("**Literary Devices:**")
    for d in data["devices"]:
        st.write(f"- {d}")
    
    st.warning("**Exam Questions:**")
    
    for item in data["questions"]:
        if isinstance(item, dict):
            st.markdown(f"**{item['set']}**")
            st.markdown(f"1. {item['q1']}")
            st.markdown(f"2. {item['q2']}")
            st.markdown(f"3. {item['q3']}")
            st.divider()
        else:
            st.markdown(f"- {item}")

st.divider()
st.subheader("🎯 Quick Quiz")
q = st.radio("Which poem ends with 'My Lord' as submission?", ["Echo", "The Collar", "The Solitary Reaper", "To Helen"], index=None)
if q:
    if q == "The Collar":
        st.balloons()
        st.success("Correct!")
    else:
        st.error("Try again!")
