const express = require('express');
const path = require('path');

const app = express();

app.get('/passwd', (req, res) => {
    const p = '/etc/passwd';
    res.download(p);
});

app.listen('3030', (err) => {
    console.log("works");
});