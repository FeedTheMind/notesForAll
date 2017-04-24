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
/*
app.get('/blog/:title?', function (req, res) {
  var title = req.params.title;

  if (title === undefined) {
    res.status(503);
    res.send('This page is under construction.');
  } else {
    var post = posts[title];
    res.send();
  }
});
*/

// To visit the "blog" route, type localhost:3000/blog
// Example 2 - End

// Templates and Template Rendering
// Templates are a special file with own syntax 
// Server dynamically "injects" template with data, creating a "view" of HTML
// Most template languages resemble HTML
// For this example, Example 3, let's use pug

// Example 3 - Begin
// src folder now has template folder (directory)
// template, after defining in app, will look for templates from template folder
  // template is the name to specify what files go here . . . some developers use views, not template

// In template, there is an index.pug file
  // To render this, we set the following

app.get('/blog/:title?', function (req, res) {
  var title = req.params.title;

  if (title === undefined) {
    res.status(503);
    res.send('This page is under construction.');
  } else {
    var post = posts[title] || {};
    res.render('post', {post: post});
  }
});

app.set('view engine', 'pug');
app.set('views', __dirname + '/templates');

app.get('/', function (req, res) {
  // .pug extension isn't required
  res.render('index');
});

// use() defines middleware in Express; it is the logic that tells Express how to handle a request before it arrives at a route
app.use('/static', express.static(__dirname + '/public'));

// Example 3 - End

// Miscellaneous 
// node-inspector works with older versions of node
  // experimental technology = node --inspect path/to/file

// It is important to keep your directory organized. Scaffolding helps with this! Giving logical names helps, too.

// A layout template is a great solution to maximize code reuse. 
  // Other templates (views) will inherit from this template.
  // If you're wondering what the benefits are, I don't blame you.
  // The major benefit of a layout template (view) is that you only have to change one file, not one, two, or dozens.
