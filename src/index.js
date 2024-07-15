const express = require('express');
const multer = require('multer');
const Tesseract = require('tesseract.js');
const path = require('path');
const fs = require('fs');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.post('/extract-text', upload.single('image'), (req, res) => {
    const imagePath = req.file.path;

    Tesseract.recognize(
        imagePath,
        'eng',
        {
            logger: m => console.log(m)
        }
    ).then(({ data: { text } }) => {
        fs.unlinkSync(imagePath); // Clean up the uploaded image
        res.json({ text });
    }).catch(err => {
        console.error(err);
        res.status(500).json({ error: err.message });
    });
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
