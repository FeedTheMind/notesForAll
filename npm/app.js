var unsecuredPassword = 'password';
var bcrypt = require('bcrypt'); // require function allows us to access modules
var colors = require('colors');

bcrypt.genSalt(10, function(err, salt) {
  bcrypt.hash(unsecuredPassword, salt, function(err, hash) {
    console.log(hash.green);  
  });
});
