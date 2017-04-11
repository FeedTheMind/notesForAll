var unsecuredPassword = 'password';
var bcrypt = require('bcrypt');

bcrypt.genSalt(10, function(err, salt) {
  bcrypt.hash(unsecuredPassword, salt, function(err, hash) {
    console.log(hash);  
  });
});
