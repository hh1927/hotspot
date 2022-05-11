import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import("./CreateAcc.css");

//const baseURL = //api location here

export default function CreateAcc() {
  const [user, setUser] = useState("")
  const [pass, setPass] = useState("")
  const [first, setFirst] = useState("")
  const [last, setLast] = useState("")
  const [dob, setDOB] = useState("")
  const [email, setEmail] = useState("")
  const [phone, setPhone] = useState("")
  const [type, setType] = useState("")


  return (
    <div className="login">
      <h1>Create an Account </h1>
      <a href="/bsettings">
        <button id="settings">
          {" "}
          <img src="https://img.icons8.com/nolan/64/apple-settings.png" />
        </button>
      </a>
      <div>
        <form>
          <label>
            Username: <input type="text" value={user} />
          </label>
          <br />
          <label>
            Password: <input type="text" value={pass} />
          </label>
          <br />
          <label>
            First Name: <input type="text" value={first} />
          </label>
          <br />
          <label>
            Last Name: <input type="text" value={last} />
          </label>
          <br />
          <label>
            Date of Birth (MM/DD/YYYY): <input type="text" value={dob} />
          </label>
          <br />
          <label>
            Email: <input type="text" value={email} />
          </label>
          <br />
          <label>
            Phone Number: <input type="text" value={phone} />
          </label>
          <br />
          <label>
            Type of Account:
            <select id="dropdown">
              <option>Select...</option>
              <option value="Customer">Customer</option>
              <option value="Business">Business</option>
            </select>
            value = {type}
          </label>
        </form>
      </div>

      <button
        onClick={() => (window.location.href = "/cHome")} //need to decide on page after login
        className="button1"
      >
        Create Personal
      </button>
      <button
        onClick={() => (window.location.href = "/bHome")} //need to decide on page after login
        className="button1"
      >
        Create Business
      </button>
    </div>
  );
}
