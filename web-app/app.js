const http = require("http");
const { spawn } = require("child_process");

const hostname = "127.0.0.1";
const port = 3000;

const server = http.createServer((req, res) => {
  if (req.url === "/run") {
    // Spawn a new child process to run the Python script
    const python = spawn("python", ["script.py"]);

    // Listen for data from the child process and log it to the console
    python.stdout.on("data", (data) => {
      console.log(`Python script output: ${data}`);
    });

    // Listen for errors from the child process and log them to the console
    python.stderr.on("data", (data) => {
      console.error(`Python script error: ${data}`);
    });

    // Listen for the child process to close and send a response to the client
    python.on("close", (code) => {
      if (code === 0) {
        res.statusCode = 200;
        res.end;
      } else {
        res.statusCode = 500;
        res.end("Python script failed to run.");
      }
    });
  } else {
    // Serve the HTML page that contains the button
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/html");
    res.end(`
      <!DOCTYPE html>
      <html>
        <body>
          <button onclick="runScript()">Run Python Script</button>

          <script>
            function runScript() {
              fetch('/run')
                .then(response => response.text())
                .then(result => alert(result));
            }
          </script>
        </body>
      </html>
    `);
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
