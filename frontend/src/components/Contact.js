import React, { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { FaArrowUp } from "react-icons/fa";

toast.configure();
const Contact = () => {
  const [name, setName] = useState("");
  const [subject, setSubject] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const enabled =
    name.length > 0 &&
    subject.length > 0 &&
    email.length > 0 &&
    message.length > 0;
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("name", name);
    formData.append("subject", subject);
    formData.append("email", email);
    formData.append("message", message);

    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

    const config = {
      headers: {
        "Content-type": "application/json",
        "X-CSRFToken":getCookie('csrftoken')
      },
    };
    const res = await axios.post("/api/contact_view/", formData, config);
    if (res.status === 201) {
      toast.info(
        `Thank you ${name} for contacting me! I will back to you later.`,
        { position: toast.POSITION.TOP_CENTER }
      );
    } else{
      toast.error("Something went wrong! Please try again later.", {
        position: toast.POSITION.TOP_CENTER,
      });
    }
  };

  const topFunction = () => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }

  return (
    <section className="s2">
      <div className="main-container">
        <h3 style={{ textAlign: "center" }}>Get in touch</h3>
        <form id="contact-form" onSubmit={handleSubmit}>
          <label>Name</label>
          <input
            type="text"
            className="input-field"
            value={name}
            placeholder="Full Name"
            onChange={(e) => setName(e.target.value)}
            required
          />

          <label>Subject</label>
          <input
            type="text"
            className="input-field"
            value={subject}
            placeholder="Subject"
            onChange={(e) => setSubject(e.target.value)}
            required
          />

          <label>Email</label>
          <input
            type="email"
            className="input-field"
            value={email}
            placeholder="Your Email"
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <label>Message</label>
          <textarea
            value={message}
            className="input-field"
            placeholder="Your message"
            onChange={(e) => setMessage(e.target.value)}
            required
          />

          <input
            id="submit-btn"
            type="submit"
            value="Send"
            disabled={!enabled}
            style={{
              color: !enabled && "#A9A9A9",
              cursor: !enabled && "not-allowed",
            }}
          />
        </form>
      </div>
      <button onClick={topFunction} id="topBtn" title="Go to top"><FaArrowUp/></button>
    </section>
  );
};

export default Contact;
