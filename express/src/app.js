// Example 1
// First, let's use the 'use strict'; statement

'use strict'; // Throws error if common mistakes are made

// Second, let's require express

var express = require('express');

// Third, let's assign express to another variable, app

var app = express(); 

// Now, let's listen on port 3000; listen() is an express method
// To run the code, head to the console and type node path_name_to_file/app.js

// Example: node src/app.js

app.listen(3000, function () {
  console.log('Frontend server is listening on localhost:3000');
});

// Head to localhost:3000 and you should see:
    // Cannot Get /

// And with that, we have created our first Express app


//But let's create a route
// The slash (/) is for the root of the site, also known as location parameter 
// Second parameter is anonymous callback function

// req = request and res = response

// Remove the slashes and rerun server 

// app.get('/', function (req, res) {
//   res.send('I love <strong>learning</strong>!');
// });

// Note: If changes aren't present, restart server
// Ctrl C (twice) will exit the Node environment
// If you don't like stopping and restarting the server,
  // install nodemon -- it's a great tool for Node
    // npm install nodemon -g
// Example 1 - End


// Example 2 - Begin

// Let's add another route.
// We will be gathering data from the mock folder, specifically posts.json. 
// Note: mock (folder) signifies that the "mock" information does not come from a database and that it is not created from our application. 

var posts = require('./mock/posts.json');

app.get('/blog', function (req, res) {
  res.send(posts.Running.title);
});

// To visit the "blog" route, type localhost:3000/blog
