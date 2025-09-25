
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-app.js";
  import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/10.5.0/firebase-database.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyAX51gD4GsZd-p1beFhRBooFJ7m7WrHgTI",
    authDomain: "h1gh-cl0ud.firebaseapp.com",
    databaseURL: "https://h1gh-cl0ud-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "h1gh-cl0ud",
    storageBucket: "h1gh-cl0ud.appspot.com",
    messagingSenderId: "810810494855",
    appId: "1:810810494855:web:9c8de348c0036876f6cd22"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const db = getDatabase();
  const starCountRef = ref(db, 'high/');
  // # ! in case i forgot i put in some flag in flag # !
  
  // onValue(starCountRef, (snapshot) => {
  // const data = snapshot.val();
  // console.log(data)
  // });

  function nice(items) {
    console.log(items);
  }

  function nope(err){
    console.log(err);
  }

