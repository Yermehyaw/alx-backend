/**
 * Create a running client to connect to a running backgrpund server 
 * inorder to store and retrieve data
 */

import redis from 'redis';



/**
 * set values on he client
 */
function setNewSchool(schoolName, value) {
  const client = redis.createClient();
  client.on('error', err => console.log('Redis client not connected to the server: ', err));

  client.on('connect', () => console.log('Redis client connected to the server'));

  client.on('ready', () => {
    client.set(schoolName, value, redis.print);
  });
}


/**
 * Get the value of a key in the db
 */
function displaySchoolValue(schoolName) {
  const client = redis.createClient();
  client.on('error', err => console.log('Redis client not connected to the server: ', err));
  client.on('ready', () => {
    client.get(schoolName, (err, reply) => {
      if (err) {
	console.log('Err occurred: ', err);
	return;
      }
      console.log(reply);
    });
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
