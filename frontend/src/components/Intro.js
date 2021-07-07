import React from 'react'

const Intro = () => {
    return (
        <section className="s1">
        <div className="main-container">
          <div className="greeting-wrapper">
            <h1>Hi, I'm Avishek Das</h1>
          </div>
          <div className="intro-wrapper">
            <div className="nav-wrapper">
              <div className="dots-wrapper">
                <div id="dot-1" className="browser-dot"></div>
                <div id="dot-2" className="browser-dot"></div>
                <div id="dot-3" className="browser-dot"></div>
              </div>
              <ul id="navigation">
                <li><a href="#contact-form">Contact</a></li>
              </ul>
            </div>
            <div className="left-column">
              <img src={process.env.PUBLIC_URL +'/static/Me.jpg'} alt="Avishek Das" id="profile_pic" />
              <h5 style={{textAlign: "center", lineHeight: "0"}}>
                Personalize Theme
              </h5>
              <div id="theme-options-wrapper">
                <div data-mode="light" id="light-mode" className="theme-dot"></div>
                <div data-mode="blue" id="blue-mode" className="theme-dot"></div>
                <div data-mode="green" id="green-mode" className="theme-dot"></div>
                <div data-mode="purple" id="purple-mode" className="theme-dot"></div>
              </div>
              <p id="settings-note">
                Theme settings will be saved for<br />your next visit.
              </p>
            </div>
            <div className="right-column">
              <div id="preview-shadow">
                <div id="preview">
                  <div id="corner-tl" className="corner"></div>
                  <div id="corner-tr" className="corner"></div>
                  <h3>What I Do</h3>
                  <p>
                    I am now studying Computer Science and Engineering, and I am a
                    django developer.
                  </p>
                  <div id="corner-br" className="corner"></div>
                  <div id="corner-bl" className="corner"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    )
}

export default Intro
