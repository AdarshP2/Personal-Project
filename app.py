import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Will You Be My Valentine? 💕",
    page_icon="💕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Poppins:wght@300;400;600&family=Playfair+Display:wght@400;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #000000 0%, #1a001a 25%, #ff69b4 50%, #ff1493 75%, #000000 100%);
        background-size: 400% 400%;
        animation: gradient 20s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a001a 25%, #ff69b4 50%, #ff1493 75%, #000000 100%);
        background-size: 400% 400%;
        animation: gradient 20s ease infinite;
    }
    
    .valentine-container {
        text-align: center;
        padding: 3rem 2rem;
        background: rgba(255, 255, 255, 0.98);
        border-radius: 30px;
        box-shadow: 0 20px 60px rgba(255, 105, 180, 0.4), 0 0 40px rgba(0, 0, 0, 0.5);
        margin: 2rem auto;
        max-width: 650px;
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 105, 180, 0.3);
    }
    
    .valentine-title {
        font-family: 'Dancing Script', cursive;
        font-size: 4.5rem;
        color: #ff1493;
        margin-bottom: 1rem;
        text-shadow: 3px 3px 8px rgba(255, 105, 180, 0.5), 0 0 20px rgba(255, 20, 147, 0.3);
        animation: heartbeat 1.5s ease-in-out infinite;
        font-weight: 700;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.08); }
    }
    
    .valentine-subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.4rem;
        color: #333;
        margin-bottom: 1.5rem;
        font-weight: 300;
        line-height: 1.6;
    }
    
    .color-message {
        font-family: 'Playfair Display', serif;
        font-size: 1rem;
        color: #666;
        font-style: italic;
        margin-top: 1.5rem;
        padding: 1rem;
        background: rgba(255, 105, 180, 0.1);
        border-radius: 15px;
        border-left: 4px solid #ff1493;
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 3rem;
        flex-wrap: wrap;
    }
    
    .yes-button {
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 100%);
        color: white;
        border: none;
        padding: 1.2rem 3.5rem;
        font-size: 1.6rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        border-radius: 50px;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(255, 20, 147, 0.5), 0 0 20px rgba(255, 105, 180, 0.3);
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .yes-button:hover {
        transform: scale(1.1);
        box-shadow: 0 15px 40px rgba(255, 20, 147, 0.7), 0 0 30px rgba(255, 105, 180, 0.5);
    }
    
    .no-button-container {
        position: relative;
    }
    
    .no-button {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
        color: #ff69b4;
        border: 2px solid #ff69b4;
        padding: 1.2rem 3.5rem;
        font-size: 1.6rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        border-radius: 50px;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        transition: all 0.1s ease;
        text-decoration: none;
        display: inline-block;
        position: relative;
    }
    
    .heart {
        font-size: 2rem;
        animation: float 3s ease-in-out infinite;
        display: inline-block;
        margin: 0 0.5rem;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    .hearts-container {
        margin: 2rem 0;
    }
    
    .success-message {
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem;
        color: #ff1493;
        margin: 2rem 0;
        animation: fadeIn 1s ease-in;
        text-shadow: 2px 2px 6px rgba(255, 105, 180, 0.5);
    }
    
    .cheesy-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        color: #333;
        font-style: italic;
        margin: 1.5rem 0;
        line-height: 1.8;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        background: #f5576c;
        position: absolute;
    }
    
    /* Custom Streamlit button styling */
    button[kind="primary"] {
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
        padding: 0.8rem 2rem !important;
        box-shadow: 0 10px 30px rgba(255, 20, 147, 0.5), 0 0 20px rgba(255, 105, 180, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    button[kind="primary"]:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 15px 40px rgba(255, 20, 147, 0.7), 0 0 30px rgba(255, 105, 180, 0.5) !important;
    }
    
    button[kind="secondary"] {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%) !important;
        color: #ff69b4 !important;
        border: 2px solid #ff69b4 !important;
        border-radius: 50px !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
        padding: 0.8rem 2rem !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
        transition: none !important;
        will-change: transform !important;
    }
    
    /* Ensure button containers allow absolute positioning */
    div[data-testid="column"],
    div[class*="stColumn"],
    div[class*="column"] {
        position: relative !important;
        overflow: visible !important;
    }
    
    /* Container for buttons */
    .element-container {
        position: relative !important;
        overflow: visible !important;
    }
    
    /* Cute escape message */
    .escape-message {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 20, 147, 0.95);
        color: white;
        padding: 1rem 2rem;
        border-radius: 20px;
        font-family: 'Dancing Script', cursive;
        font-size: 1.5rem;
        z-index: 10001;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.3s ease;
        box-shadow: 0 10px 40px rgba(255, 20, 147, 0.5);
    }
    
    .escape-message.show {
        opacity: 1;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'response' not in st.session_state:
    st.session_state.response = None

# Main content
st.markdown("""
    <div class="valentine-container">
        <div class="hearts-container">
            <span class="heart">💕</span>
            <span class="heart" style="animation-delay: 0.5s;">💖</span>
            <span class="heart" style="animation-delay: 1s;">💗</span>
            <span class="heart" style="animation-delay: 1.5s;">💝</span>
            <span class="heart" style="animation-delay: 2s;">💘</span>
        </div>
        <h1 class="valentine-title">Will You Be My Valentine?</h1>
        <p class="valentine-subtitle">I have something special to ask you, Jaan 💕</p>
        <div class="color-message">
            <p style="margin: 0;">✨ Note - I chose black because it's your choice and you're the boss, and just like you, It's absolutely beautiful. The pink? That's my heart showing through. 💖</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# JavaScript for the "No" button that runs away from cursor

# Button container
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.session_state.response is None:
        st.markdown("""
            <p style="text-align: center; font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #666; font-style: italic; margin-bottom: 2rem;">
                Choose wisely, my love... 💕
            </p>
        """, unsafe_allow_html=True)
        
        button_col1, button_col2 = st.columns(2)
        
        with button_col1:
            if st.button("Yes 💕", key="yes", use_container_width=True, type="primary"):
                st.session_state.response = "yes"
                st.rerun()
        
        with button_col2:
            if st.button("No", key="no", use_container_width=True, type="secondary"):
                st.session_state.response = "no"
                st.rerun()
    
    elif st.session_state.response == "yes":
        st.markdown("""
            <div class="valentine-container">
                <div class="success-message">
                    My Heart is Yours Forever! 💕
                </div>
                <div class="hearts-container">
                    <span class="heart">💕</span>
                    <span class="heart" style="animation-delay: 0.5s;">💖</span>
                    <span class="heart" style="animation-delay: 1s;">💗</span>
                    <span class="heart" style="animation-delay: 1.5s;">💝</span>
                    <span class="heart" style="animation-delay: 2s;">💘</span>
                </div>
                <p class="cheesy-text">
                    You've just made me the happiest person in the universe! I know I am a little bad with my timing but we can make this work! 🌟<br>
                    I can't wait to celebrate this beautiful day with you, my love.<br>
                    You are my everything, and I'm so grateful to have you in my life. 💖✨
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Confetti effect
        st.balloons()
    
    elif st.session_state.response == "no":
        st.markdown("""
            <div class="valentine-container">
                <p class="cheesy-text" style="margin-top: 2rem;">
                    Wrong Choice! <br>
                    Ek hi Dil hai, Kitni baar todogi?
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Try Again 💕", key="try_again", use_container_width=True):
            st.session_state.response = None
            st.rerun()

# JavaScript for "No" button that moves to random position on hover (like the repo example)
st.markdown("""
<script>
(function() {
    let noButton = null;
    let attempts = 0;
    const maxAttempts = 200;
    let originalPosition = null;
    
    function findNoButton() {
        const buttons = Array.from(document.querySelectorAll('button'));
        noButton = buttons.find(btn => {
            const text = btn.textContent.trim();
            return text === 'No' && !text.includes('Yes') && !text.includes('💕') && !text.includes('Try Again');
        });
        
        if (noButton) {
            setupNoButton();
        } else if (attempts < maxAttempts) {
            attempts++;
            setTimeout(findNoButton, 100);
        }
    }
    
    function moveButton() {
        if (!noButton) return;
        
        // Get button dimensions
        const buttonWidth = noButton.offsetWidth;
        const buttonHeight = noButton.offsetHeight;
        
        // Calculate random position within viewport bounds
        const maxX = window.innerWidth - buttonWidth;
        const maxY = window.innerHeight - buttonHeight;
        
        // Ensure button stays within bounds (with some padding)
        const padding = 20;
        const x = Math.max(padding, Math.random() * Math.max(padding, maxX - padding));
        const y = Math.max(padding, Math.random() * Math.max(padding, maxY - padding));
        
        // Move button to random position
        noButton.style.left = x + 'px';
        noButton.style.top = y + 'px';
    }
    
    function setupNoButton() {
        if (!noButton) return;
        
        // Store original position
        const rect = noButton.getBoundingClientRect();
        originalPosition = {
            left: rect.left,
            top: rect.top,
            parent: noButton.parentElement
        };
        
        // Get the button's parent container (Streamlit column)
        const buttonParent = noButton.parentElement;
        const parentRect = buttonParent.getBoundingClientRect();
        
        // Make parent position relative if needed
        const parentStyle = window.getComputedStyle(buttonParent);
        if (parentStyle.position === 'static') {
            buttonParent.style.position = 'relative';
        }
        
        // Make button absolutely positioned
        noButton.style.position = 'absolute';
        noButton.style.left = (rect.left - parentRect.left) + 'px';
        noButton.style.top = (rect.top - parentRect.top) + 'px';
        noButton.style.zIndex = '10000';
        noButton.style.cursor = 'not-allowed';
        noButton.style.transition = 'left 0.3s ease, top 0.3s ease';
        
        // Prevent clicks
        const clickHandler = function(e) {
            e.preventDefault();
            e.stopPropagation();
            e.stopImmediatePropagation();
            moveButton(); // Move again on click attempt
            return false;
        };
        
        noButton.addEventListener('click', clickHandler, true);
        noButton.addEventListener('mousedown', clickHandler, true);
        noButton.addEventListener('mouseup', clickHandler, true);
        
        // Add mouseover event to move button (like the repo example)
        noButton.addEventListener('mouseenter', moveButton);
        noButton.addEventListener('mouseover', moveButton);
        
        // Also move on touch (for mobile)
        noButton.addEventListener('touchstart', function(e) {
            e.preventDefault();
            moveButton();
        });
    }
    
    // Start looking for button
    function start() {
        findNoButton();
        // Keep checking in case Streamlit rerenders
        setInterval(() => {
            if (!noButton || !document.body.contains(noButton)) {
                noButton = null;
                attempts = 0;
                findNoButton();
            }
        }, 2000);
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start);
    } else {
        start();
    }
    
    // Watch for DOM changes
    const observer = new MutationObserver(() => {
        if (!noButton || !document.body.contains(noButton)) {
            noButton = null;
            attempts = 0;
            setTimeout(findNoButton, 500);
        }
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
</script>
""", unsafe_allow_html=True)

