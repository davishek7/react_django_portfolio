import React from "react";
import { FaLinkedin, FaTwitterSquare } from "react-icons/fa";

const About = () => {
  return (
    <section className="s2">
      <div className="main-container">
        <div className="about-wrapper">
          <div className="about-me">
          <h4>Work Experience</h4>
            <h5>Associate Developer
              <br />
              <i>Vyrazu Labs Pvt. Ltd.</i>
              <br />
              <span style={{ fontSize: "15px" }}>from August,2021 to Present</span>
            </h5>
            <hr/>
            <h4>Internship</h4>
            <h5>Django Web Developer Intern
              <br />
              <i>Suven Consultants & Technology Pvt. Ltd.</i>
              <br />
              <span style={{ fontSize: "15px" }}>from May,2021 to June,2021</span>
              <div style={{ paddingTop: "15px" }}>
                <a href={process.env.PUBLIC_URL +"/static/internship_certificate_avishek.pdf"}
                  target="_blank" rel="noreferrer"
                  style={{ float: "left", fontSize: "15px" }}>
                  Certificate
                </a>
                <a target="_blank" rel="noreferrer"
                  href="https://internship.suvenconsultants.com/user?u=ZGF2aXNoZWs3QHNjdHBs"
                  style={{ float: "right", fontSize: "15px" }}>
                  Intern Profile
                </a>
              </div>
            </h5>
            <hr />

            <h4>TOP EXPERTISE</h4>

            <p>
              Fullstack developer with primary focus on Django + React:
              <a target="_blank" rel="noreferrer" href={process.env.PUBLIC_URL +"/static/Avishek's_Resume.pdf"}>
                Download Resume
              </a>
            </p>

            <div id="skills">
              <ul>
                <li>Python</li>
                <li>Django</li>
                <li>JavaScript</li>
                <li>React</li>
                <li>SQL</li>
                <li>PostgreSQL</li>
                <li>Github</li>
              </ul>

              <ul>
                <li>Gitlab</li>
                <li>MySQL</li>
                <li>Git</li>
                <li>AJAX</li>
                <li>Flask</li>
                <li>Heroku</li>
                <li>HTML/CSS</li>
              </ul>
            </div>
          </div>

          <div className="social-links">
            <img src={process.env.PUBLIC_URL +"/static/github.png"} alt="follow me" id="social_img" />
            <h3>Find me on Twitter & Linkedin</h3>
            <a
              target="_blank"
              rel="noreferrer"
              href="https://twitter.com/davishek7"
            >
              <FaTwitterSquare
                style={{ color: "#1DA1F2", backgroundColor: "#fff" }}
              />{" "}
              /davishek7
            </a>
            <br />
            <a
              target="_blank"
              rel="noreferrer"
              href="https://www.linkedin.com/in/davishek7/"
            >
              <FaLinkedin
                style={{ color: "#2867B2", backgroundColor: "#fff" }}
              />{" "}
              /in/davishek7
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
