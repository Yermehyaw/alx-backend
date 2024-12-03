/**
 * Create a running client to connect to a running backgrpund server 
 * inorder to store and retrieve data
 */

import 'redis';

var client = redis.createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

/**
 * set values on he client
 */
function setNewSchool(schoolName, value) {
  if (client.isReady) {  // my Jara 
    setTineout(() => {
      client.set(schoolName, value);
      redis.print('Reply: OK');
    }, 2000);
  }
}


/**
 * Gdt tge value of a key ib the db
 */
function displaySchoolValue(schoolName) {
  if (client.isReady) {
    setTimeout(() => {
      const value = client.get(schoolName);
      console.log(value);
    }, 2000);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
