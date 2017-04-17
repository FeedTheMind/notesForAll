'use strict';
// Note: Normally, the "required" modules are placed at the top, but for this demonstration, they are not

var gulp = require('gulp'); // require is a Node method
// Name variable name after module: best practice

// At this point, we should define a task, using the task method

// 'hello' is the name of the task
// the anonymous function serves as a callback
    // log(ging) a string is what it does
gulp.task('hello', function () {
  console.log('Hello, I am a Gulp task.');
});

// To run the above task, go to the command line (terminal) and run gulp hello

// Let's say that you want to run the above task without having
// to run gulp hello, how would you do it?

// You'd have to create a "default" task.
  // Add an array of dependencies as the second parameter.
    // The name of the item should be the "hello" task.
      // default will run after hello (and whatever else is in the array)
gulp.task('default', ['hello'], function () {
  console.log('Hello, I am the default task! I ran second.');
});
// Head back to gulpNotes.txt


///////////////////////// Concat

// Add gulp-concat
// Again, this "require" should be at the top, but not for this demo

var concat = require('gulp-concat'); // Note: naming variable gulp-concat would not work because of the hyphen--JavaScript engine will see it as a minus

// The task name is concatScripts
gulp.task('concatScripts', function () {
  // src() can take array of files or a string of a single file
  // This gets the js foler and all files with .js ending
  gulp.src('js/*.js')
  // concat() takes a string parameter of the file you want to create
    // Let's create our all.js file
    .pipe(concat('all.js'))
  // dest() writes to disk, versus stream
    .pipe(gulp.dest('js'));
});

// Now, if you run gulp concatScripts from the command line,
// you should see that all.js is now in the js folder
// But there is a problem! The single file has a ton of unnecessary space. Let's fix that!
//Head back to gulpNotes.txt

/////////////////////// Minify

var uglify = require('gulp-uglify');
var rename = require('gulp-rename'); // Rename allows for the file to be, you guessed it, renamed
// This is great so that you don't override the concat all.js 
// Install gulp-rename with npm install gulp-rename --save-dev

gulp.task('minifyScripts', function () {
  gulp.src('js/all.js')
    .pipe(uglify())
    .pipe(rename('all.min.js'))
    .pipe(gulp.dest('js'));
});
