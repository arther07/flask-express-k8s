const express = require("express");
const app = express();

app.get("/api", (req, res) => {
    res.send("Hello from the Express backend!");
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Express server listening on port ${PORT}`);
});
