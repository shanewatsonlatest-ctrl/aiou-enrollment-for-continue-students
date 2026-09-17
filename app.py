import streamlit as st

# ---------------- PAGE CONFIG (important for Google & browser tab) ----------------
st.set_page_config(
    page_title="AIOU Continuing Students Enrollment Guide 2026 | Re-Admission Process",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- SIMPLE SEO-STYLE META (helps a bit even in Streamlit) ----------------
st.markdown(
    """
    <meta name="description" content="Complete guide for AIOU (Allama Iqbal Open University) continuing / already-enrolled students: how to re-enroll, fee submission, deadlines, and FAQs for every semester.">
    <meta name="keywords" content="AIOU, AIOU enrollment, AIOU continuing students, AIOU re-admission, AIOU fee, AIOU semester enrollment, Allama Iqbal Open University">
    """,
    unsafe_allow_html=True,
)

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📚 AIOU Enrollment Guide")
page = st.sidebar.radio(
    "Menu",
    [
        "🏠 Home",
        "📝 Enrollment Process (Step by Step)",
        "💰 Fee & Payment Guide",
        "📅 Important Dates",
        "❓ FAQs",
        "✅ Personal Checklist",
        "🔗 Official Links",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "⚠️ Yeh app AIOU ki **official website nahi** hai. Yeh ek independent guide hai. "
    "Final aur updated maloomat hamesha aiou.edu.pk se confirm karein."
)

# ---------------- HOME ----------------
if page == "🏠 Home":
    st.title("🎓 AIOU Continuing Students – Enrollment Guide")
    st.markdown(
        """
        Agar aap **Allama Iqbal Open University (AIOU)** ke pehle se enrolled (continuing) student hain
        aur har naye semester me apna admission/enrollment continue karna chahte hain, to yeh guide aapke liye hai.

        Is app me aapko milega:
        - Enrollment process ka **step-by-step tareeqa**
        - Fee jama karwane ka **sahi procedure**
        - Semester wise **important dates** ka pattern
        - Sab se zyada pooche jane wale **sawalat (FAQs)**
        - Aik **personal checklist** jo aap follow kar saken

        📖 Mazeed tafseeli maloomat ke liye parhein:
        [AIOU Enrollment for Continue Students](https://aiou.studyvillas.com/aiou-enrollment/)
        """
    )
    st.success("👈 Left sidebar se koi bhi section select karein.")

# ---------------- PROCESS ----------------
elif page == "📝 Enrollment Process (Step by Step)":
    st.title("📝 Continuing Students ke liye Enrollment Process")
    st.markdown(
        """
        AIOU har semester (Spring & Autumn) me continuing students ke liye enrollment/re-admission
        ka window kholta hai. Neeche general step-by-step process diya gaya hai:
        """
    )

    steps = [
        ("1️⃣ AIOU Student Portal / eServices par login karein",
         "Apne registration number aur password se AIOU ke online portal (aiou.edu.pk se link milega) par login karein."),
        ("2️⃣ Naye semester ka enrollment form check karein",
         "Portal me dekhein ke aapke program ke liye current semester ka enrollment form open hai ya nahi."),
        ("3️⃣ Courses select karein",
         "Apne study scheme ke mutabiq agle semester ke courses select karein. Confusion ho to apne Regional Office se rabta karein."),
        ("4️⃣ Challan form generate karein",
         "System se fee challan/voucher generate hoga jisme total amount likha hoga."),
        ("5️⃣ Fee jama karwayein",
         "Bank (jese ABL, HBL, ya jo bhi allowed ho) ya online banking se challan ki fee tay shuda deadline se pehle jama karwayein."),
        ("6️⃣ Confirmation check karein",
         "Fee jama karwane ke baad kuch dinon me portal par apna enrollment status 'confirmed' zaroor check karein."),
        ("7️⃣ Study material ka intezar karein",
         "Enrollment confirm hone ke baad AIOU courier/postal service se ya online (LMS) study material bhejta hai."),
    ]

    for title, desc in steps:
        with st.expander(title):
            st.write(desc)

    st.warning(
        "⚠️ Har semester me exact steps ya portal ka design thoda change ho sakta hai. "
        "Hamesha apne AIOU Regional Office ya official website se latest instructions confirm karein."
    )

    st.markdown(
        "📖 Har step ki detail, screenshots aur latest updates ke liye ye guide parhein: "
        "**[AIOU Enrollment for Continue Students](https://aiou.studyvillas.com/aiou-enrollment/)**"
    )

# ---------------- FEE ----------------
elif page == "💰 Fee & Payment Guide":
    st.title("💰 Fee & Payment Guide")
    st.markdown(
        """
        ### Fee jama karwane ka tareeqa
        - Enrollment ke baad system se generate hone wala **challan/voucher** use karein.
        - Fee designated banks ki kisi bhi branch se ya online/mobile banking se jama karwayi ja sakti hai.
        - Deadline se pehle fee jama karwana zaroori hai, warna:
            - Late fee lagti hai, ya
            - Enrollment cancel ho sakta hai.

        ### Kuch zaroori tips
        - Challan ki copy hamesha **sambhal kar rakhein** (scan/photo bhi le lein).
        - Fee jama karwane ke 2-3 working days baad portal par status check karein.
        - Agar fee jama karwane ke bawajood enrollment confirm na ho, apne Regional Office se turant rabta karein.
        """
    )
    st.info("💡 Exact fee amount program aur credit hours ke hisaab se alag hota hai — yeh sirf general guide hai.")

# ---------------- DATES ----------------
elif page == "📅 Important Dates":
    st.title("📅 Important Dates – General Pattern")
    st.markdown(
        """
        AIOU saal me do semesters chalata hai:

        | Semester | Aam taur par shuru | Enrollment window |
        |---|---|---|
        | **Spring** | January – February | December – February (extensions bhi hoti hain) |
        | **Autumn** | August – September | July – August (extensions bhi hoti hain) |

        ⚠️ **Note:** Yeh sirf general pattern hai. Exact dates har semester AIOU announce karta hai
        aur kayi dafa deadline **extend** bhi hoti hai. Sahi aur current date hamesha official
        website ya Regional Office se check karein.
        """
    )

# ---------------- FAQs ----------------
elif page == "❓ FAQs":
    st.title("❓ Frequently Asked Questions")

    faqs = [
        ("Continuing student kise kehte hain?",
         "Woh student jo pehle se AIOU me kisi program me enrolled hai aur agle semester bhi apni degree continue kar raha hai (naya admission nahi le raha)."),
        ("Agar mein ek semester enrollment miss kar doon to kya hoga?",
         "Aksar AIOU aik ya do semester ka gap allow karta hai lekin lambay gap ke baad dobara fresh admission process follow karna pad sakta hai. Apne Regional Office se confirm karein."),
        ("Enrollment fee jama karwane ke baad kitne din me confirm hoti hai?",
         "Aam taur par kuch working days lagte hain. Portal par status check karte rahein."),
        ("Courses change karwa sakte hain?",
         "Haan, lekin uske liye alag procedure aur kabhi kabhi extra fee hoti hai — Regional Office se guidance lein."),
        ("Agar portal par masla aaye to kya karein?",
         "AIOU Regional Office (apne shehar wala) ya AIOU helpline/official email par rabta karein."),
    ]

    for q, a in faqs:
        with st.expander(f"Q: {q}"):
            st.write(a)

# ---------------- CHECKLIST ----------------
elif page == "✅ Personal Checklist":
    st.title("✅ Apna Enrollment Checklist")
    st.markdown("Har item complete karne ke baad tick karein — yeh sirf is session ke liye save hota hai.")

    items = [
        "Portal par login kar liya",
        "Enrollment window open hai, confirm kar liya",
        "Courses select kar liye",
        "Challan generate kar liya",
        "Fee jama karwa di",
        "Challan ki copy save kar li",
        "2-3 din baad status check kar liya",
        "Enrollment 'confirmed' show ho raha hai",
    ]

    for item in items:
        st.checkbox(item)

    st.caption("Note: Yeh checklist browser refresh hone par reset ho jayegi (koi data server par save nahi hota).")

# ---------------- LINKS ----------------
elif page == "🔗 Official Links":
    st.title("🔗 Official AIOU Links")
    st.markdown(
        """
        - 🌐 AIOU Official Website: [aiou.edu.pk](https://www.aiou.edu.pk)
        - 🖥️ Student eServices / Portal: AIOU website ke "Student Login" section se access karein
        - 📍 Regional Offices List: AIOU website par "Regional Services" section me milegi
        - 📞 Helpline/Contact: AIOU official website ke "Contact Us" page par current numbers milenge

        ⚠️ Hamesha URL check karein ke wo **aiou.edu.pk** domain hi ho — fraud/fake websites se bachein.
        """
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "🔎 Detailed guide: "
    "[AIOU Enrollment for Continue Students](https://aiou.studyvillas.com/aiou-enrollment/)"
)
st.caption(
    "Yeh ek independent, student-friendly guide hai jo AIOU continuing students ki madad ke liye banayi gayi hai. "
    "Official aur final maloomat ke liye hamesha aiou.edu.pk visit karein."
)
