"""POLYVERSE — a Python-powered everyday polymer explorer.
Run with: streamlit run app.py
"""

import random
import streamlit as st

from molecules import make_molecule_figure
from polymers import POLYMERS, EVERYDAY_OBJECTS, FACTS
from pico import PICO_SVG, pico_message
from styles import CSS
from selector import REQUIREMENTS, get_recommendation

st.set_page_config(
    page_title="Polyverse | Everyday life, molecular magic",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(CSS, unsafe_allow_html=True)

PAGES = ["Welcome", "Polymer selector", "Polymer explorer", "Everyday finder", "Molecule lab", "Random facts"]

with st.sidebar:
    st.markdown(
        """
        <div class="poly-logo">
          <div class="poly-logo-mark">✳</div>
          <div><div class="poly-logo-name">POLYVERSE</div><div class="poly-logo-sub">Everyday life · Molecular magic</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("YOUR PERSONAL POLYMER FIELD GUIDE")
    page = st.radio("Explore", PAGES, index=0, key="navigation")
    st.markdown("---")
    st.markdown("**Pico's quick note**")
    st.caption("Polymers are all around you. Start with an object you know, then discover the material behind it.")
    st.markdown("---")
    st.markdown("<span class='small-muted'>BUILT FOR CURIOUS MINDS</span>", unsafe_allow_html=True)


def section_heading(kicker, title, subtitle=None):
    st.markdown(
        "<div class='kicker'>{}</div><div class='section-title'>{}</div>{}".format(
            kicker, title,
            "<div class='section-sub'>{}</div>".format(subtitle) if subtitle else "",
        ),
        unsafe_allow_html=True,
    )


def render_pico(message, eyebrow="PICO · YOUR POLYVERSE GUIDE"):
    st.markdown(pico_message(message, eyebrow), unsafe_allow_html=True)


def go_to_molecule(name):
    st.session_state["molecule_choice"] = name
    st.session_state["navigation"] = "Molecule lab"


def go_to_explorer(name):
    st.session_state["explorer_choice"] = name
    st.session_state["navigation"] = "Polymer explorer"


def render_polymer_detail(name):
    polymer = POLYMERS[name]
    st.markdown(
        "<div class='kicker'>POLYMER FIELD NOTES · {}</div>".format(polymer["family"]),
        unsafe_allow_html=True,
    )
    st.markdown("<div class='section-title'>{}</div>".format(name), unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>{}</div>".format(polymer["tagline"]), unsafe_allow_html=True)

    c1, c2 = st.columns([1.05, 1.35], gap="large")
    with c1:
        st.markdown("<div class='info-panel'><h3>Why it matters</h3><p>{}</p></div>".format(polymer["why_it_matters"]), unsafe_allow_html=True)
        st.write("")
        st.markdown("<div class='info-panel'><h3>Look out for</h3><p>{}</p></div>".format(polymer["watch_out"]), unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='info-panel'><h3>Key properties</h3><ul>{}</ul></div>".format("".join("<li>{}</li>".format(x) for x in polymer["properties"])), unsafe_allow_html=True)
        st.write("")
        st.markdown("<div class='info-panel'><h3>Where you may find it</h3><ul>{}</ul></div>".format("".join("<li>{}</li>".format(x) for x in polymer["daily_uses"])), unsafe_allow_html=True)

    st.write("")
    left, right = st.columns([1, 1], gap="large")
    with left:
        st.markdown("<div class='info-panel'><div class='poly-meta'>REPEATING UNIT · SIMPLIFIED NOTATION</div><h3 style='font-size:1.35rem'>{}</h3><p>{}</p></div>".format(polymer["repeat_unit"], "The brackets and subscript n indicate that this pattern repeats many times along a polymer chain."), unsafe_allow_html=True)
    with right:
        st.markdown("<div class='info-panel'><div class='poly-meta'>A REAL-WORLD EXAMPLE</div><h3>Material in action</h3><p>{}</p></div>".format(polymer["example"]), unsafe_allow_html=True)

    st.button("Open this polymer in the 3D Molecule Lab", key="detail_to_lab", on_click=go_to_molecule, args=(name,))


# -----------------------------------------------------------------------------
# WELCOME
# -----------------------------------------------------------------------------
if page == "Welcome":
    st.markdown(
        """
        <div class="hero">
          <div class="hero-chip">A LITTLE SCIENCE IN EVERYDAY LIFE</div>
          <h1>Meet the materials<br>that make life move.</h1>
          <p>From the bottle in your hand to the cable beside your desk, polymers quietly shape the world around you. Explore them with Pico, your curious little guide.</p>
          <div class="hero-art">{}</div>
        </div>
        """.format(PICO_SVG),
        unsafe_allow_html=True,
    )
    render_pico("Hey there! I'm Pico. What would you like to explore today? Pick a polymer, choose an everyday object, or zoom right into a molecule. Let's make materials make sense.")

    section_heading("START EXPLORING", "Where should we begin?", "Choose a path. You can move between these spaces anytime using the menu on the left.")
    cols = st.columns(5, gap="medium")
    cards = [
        ("🎯", "Polymer selector", "Choose a requirement and get a polymer recommendation with a scientific reason."),
        ("🧪", "Polymer explorer", "Meet eight polymers and discover their properties, uses and limitations."),
        ("🧺", "Everyday finder", "Choose an object from daily life and see which polymer may be used in it."),
        ("🧬", "Molecule lab", "Rotate, inspect and zoom into simplified 3D repeating-unit models."),
        ("✨", "Random facts", "Collect surprising facts about the science behind ordinary materials."),
    ]
    for col, card in zip(cols, cards):
        with col:
            st.markdown("<div class='feature-card'><div class='emoji'>{}</div><h3>{}</h3><p>{}</p></div>".format(*card), unsafe_allow_html=True)

    st.write("")
    section_heading("THE POLYMER LINE-UP", "Eight materials. Countless possibilities.", "A quick preview of the materials waiting inside Polyverse.")
    poly_cols = st.columns(4, gap="medium")
    for col, (name, data) in zip(poly_cols, list(POLYMERS.items())[:4]):
        with col:
            st.markdown("<div class='poly-card'><span class='poly-dot' style='background:{}'></span><span class='poly-meta'>{}</span><h3>{}</h3><p>{}</p></div>".format(data["color"], data["family"], name, data["tagline"]), unsafe_allow_html=True)
    poly_cols2 = st.columns(4, gap="medium")
    for col, (name, data) in zip(poly_cols2, list(POLYMERS.items())[4:]):
        with col:
            st.markdown("<div class='poly-card'><span class='poly-dot' style='background:{}'></span><span class='poly-meta'>{}</span><h3>{}</h3><p>{}</p></div>".format(data["color"], data["family"], name, data["tagline"]), unsafe_allow_html=True)

    st.write("")
    st.markdown("<div class='footer'>POLYVERSE · Learn the material. Understand the object. Make informed choices.</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# POLYMER SELECTOR
# -----------------------------------------------------------------------------
elif page == "Polymer selector":
    section_heading(
        "PICO'S MATERIAL MATCHMAKER",
        "What does your product need to do?",
        "Choose the main requirement. Polyverse will recommend a polymer and give one sentence explaining the match.",
    )
    render_pico(
        "Tell me what your product needs! Pick the requirement number, submit it, and I'll suggest a polymer. If the number isn't valid, I'll ask you to choose again.",
        "PICO · LET'S FIND A MATERIAL",
    )

    # Keep the menu and the free-text input separate: the free-text field is
    # intentional because it lets the app detect and explain invalid choices.
    st.markdown("<div class='selector-options-title'>CHOOSE ONE MAIN REQUIREMENT</div>", unsafe_allow_html=True)
    option_columns = st.columns(2, gap="medium")
    for index, (number, requirement) in enumerate(REQUIREMENTS.items()):
        with option_columns[index % 2]:
            st.markdown(
                "<div class='selector-option'>"
                "<div class='selector-option-top'><span class='selector-number'>{}</span><span class='selector-tag'>{}</span></div>"
                "<div class='selector-option-icon'>{}</div><h3>{}</h3></div>".format(
                    number, requirement["tag"], requirement["icon"], requirement["title"]
                ),
                unsafe_allow_html=True,
            )

    with st.form("polymer_requirement_form", clear_on_submit=False):
        choice_text = st.text_input(
            "Enter your choice number (1–5)",
            placeholder="For example, 4",
            key="requirement_choice_input",
            help="Enter a number from 1 to 5. The program checks the input when you submit.",
        )
        submitted = st.form_submit_button("Find my polymer  →", use_container_width=True)

    if submitted:
        recommendation = get_recommendation(choice_text)
        if recommendation is None:
            st.session_state["selector_result"] = None
            st.session_state["selector_invalid"] = True
        else:
            st.session_state["selector_result"] = str(choice_text).strip()
            st.session_state["selector_invalid"] = False

    if st.session_state.get("selector_invalid", False):
        st.error("Invalid choice! Please select a valid option from 1 to 5 and try again.")

    selected_number = st.session_state.get("selector_result")
    if selected_number in REQUIREMENTS:
        result = REQUIREMENTS[selected_number]
        st.markdown(
            "<div class='selector-result'>"
            "<div class='selector-result-kicker'>YOUR POLYMER RECOMMENDATION</div>"
            "<div class='selector-result-row'><div class='selector-result-icon'>{}</div>"
            "<div><div class='selector-result-label'>RECOMMENDED POLYMER</div>"
            "<div class='selector-result-name'>{}</div></div></div>"
            "<div class='selector-reason-label'>WHY THIS POLYMER?</div>"
            "<p class='selector-reason'>{}</p></div>".format(
                result["icon"], result["polymer"], result["reason"]
            ),
            unsafe_allow_html=True,
        )
        result_left, result_right = st.columns(2)
        with result_left:
            st.button(
                "Explore {}".format(result["polymer"]),
                key="selector_explore_result",
                on_click=go_to_explorer,
                args=(result["polymer"],),
                use_container_width=True,
            )
        with result_right:
            st.button(
                "View its 3D structure",
                key="selector_molecule_result",
                on_click=go_to_molecule,
                args=(result["polymer"],),
                use_container_width=True,
            )

    with st.expander("Peer-testing challenge and sample test cases"):
        st.markdown(
            "**Try the printer scenario:** A small guide inside a printer must let a moving part slide smoothly. "
            "Predict the answer before entering **5**. The expected recommendation is PTFE."
        )
        st.table(
            [
                {"Test input": "1", "Expected result": "Kevlar – high strength relative to weight"},
                {"Test input": "2", "Expected result": "Polyaniline – conductivity in a suitable doped form"},
                {"Test input": "3", "Expected result": "PLA – suitable grade for industrial composting"},
                {"Test input": "4", "Expected result": "PTFE – low coefficient of friction"},
                {"Test input": "5", "Expected result": "PTFE – smooth-sliding printer guide"},
                {"Test input": "8 or abc", "Expected result": "Invalid choice message; ask the user to choose 1–5"},
            ]
        )
        st.caption(
            "A recommendation is a first material match, not a final engineering specification. "
            "Real product selection also depends on grade, load, temperature, manufacturing and end-of-life requirements."
        )

# -----------------------------------------------------------------------------
# POLYMER EXPLORER
# -----------------------------------------------------------------------------
elif page == "Polymer explorer":
    section_heading("THE MATERIAL LIBRARY", "Get to know your polymers", "Select a material to explore its family, properties, everyday uses and practical limitations.")
    render_pico("Think of this as your polymer field guide. A material is not 'good' or 'bad' by itself—the best choice depends on what the product needs to do and what happens after we use it.")

    names = list(POLYMERS.keys())
    selected = st.selectbox("Choose a polymer", names, key="explorer_choice")
    render_polymer_detail(selected)

    st.write("")
    section_heading("BROWSE THE LIBRARY", "Explore all eight")
    cols = st.columns(4, gap="medium")
    for col, (name, data) in zip(cols, POLYMERS.items()):
        with col:
            st.markdown("<div class='poly-card'><span class='poly-dot' style='background:{}'></span><span class='poly-meta'>{}</span><h3>{}</h3><p>{}</p><p class='small-muted'>Repeat unit: {}</p></div>".format(data["color"], data["family"], name, data["tagline"], data["repeat_unit"]), unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# EVERYDAY FINDER
# -----------------------------------------------------------------------------
elif page == "Everyday finder":
    section_heading("FROM OBJECT TO MATERIAL", "What's it made of?", "Choose something familiar and uncover a polymer that may be used to make it.")
    render_pico("Show me something from your everyday life! I'll connect it to a polymer and explain which property makes that material useful. Remember: products can use different materials, so always check the label or product specification.")

    object_names = list(EVERYDAY_OBJECTS.keys())
    selected_object = st.selectbox("Pick an everyday object", object_names, key="object_choice")
    item = EVERYDAY_OBJECTS[selected_object]
    polymer = POLYMERS[item["polymer"]]

    st.markdown("<div class='info-panel'><div class='kicker'>{} · EVERYDAY OBJECT</div><h2 style='font-family:Manrope;color:#214638;margin:.2rem 0'>{}</h2><p style='font-size:1rem;color:#65796d'>{}</p></div>".format(item["category"], selected_object, item["reason"]), unsafe_allow_html=True)
    st.write("")
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.markdown("<div class='info-panel'><div class='poly-meta'>A POSSIBLE POLYMER MATCH</div><h2 style='font-family:Manrope;color:#214638'>{}</h2><p>{}</p><p><b>Why this fit?</b> {}</p></div>".format(item["polymer"], polymer["family"], item["reason"]), unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='info-panel'><h3>Keep in mind</h3><p>{}</p><h3>Explore the material</h3><p>{}</p></div>".format(item["alternatives"], polymer["watch_out"]), unsafe_allow_html=True)
    st.write("")
    st.button("Explore {} in the polymer library".format(item["polymer"]), key="object_to_polymer", on_click=go_to_explorer, args=(item["polymer"],))
    st.button("See its molecular structure", key="object_to_molecule", on_click=go_to_molecule, args=(item["polymer"],))

# -----------------------------------------------------------------------------
# MOLECULE LAB
# -----------------------------------------------------------------------------
elif page == "Molecule lab":
    section_heading("ZOOM INTO THE SMALL WORLD", "The 3D molecule lab", "Explore a simplified repeating-unit model. Drag to rotate, scroll to zoom and use the camera controls to reset your view.")
    render_pico("Ready to go microscopic? The colourful spheres represent atoms, and the connecting lines represent chemical bonds. Try rotating the structure to see it from another angle!")

    polymer_names = list(POLYMERS.keys())
    default_molecule = st.session_state.get("molecule_choice", "Kevlar")
    if default_molecule not in polymer_names:
        default_molecule = "Kevlar"
    default_index = polymer_names.index(default_molecule)
    molecule_name = st.selectbox("Select a polymer structure", polymer_names, index=default_index, key="molecule_choice")
    molecule_info = POLYMERS[molecule_name]

    left, right = st.columns([1.7, 1], gap="large")
    with left:
        st.markdown("<div class='info-panel' style='padding:.55rem .6rem .2rem'><div class='poly-meta' style='padding:.55rem .8rem 0'>ROTATABLE MOLECULAR MODEL · DRAG TO ROTATE</div></div>", unsafe_allow_html=True)
        fig = make_molecule_figure(molecule_name)
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "scrollZoom": True,
                "displayModeBar": True,
                "displaylogo": False,
                "responsive": True,
                "modeBarButtonsToRemove": ["toImage"],
            },
            key="molecule_figure_" + molecule_name,
        )
        st.markdown("<div class='molecule-note'>Tip: click and drag to rotate · scroll to zoom · use the Plotly camera controls to reset the view. On a phone, use two fingers to zoom where supported.</div>", unsafe_allow_html=True)
    with right:
        st.markdown("<div class='info-panel'><div class='kicker'>REPEATING UNIT</div><h2 style='font-family:Manrope;color:#214638'>{}</h2><p>{}</p><hr><h3>What to notice</h3><p>{}</p></div>".format(molecule_info["repeat_unit"], molecule_info["family"], molecule_info["why_it_matters"]), unsafe_allow_html=True)
        st.write("")
        st.markdown("<div class='info-panel'><h3>Atom colour key</h3><p><span style='color:#505b66'>●</span> Carbon &nbsp; <span style='color:#f3f5f7'>●</span> Hydrogen &nbsp; <span style='color:#e36f69'>●</span> Oxygen</p><p><span style='color:#6593d6'>●</span> Nitrogen &nbsp; <span style='color:#78b97b'>●</span> Fluorine &nbsp; <span style='color:#56a87c'>●</span> Chlorine</p></div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("<div class='molecule-note'><b>Scientific note:</b> These are simplified educational sketches of representative repeat-unit connectivity. They are not crystallographic structures, measured bond lengths, full polymer chains or to-scale atomic models. For complex polymers such as polyaniline, the exact structure also depends on oxidation state and doping.</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# RANDOM FACTS
# -----------------------------------------------------------------------------
elif page == "Random facts":
    section_heading("A POCKETFUL OF SCIENCE", "A little polymer surprise", "Tap the button to discover another fact about the materials hiding in plain sight.")
    render_pico("I collect tiny science surprises. Here's one for your curiosity shelf. Want another? Just shuffle the fact!")

    if "current_fact" not in st.session_state:
        st.session_state["current_fact"] = random.choice(FACTS)
    if st.button("✨ Give me another fact", key="new_fact"):
        candidates = [fact for fact in FACTS if fact != st.session_state["current_fact"]]
        st.session_state["current_fact"] = random.choice(candidates or FACTS)

    st.markdown("<div class='fact-panel'><div class='fact-word'>✦ FACT DROP · POLYVERSE</div><div class='fact-copy'>{}</div></div>".format(st.session_state["current_fact"]), unsafe_allow_html=True)
    st.write("")
    section_heading("KEEP EXPLORING", "More facts to take with you")
    facts_cols = st.columns(3, gap="medium")
    selected_facts = random.sample(FACTS, 3)
    for col, fact in zip(facts_cols, selected_facts):
        with col:
            st.markdown("<div class='feature-card'><div class='emoji'>✳</div><p>{}</p></div>".format(fact), unsafe_allow_html=True)

st.markdown("<div class='footer'>POLYVERSE · An educational polymer explorer · Always check product specifications and local disposal guidance.</div>", unsafe_allow_html=True)
